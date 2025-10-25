# Foydalanuvchidan son olib, uning 1 dan 10 gacha bo'lgan ko'paytma jadvalini chiqaruvchi dastur
son = int(input("Jadvalini chiqarishni istagan soningizni kiriting: "))
for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")