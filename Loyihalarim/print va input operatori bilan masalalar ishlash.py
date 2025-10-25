print("Bugun mening tug'ilgan kunim")
#tekislikdagi berilgan ikki nuqta orasidagi masofani hisoblovchi dastur (x1)(y1);(x2)(y2)
from math import*
x1=float(input("Birinchi nuqtaning x1 koordinatasini kiriting: "))
y1=float(input("Birinchi nuqtaning y1 koordinatasini kiriting: "))
x2=float(input("Ikkinchi nuqtaning x2 koordinatasini kiriting: "))
y2=float(input("Ikkinchi nuqtaning y2 koordinatasini kiriting: "))
s=sqrt((x2-x1)**2+(y2-y1)**2)
print("Ikki nuqta orasidagi masofa:",s)

