from math import*
#masala 13: umumiy markazga ega bo'lgan ikkita aylana raduisi berilgan. s1 va s2 ularning ayirmasi s3 aniqlansin.
r1=float(input("Birinchi aylana radiusini kiriting: "))
r2=float(input("Ikkinchi aylana radiusini kiriting: "))
s1=pi*r1
s2=pi*r2
s3=pi*(r1-r2)
print("Birinchi aylananing yuzasi",s1)
print("Ikkinchi aylananing yuzasi",s2)
print("Aylanalarning yuzalari ayirmasi",s3)
#masala 16: sonlar o'qida ikkita nuqta oraliqidagi masofa aniqlansin: 
x1=float(input("Birinchi nuqtaning koordinatasini kiriting: "))
x2=float(input("Ikkinchi nuqtaning koordinatasini kiriting: "))
d=abs(x2-x1)
print("Nuqtalar orasidagi masofa:",d)
#masala 17: sonlar o'qida A ,B,C nuqtalar berilgan. AC va BC kesmalarining uzunliklari va kesmalar uzunliking yigindisi aniqlansin.
A=float(input("A nuqtaning koordinatasini kiriting: "))
B=float(input("B nuqtaning koordinatasini kiriting: "))
C=float(input("C nuqtaning koordinatasini kiriting: "))
AC=abs(C-A)
BC=abs(C-B)
yigindi=AC+BC
print("AC kesmasi uzunligi:",AC)
print("BC kesmasi uzunligi:",BC)
print("AC va BC kesmalari uzunliklarining yig'indisi:",yigindi)
#X kg konfetning narxi A so'm. 1 kg konfetning narxi va Y kg konfetning narxi aniqlansin.
X=float(input("Konfetning og'irligini kiriting (kg): "))
A=float(input("Konfetning narxini kiriting (so'm): "))
Y=float(input("Nechta kg konfet olmoqchisiz: "))
narx1=A/X
narx2=Y*narx1
print("1 kg konfetning narxi:",narx1,"so'm")
print(Y,"kg konfetning narxi:",narx2,"so'm")

