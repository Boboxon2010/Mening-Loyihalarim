# input bu foydalanuvchi tomonidan kiritilgan ma'lumotni qabul qilish uchun ishlatiladi
ism = input("Ismingiz nima? ")
print("Salom, " + ism + "!")
yosh = input("Yoshingiz nechida? ")
print(ism + ", siz " + yosh + " yoshdasiz.")
# Foydalanuvchidan son olib, uning 1 dan 10 gacha bo'lgan ko'paytma jadvalini chiqaruvchi dastur
son = int(input("Jadvalini chiqarishni istagan soningizni kiriting: "))
for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")
