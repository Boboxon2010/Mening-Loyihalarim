import pygame
import sys
import os
import random
import json
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Shooting Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load sound effects
try:
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
    powerup_sound = pygame.mixer.Sound('powerup.wav')
    game_over_sound = pygame.mixer.Sound('game_over.wav')
    victory_sound = pygame.mixer.Sound('victory.wav')
except:
    print("Sound files not found. Creating dummy sounds.")
    class DummySound:
        def play(self): pass
    shoot_sound = explosion_sound = powerup_sound = game_over_sound = victory_sound = DummySound()

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5

# Load player sprite - TO'G'RI YUKLASH
try:
    # player.png faylini direktoriyadan qidiramiz
    player_image = pygame.image.load('player.png').convert_alpha()
    player_image = pygame.transform.scale(player_image, (player_size, player_size))
    print("Player image loaded successfully")
except Exception as e:
    print(f"Player image loading error: {e}")
    # Create a simple player sprite as fallback
    player_image = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
    pygame.draw.rect(player_image, BLUE, (0, 0, player_size, player_size))
    pygame.draw.circle(player_image, WHITE, (player_size//2, player_size//2), player_size//4)

# Load enemy sprite - TO'G'RI YUKLASH
bot_size = 40
try:
    # enemy.png faylini direktoriyadan qidiramiz
    enemy_image = pygame.image.load('enemy.png').convert_alpha()
    enemy_image = pygame.transform.scale(enemy_image, (bot_size, bot_size))
    print("Enemy image loaded successfully")
except Exception as e:
    print(f"Enemy image loading error: {e}")
    # Create a simple enemy sprite as fallback
    enemy_image = pygame.Surface((bot_size, bot_size), pygame.SRCALPHA)
    pygame.draw.rect(enemy_image, RED, (0, 0, bot_size, bot_size))
    pygame.draw.circle(enemy_image, WHITE, (bot_size//2, bot_size//2), bot_size//4)

# Player physics
player_y_velocity = 0
is_jumping = False
is_crouching = False
is_invulnerable = False

# Bot settings
bots = []
num_bots = 5

# Initialize bots
for _ in range(num_bots):
    bot_x = random.randint(0, WIDTH - bot_size)
    bot_y = random.randint(0, HEIGHT - bot_size)
    bots.append({
        'rect': pygame.Rect(bot_x, bot_y, bot_size, bot_size),
        'speed': random.uniform(1.0, 2.0),
        'health': 1,
        'type': 'normal'
    })

# Bullets
bullets = []
bullet_color = BLACK
bullet_speed = 10
bullet_size = 5

# Special bullets (Ctrl bosganda)
special_bullets = []
special_bullet_color = ORANGE
special_bullet_speed = 8
special_bullet_size = 8

# Bot shooting settings
bot_bullets = []
bot_bullet_color = (200, 0, 0)
bot_bullet_speed = 5
bot_shoot_chance = 0.01
bot_accuracy = 0.7

# Game states
victory = False
current_level = 1
score = 0
high_score = 0

# Load high score
try:
    with open('high_score.json', 'r') as f:
        data = json.load(f)
        high_score = data.get('high_score', 0)
except:
    high_score = 0

# Powerups
powerups = []
powerup_types = ['speed', 'rapid_fire', 'shield', 'invulnerability']
powerup_active = False
powerup_time = 0
powerup_type = ''
shield_active = False
invulnerability_active = False

# Explosions
explosions = []

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
VICTORY = 3
DIFFICULTY_SELECT = 4
current_state = MENU

def handle_jump_and_crouch(keys):
    global player_y, player_y_velocity, is_jumping, is_crouching, is_invulnerable

    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_velocity = -15
        is_jumping = True
        shoot_sound.play()

    # Shift bosganda o'tiradi va invulnerable bo'ladi
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        is_crouching = True
        is_invulnerable = True
    else:
        is_crouching = False
        is_invulnerable = False

def apply_gravity():
    global player_y, player_y_velocity, is_jumping

    player_y_velocity += 1
    player_y += player_y_velocity

    if player_y >= HEIGHT - player_size:
        player_y = HEIGHT - player_size
        player_y_velocity = 0
        is_jumping = False

def handle_movement(keys):
    global player_x, player_y

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed

    # Screen boundaries
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

def handle_shooting():
    mouse_pressed = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    
    # Oddiy o'q - sichqoncha chap tugmasi
    if mouse_pressed[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        bullet = pygame.Rect(player_x + player_size // 2, player_y + player_size // 2, bullet_size, bullet_size)
        bullets.append((bullet, mouse_x, mouse_y))
        shoot_sound.play()
    
    # Maxsus o'q - Ctrl tugmasi
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        # Eng yaqin botni top
        closest_bot = None
        min_distance = float('inf')
        
        for bot in bots:
            distance = math.sqrt((bot['rect'].x - player_x)**2 + (bot['rect'].y - player_y)**2)
            if distance < min_distance:
                min_distance = distance
                closest_bot = bot
        
        if closest_bot:
            target_x = closest_bot['rect'].x + bot_size // 2
            target_y = closest_bot['rect'].y + bot_size // 2
            bullet = pygame.Rect(player_x + player_size // 2, player_y + player_size // 2, special_bullet_size, special_bullet_size)
            special_bullets.append((bullet, target_x, target_y))
            shoot_sound.play()

def move_bullets():
    global bullets
    bullets_to_remove = []
    
    for i, (bullet, target_x, target_y) in enumerate(bullets):
        dx = target_x - bullet.x
        dy = target_y - bullet.y
        distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
        bullet.x += int(bullet_speed * dx / distance)
        bullet.y += int(bullet_speed * dy / distance)

        # Remove bullet if it goes off-screen
        if (bullet.x < 0 or bullet.x > WIDTH or 
            bullet.y < 0 or bullet.y > HEIGHT):
            bullets_to_remove.append(i)
    
    # Remove bullets in reverse order to avoid index issues
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(bullets):
            bullets.pop(i)

def move_special_bullets():
    global special_bullets
    bullets_to_remove = []
    
    for i, (bullet, target_x, target_y) in enumerate(special_bullets):
        dx = target_x - bullet.x
        dy = target_y - bullet.y
        distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
        bullet.x += int(special_bullet_speed * dx / distance)
        bullet.y += int(special_bullet_speed * dy / distance)

        # Remove bullet if it goes off-screen
        if (bullet.x < 0 or bullet.x > WIDTH or 
            bullet.y < 0 or bullet.y > HEIGHT):
            bullets_to_remove.append(i)
    
    # Remove bullets in reverse order to avoid index issues
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(special_bullets):
            special_bullets.pop(i)

def move_bots():
    global bots
    for bot in bots:
        # Simple AI: move towards player
        dx = player_x - bot['rect'].x
        dy = player_y - bot['rect'].y
        distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
        
        bot['rect'].x += int(bot['speed'] * dx / distance)
        bot['rect'].y += int(bot['speed'] * dy / distance)

def bots_shoot():
    for bot in bots:
        if random.random() < bot_shoot_chance:
            # Qiyinchilik darajasiga qarab nishon o'zgaradi
            if random.random() < bot_accuracy:
                # To'g'ri nishonga olish
                target_x = player_x
                target_y = player_y
            else:
                # Noto'g'ri nishonga olish - tasodifiy joyga
                target_x = random.randint(0, WIDTH)
                target_y = random.randint(0, HEIGHT)
            
            bullet = pygame.Rect(bot['rect'].x + bot_size // 2, bot['rect'].y + bot_size // 2, bullet_size, bullet_size)
            bot_bullets.append((bullet, target_x, target_y))

def move_bot_bullets():
    global bot_bullets
    bullets_to_remove = []
    
    for i, (bullet, target_x, target_y) in enumerate(bot_bullets):
        dx = target_x - bullet.x
        dy = target_y - bullet.y
        distance = max(1, math.sqrt(dx ** 2 + dy ** 2))
        bullet.x += int(bot_bullet_speed * dx / distance)
        bullet.y += int(bot_bullet_speed * dy / distance)

        # Remove bullet if it goes off-screen
        if (bullet.x < 0 or bullet.x > WIDTH or 
            bullet.y < 0 or bullet.y > HEIGHT):
            bullets_to_remove.append(i)
    
    # Remove bullets in reverse order to avoid index issues
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(bot_bullets):
            bot_bullets.pop(i)

def spawn_powerup():
    if random.random() < 0.005 and not powerup_active:
        powerup_type = random.choice(powerup_types)
        powerup_x = random.randint(0, WIDTH - 30)
        powerup_y = random.randint(0, HEIGHT - 30)
        powerups.append({
            'rect': pygame.Rect(powerup_x, powerup_y, 30, 30),
            'type': powerup_type,
            'color': YELLOW if powerup_type == 'speed' else 
                    PURPLE if powerup_type == 'rapid_fire' else 
                    GREEN if powerup_type == 'shield' else
                    ORANGE
        })

def check_powerup_collision():
    global player_speed, bullet_speed, powerup_active, powerup_time, powerup_type, shield_active, invulnerability_active
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for powerup in powerups[:]:
        if player_rect.colliderect(powerup['rect']):
            apply_powerup(powerup['type'])
            powerups.remove(powerup)
            powerup_sound.play()

def apply_powerup(type):
    global player_speed, bullet_speed, powerup_active, powerup_time, powerup_type, shield_active, invulnerability_active
    powerup_type = type
    powerup_active = True
    
    if type == 'speed':
        player_speed += 3
        powerup_time = 300
    elif type == 'rapid_fire':
        bullet_speed += 7
        powerup_time = 420
    elif type == 'shield':
        shield_active = True
        powerup_time = 600
    elif type == 'invulnerability':
        invulnerability_active = True
        powerup_time = 450

def remove_powerup_effects():
    global player_speed, bullet_speed, shield_active, invulnerability_active
    if powerup_type == 'speed':
        player_speed -= 3
    elif powerup_type == 'rapid_fire':
        bullet_speed -= 7
    elif powerup_type == 'shield':
        shield_active = False
    elif powerup_type == 'invulnerability':
        invulnerability_active = False

def create_explosion(x, y):
    explosions.append({
        'x': x,
        'y': y,
        'radius': 5,
        'max_radius': 30,
        'growth_rate': 2
    })
    explosion_sound.play()

def update_explosions():
    for explosion in explosions[:]:
        explosion['radius'] += explosion['growth_rate']
        if explosion['radius'] >= explosion['max_radius']:
            explosions.remove(explosion)

def draw_ui():
    font = pygame.font.Font(None, 36)
    
    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Level
    level_text = font.render(f"Level: {current_level}", True, BLACK)
    screen.blit(level_text, (10, 50))
    
    # High Score
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_text, (WIDTH - 200, 10))
    
    # Bots remaining
    bots_text = font.render(f"Bots: {len(bots)}", True, BLACK)
    screen.blit(bots_text, (WIDTH - 150, 50))
    
    # Powerup timer
    if powerup_active:
        time_text = font.render(f"{powerup_type}: {powerup_time//60}s", True, (0, 100, 0))
        screen.blit(time_text, (WIDTH // 2 - 80, 10))
    
    # Shield indicator
    if shield_active:
        shield_text = font.render("SHIELD ACTIVE", True, GREEN)
        screen.blit(shield_text, (WIDTH // 2 - 100, 50))
    
    # Invulnerability indicator
    if invulnerability_active:
        invul_text = font.render("INVULNERABLE", True, ORANGE)
        screen.blit(invul_text, (WIDTH // 2 - 100, 80))
    
    # Crouch indicator
    if is_crouching:
        crouch_text = font.render("CROUCHING - INVULNERABLE", True, BLUE)
        screen.blit(crouch_text, (10, HEIGHT - 40))
    
    # Controls help
    controls_text = font.render("LMB: Shoot | CTRL: Auto-aim | SHIFT: Crouch", True, BLACK)
    screen.blit(controls_text, (WIDTH // 2 - 200, HEIGHT - 40))

def display_message(message, color=BLACK):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

def draw_button(text, center_y):
    font = pygame.font.Font(None, 50)
    button_text = font.render(text, True, WHITE)
    button_rect = button_text.get_rect(center=(WIDTH // 2, center_y))
    pygame.draw.rect(screen, BLACK, button_rect.inflate(20, 10))
    screen.blit(button_text, button_rect)
    return button_rect

def check_victory():
    global victory, current_state, current_level, score, high_score
    
    if not bots:
        score += current_level * 100
        if score > high_score:
            high_score = score
            # Save high score
            try:
                with open('high_score.json', 'w') as f:
                    json.dump({'high_score': high_score}, f)
            except:
                pass
        
        if current_level >= 3:  # 3 levels total
            current_state = VICTORY
            victory_sound.play()
        else:
            current_level += 1
            next_level()

def check_bot_bullet_collisions():
    global current_state, bot_bullets
    
    # Agar invulnerable bo'lsa (o'tirgan yoki powerup), o'q tegmaydi
    if is_invulnerable or shield_active or invulnerability_active:
        return
        
    bullets_to_remove = []
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    
    for i, (bullet, _, _) in enumerate(bot_bullets):
        if bullet.colliderect(player_rect):
            current_state = GAME_OVER
            game_over_sound.play()
            return
    
    # Remove bullets that hit the player
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(bot_bullets):
            bot_bullets.pop(i)

def check_bullet_collisions():
    global bots, bullets, score
    
    bullets_to_remove = []
    
    for i, (bullet, _, _) in enumerate(bullets):
        for j, bot in enumerate(bots):
            if bullet.colliderect(bot['rect']):
                create_explosion(bot['rect'].x, bot['rect'].y)
                bots.pop(j)
                bullets_to_remove.append(i)
                score += 10
                break
    
    # Remove bullets in reverse order to avoid index issues
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(bullets):
            bullets.pop(i)

def check_special_bullet_collisions():
    global bots, special_bullets, score
    
    bullets_to_remove = []
    
    for i, (bullet, _, _) in enumerate(special_bullets):
        for j, bot in enumerate(bots):
            if bullet.colliderect(bot['rect']):
                create_explosion(bot['rect'].x, bot['rect'].y)
                bots.pop(j)
                bullets_to_remove.append(i)
                score += 15  # Maxsus o'q uchun ko'proq ball
                break
    
    # Remove bullets in reverse order to avoid index issues
    for i in sorted(bullets_to_remove, reverse=True):
        if i < len(special_bullets):
            special_bullets.pop(i)

def next_level():
    global bots, bot_bullets, bullets, special_bullets, powerups, explosions, player_x, player_y
    global player_y_velocity, is_jumping, is_crouching, powerup_active, shield_active, invulnerability_active
    
    # Reset player position
    player_x, player_y = WIDTH // 2, HEIGHT - player_size
    player_y_velocity = 0
    is_jumping = False
    is_crouching = False
    
    # Clear all game objects
    bots.clear()
    bot_bullets.clear()
    bullets.clear()
    special_bullets.clear()
    powerups.clear()
    explosions.clear()
    powerup_active = False
    shield_active = False
    invulnerability_active = False
    
    # Create bots for new level
    num_new_bots = 5 + (current_level - 1) * 2
    for _ in range(num_new_bots):
        bot_x = random.randint(0, WIDTH - bot_size)
        bot_y = random.randint(0, HEIGHT - bot_size)
        bots.append({
            'rect': pygame.Rect(bot_x, bot_y, bot_size, bot_size),
            'speed': random.uniform(1.0 + (current_level * 0.5), 2.0 + (current_level * 0.5)),
            'health': 1,
            'type': 'normal'
        })
    
    # Increase bot shooting chance with level
    global bot_shoot_chance
    bot_shoot_chance = min(0.05, 0.01 + (current_level * 0.01))

def reset_game():
    global player_x, player_y, bots, bot_bullets, bullets, special_bullets, powerups, explosions
    global current_level, score, victory, powerup_active, shield_active, invulnerability_active
    global player_y_velocity, is_jumping, is_crouching, is_invulnerable
    
    # Reset all game state
    player_x, player_y = WIDTH // 2, HEIGHT - player_size
    player_y_velocity = 0
    is_jumping = False
    is_crouching = False
    is_invulnerable = False
    
    bots.clear()
    bot_bullets.clear()
    bullets.clear()
    special_bullets.clear()
    powerups.clear()
    explosions.clear()
    
    current_level = 1
    score = 0
    victory = False
    powerup_active = False
    shield_active = False
    invulnerability_active = False
    
    # Initialize bots for level 1
    for _ in range(5):
        bot_x = random.randint(0, WIDTH - bot_size)
        bot_y = random.randint(0, HEIGHT - bot_size)
        bots.append({
            'rect': pygame.Rect(bot_x, bot_y, bot_size, bot_size),
            'speed': random.uniform(1.0, 2.0),
            'health': 1,
            'type': 'normal'
        })

def draw_menu():
    screen.fill(WHITE)
    
    # Title
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("SHOOTING GAME", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)
    
    # Buttons
    start_button = draw_button("Start Game", HEIGHT // 2)
    difficulty_button = draw_button("Difficulty", HEIGHT // 2 + 60)
    quit_button = draw_button("Quit", HEIGHT // 2 + 120)
    
    # High score
    font = pygame.font.Font(None, 36)
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(high_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 180))
    
    return start_button, difficulty_button, quit_button

def draw_difficulty_menu():
    screen.fill(WHITE)
    
    title_font = pygame.font.Font(None, 60)
    title_text = title_font.render("Select Difficulty", True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(title_text, title_rect)
    
    easy_button = draw_button("1. Easy", HEIGHT // 2 - 40)
    medium_button = draw_button("2. Medium", HEIGHT // 2 + 20)
    hard_button = draw_button("3. Hard", HEIGHT // 2 + 80)
    back_button = draw_button("Back", HEIGHT // 2 + 160)
    
    return easy_button, medium_button, hard_button, back_button

def set_difficulty(level):
    global bot_shoot_chance, bot_accuracy
    if level == 'easy':
        bot_shoot_chance = 0.01
        bot_accuracy = 0.7  # 70% aniq, 30% noto'g'ri
    elif level == 'medium':
        bot_shoot_chance = 0.02
        bot_accuracy = 0.85  # 85% aniq, 15% noto'g'ri
    elif level == 'hard':
        bot_shoot_chance = 0.03
        bot_accuracy = 0.95  # 95% aniq, 5% noto'g'ri

def draw_game_over():
    screen.fill(WHITE)
    display_message("Game Over", RED)
    
    score_font = pygame.font.Font(None, 50)
    score_text = score_font.render(f"Final Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(score_text, score_rect)
    
    retry_button = draw_button("Retry", HEIGHT // 2 + 60)
    menu_button = draw_button("Main Menu", HEIGHT // 2 + 120)
    
    return retry_button, menu_button

def draw_victory():
    screen.fill(WHITE)
    display_message("Victory!", GREEN)
    
    score_font = pygame.font.Font(None, 50)
    score_text = score_font.render(f"Final Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(score_text, score_rect)
    
    if score == high_score:
        record_font = pygame.font.Font(None, 40)
        record_text = record_font.render("New High Score!", True, PURPLE)
        record_rect = record_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(record_text, record_rect)
    
    retry_button = draw_button("Play Again", HEIGHT // 2 + 80)
    menu_button = draw_button("Main Menu", HEIGHT // 2 + 140)
    
    return retry_button, menu_button

def main_game_loop():
    global current_state, powerup_active, powerup_time
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    handle_movement(keys)
    handle_jump_and_crouch(keys)
    handle_shooting()
    apply_gravity()
    
    # Update game objects
    move_bullets()
    move_special_bullets()
    move_bots()
    bots_shoot()
    move_bot_bullets()
    
    # Check collisions
    check_bullet_collisions()
    check_special_bullet_collisions()
    check_bot_bullet_collisions()
    check_victory()
    
    # Powerup system
    spawn_powerup()
    check_powerup_collision()
    if powerup_active:
        powerup_time -= 1
        if powerup_time <= 0:
            remove_powerup_effects()
            powerup_active = False
    
    # Explosion animations
    update_explosions()

    # Draw everything
    screen.fill(WHITE)

    # Draw the player with effects
    if shield_active:
        shield_rect = pygame.Rect(player_x - 5, player_y - 5, player_size + 10, player_size + 10)
        pygame.draw.rect(screen, GREEN, shield_rect, 3)
    
    if invulnerability_active:
        invul_rect = pygame.Rect(player_x - 8, player_y - 8, player_size + 16, player_size + 16)
        pygame.draw.rect(screen, ORANGE, invul_rect, 3)
    
    if is_crouching:
        # O'tirganda player rasmni yarmiga kichraytiramiz
        crouch_image = pygame.transform.scale(player_image, (player_size, player_size // 2))
        screen.blit(crouch_image, (player_x, player_y + player_size // 2))
    else:
        # Oddiy holatda to'liq o'lchamda
        screen.blit(player_image, (player_x, player_y))

    # Draw bots with enemy image
    for bot in bots:
        screen.blit(enemy_image, (bot['rect'].x, bot['rect'].y))

    # Draw bullets
    for bullet, _, _ in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    # Draw special bullets
    for bullet, _, _ in special_bullets:
        pygame.draw.rect(screen, special_bullet_color, bullet)

    # Draw bot bullets
    for bullet, _, _ in bot_bullets:
        pygame.draw.rect(screen, bot_bullet_color, bullet)
        
    # Draw powerups
    for powerup in powerups:
        pygame.draw.rect(screen, powerup['color'], powerup['rect'])
        
    # Draw explosions
    for explosion in explosions:
        pygame.draw.circle(screen, (255, 165, 0), 
                          (explosion['x'], explosion['y']), 
                          explosion['radius'])
    
    # Draw UI
    draw_ui()

def main():
    global current_state, bot_shoot_chance, bot_accuracy
    
    reset_game()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if current_state == MENU:
                    start_button, difficulty_button, quit_button = draw_menu()
                    if start_button.collidepoint(mouse_pos):
                        current_state = PLAYING
                    elif difficulty_button.collidepoint(mouse_pos):
                        current_state = DIFFICULTY_SELECT
                    elif quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                
                elif current_state == DIFFICULTY_SELECT:
                    easy_button, medium_button, hard_button, back_button = draw_difficulty_menu()
                    if easy_button.collidepoint(mouse_pos):
                        set_difficulty('easy')
                        current_state = MENU
                    elif medium_button.collidepoint(mouse_pos):
                        set_difficulty('medium')
                        current_state = MENU
                    elif hard_button.collidepoint(mouse_pos):
                        set_difficulty('hard')
                        current_state = MENU
                    elif back_button.collidepoint(mouse_pos):
                        current_state = MENU
                
                elif current_state == GAME_OVER:
                    retry_button, menu_button = draw_game_over()
                    if retry_button.collidepoint(mouse_pos):
                        reset_game()
                        current_state = PLAYING
                    elif menu_button.collidepoint(mouse_pos):
                        reset_game()
                        current_state = MENU
                
                elif current_state == VICTORY:
                    retry_button, menu_button = draw_victory()
                    if retry_button.collidepoint(mouse_pos):
                        reset_game()
                        current_state = PLAYING
                    elif menu_button.collidepoint(mouse_pos):
                        reset_game()
                        current_state = MENU
        
        if current_state == MENU:
            draw_menu()
        
        elif current_state == DIFFICULTY_SELECT:
            draw_difficulty_menu()
        
        elif current_state == PLAYING:
            main_game_loop()
        
        elif current_state == GAME_OVER:
            draw_game_over()
        
        elif current_state == VICTORY:
            draw_victory()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()