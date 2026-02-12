# while True:
#     a = input("Agar mashina olasizmi? YES/NO: ")

#     if a.upper() == "YES":
#         summa = float(input("Summani kiriting (so'mda): "))

#         if 20000000 <= summa <= 40000000:
#             print("Siz haydalgan Nexia 2, Matiz, Nexia 1 olishingiz mumkin.")

#         elif 40000000 < summa <= 70000000:
#             print("Siz 2016 Spark olishingiz mumkin.")

#         elif 70000000 < summa <= 120000000:
#             print("Siz Nexia 3 yoki yangi Spark olishingiz mumkin.")

#         elif 120000000 < summa <= 170000000:
#             print("Siz Cobalt olishingiz mumkin.")

#         elif 170000000 < summa <= 250000000:
#             print("Siz yangi GM mashina olishingiz mumkin.")

#         elif 250000000 < summa <= 400000000:
#             print("Sizga BMW 2005 mashinalari mos keladi.")

#         elif summa > 400000000:
#             print("Siz BMW M5 sotib olishingiz mumkin!")

#         else:
#             print("Bunaqa pulga metallom olasiz ⬇️")

#     elif a.upper() == "NO":
#         print("Dastur tugadi.")
#         break

#     else:
#         print("Iltimos faqat YES yoki NO deb yozing.")
dostlar=[]
print("Keling yaqin do'stlaringiz ro'yxatini tuzamiz!")
while True:
    ism = input("Uning ismini kiriting:")
    dostlar.append(ism)
    yana=input("Yana do'st qo'shamizmi? Ha/Yo'q: _")
    if yana.upper()=="HA":
        continue
    elif yana.upper()=="YO'Q":
        break
    else:
        while True:
            yana=input("Iltimos faqat Ha yoki Yo'q deb javob bering: ")
            if yana.upper()=="HA" or yana.upper()=="YO'Q":
                break
            else:
                yana=input("Iltimos faqat Ha yoki Yo'q deb javob bering: ")
                continue      
print(f"Sizning do'stlaringiz ro'yxati: {dostlar}")

