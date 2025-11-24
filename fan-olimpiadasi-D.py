import sys
sys.setrecursionlimit(10000)

def solve_game(n):
    """
    Kalkulyator o'yinini yechish.
    0 ga yetkazgan kishi yutqazadi (oxirgi harakat qilgan yutqazadi).
    """
    if n == 0:
        return "Husanboy"
    
    if n == 1:
        # 1 dan hech qanday harakat qilish mumkin emas
        # Mardon harakat qila olmaydi, demak Mardon yutqazadi
        return "Husanboy"
    
    memo = {}
    
    def can_first_player_win(num):
        """
        Joriy o'yinchi (birinchi harakat qiluvchi) bu sondan yutishi mumkinmi?
        True - yutadi, False - yutqazadi
        """
        if num == 0:
            # 0 ga yetgan o'yinchi allaqachon yutqazgan (oldingi o'yinchi oxirgi harakatni qilgan)
            return False
        
        if num == 1:
            # 1 dan harakat qilish mumkin emas, joriy o'yinchi yutqazadi
            return False
        
        if num in memo:
            return memo[num]
        
        # Barcha mumkin bo'lgan harakatlarni tekshirish
        
        # 1. x ni ayirish (1 < x < num)
        for x in range(2, num):
            result = num - x
            # Agar raqib yutqazsa, biz yutamiz
            if not can_first_player_win(result):
                memo[num] = True
                return True
        
        # 2. x ga bo'lish (1 < x <= num va num % x == 0)
        divisors = []
        for x in range(2, int(num**0.5) + 1):
            if num % x == 0:
                divisors.append(x)
                if x != num // x:
                    divisors.append(num // x)
        divisors.append(num)  # O'ziga bo'lish (natija 1)
        
        for x in divisors:
            if x > 1:
                result = num // x
                # Agar raqib yutqazsa, biz yutamiz
                if not can_first_player_win(result):
                    memo[num] = True
                    return True
        
        # Hech qanday yutuvchi harakat topilmadi
        memo[num] = False
        return False
    
    # Mardon birinchi o'ynaydi
    if can_first_player_win(n):
        return "Mardon"
    else:
        return "Husanboy"


# Asosiy dastur
def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        winner = solve_game(n)
        print(winner)


if __name__ == "__main__":
    main()