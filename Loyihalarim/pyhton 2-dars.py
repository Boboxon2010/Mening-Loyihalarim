from math import*
# input bu foydalanuvchi tomonidan kiritilgan ma'lumotni qabul qilish uchun ishlatiladi
"""ism = input("Ismingiz nima? ")
print("Salom, " + ism + "!")
yosh = input("Yoshingiz nechida? ")
print(ism + ", siz " + yosh + " yoshdasiz.")
# Foydalanuvchidan son olib, uning 1 dan 10 gacha bo'lgan ko'paytma jadvalini chiqaruvchi dastur
son = int(input("Jadvalini chiqarishni istagan soningizni kiriting: "))
for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")"""
print("1- masala: kvadratning tomoni a berilgan. Uning perimetrini hisoblovchi dastur tuzing:")
tomon = float(input("Kvadratning tomonini kiriting: "))
P=4*tomon
print("Kvadratning perimetri:",P)
print("2- masala: kvadratning tomoni a berilgan. Uning yuzini hisoblovchi dastur tuzing:")
a = float(input("Kvadratning tomonini kiriting: "))
s=pow(a,2)
print("Kvadratning yuzi:",s)
print("To'rtburchakning uzunligi va eni berilgan. Uning perimetrini va yuzini  hisoblovchi dastur tuzing:")
uzunlik = float(input("To'rtburchakning uzunligini kiriting: "))
eni = float(input("To'rtburchakning enini kiriting: "))
P=2*(uzunlik+eni)
S=uzunlik*eni
print("To'rtburchakning perimetri:",P)
print("To'rtburchakning yuzi:",S)
print("3- masala: aylananing diametri  D berilgan. Uning uzunligini hisoblovchi dastur tuzing:")
D = float(input("Aylananing diametrini kiriting: "))
L=pi*D
print("Aylananing uzunligi:",L)
