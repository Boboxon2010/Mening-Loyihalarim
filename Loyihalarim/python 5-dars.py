# string metodlari 

# title() - har bir so'zning birinchi harfini katta qiladi
"""
ism = "bobur"
familiya = "murodov"
otchestva = "abdurahmonovich"
FIO= f"Assalomu aleykum {familiya} {ism} {otchestva}!"
print(FIO)
print(FIO.title())
"""
# capitalize() - faqat birinchi harfni katta qiladi
"""
text = "hello world! welcome to python programming."
print(text.capitalize())

"""
# upper() - matndagi barcha harflarni katta qiladi
#   print(text.upper())
# lower() - matndagi barcha harflarni kichik qiladi
#   print(text.lower())
#   print(text.casefold())  # lower() ga o'xshash
# swapcase() - katta harflarni kichik, kichik harflarni katta qiladi
#   print(text.swapcase())
# count() - matnda nechta ma'lum bir harf yoki so'z borligini hisoblaydi

text = "python dasturlash tili juda qiziqarli va oson til"
natija = text.count("til")
print("til so'zi matnda", natija, "marta ishlatilgan")

# find() - matnda ma'lum bir harf yoki so'zning birinchi uchrashgan joyini ko'rsatadi
pozitsiya = text.find("qiziqarli")
print("qiziqarli so'zi matnda", pozitsiya, "pozitsiyada boshlanadi")
# rfind() - matnda ma'lum bir harf yoki so'zning oxirgi uchrashgan joyini ko'rsatadi
pozitsiya2 = text.rfind("til")
print("til so'zi matnda oxirgi marta", pozitsiya2, "pozitsiyada boshlanadi")
# index() - find() ga o'xshash, lekin agar so'z topilmasa xato beradi
pozitsiya3 = text.index("dasturlash")
print("dasturlash so'zi matnda", pozitsiya3, "pozitsiyada boshlanadi")
# rindex() - rfind() ga o'xshash, lekin agar so'z topilmasa xato beradi
pozitsiya4 = text.rindex("til")
print("til so'zi matnda oxirgi marta", pozitsiya4, "pozitsiyada boshlanadi")
# strip() - matn boshidagi va oxiridagi bo'shliqlarni olib tashlaydi
text2 = "   Hello, World!   "
print("Boshidagi va oxiridagi bo'shliqlar olib tashlandi:", text2.strip())
# lstrip() - matn boshidagi bo'shliqlarni olib tashlaydi
print("Boshidagi bo'shliqlar olib tashlandi:", text2.lstrip())
# rstrip() - matn oxiridagi bo'shliqlarni olib tashlaydi
print("Oxiridagi bo'shliqlar olib tashlandi:", text2.rstrip())
# replace() - matndagi ma'lum bir so'zni boshqasi bilan almashtiradi
text3 = "I love programming. Programming is fun."
text4 = text3.replace("programming", "coding")
print("Almashtirilgan matn:", text4)
# split() - matnni so'zlarga ajratadi
text5 = "Python dasturlash tili juda qiziqarli"
sozlar = text5.split()
print("So'zlar ro'yxati:", sozlar)
# join() - so'zlar ro'yxatini bitta matnga birlashtiradi
sozlar2 = ['Python', 'dasturlash', 'tili', 'juda', 'qiziqarli']
matn = ' '.join(sozlar2)
print("Birlashtirilgan matn:", matn)
# isdigit() - matn faqat raqamlardan iboratligini tekshiradi
text6 = "12345"
print("Matn faqat raqamlardan iboratmi?", text6.isdigit())
# isalpha() - matn faqat harflardan iboratligini tekshiradi
text7 = "HelloWorld"
print("Matn faqat harflardan iboratmi?", text7.isalpha())
# isalnum() - matn faqat harflar va raqamlardan iboratligini tekshiradi
text8 = "Hello123"
print("Matn faqat harflar va raqamlardan iboratmi?", text8.isalnum())
# isspace() - matn faqat bo'shliqlardan iboratligini tekshiradi
text9 = "     "
print("Matn faqat bo'shliqlardan iboratmi?", text9.isspace())
# startswith() - matn ma'lum bir so'z yoki harf bilan boshlanishini tekshiradi
text10 = "Python dasturlash tili"
print("Matn 'Python' so'zi bilan boshlanadimi?", text10.startswith("Python"))
# endswith() - matn ma'lum bir so'z yoki harf bilan tugashini tekshiradi
print("Matn 'tili' so'zi bilan tugaydimi?", text10.endswith("tili"))    
# center() - matnni markazlashtiradi
text11 = "Hello"
print("Markazlashtirilgan matn:", text11.center(20, '*'))
# ljust() - matnni chapga tekislaydi
print("Chapga tekislangan matn:", text11.ljust(20, '-'))
# rjust() - matnni o'ngga tekislaydi
print("O'ngga tekislangan matn:", text11.rjust(20, '+'))
# zfill() - matn boshiga 0 lar qo'shadi
text12 = "42"
print("Boshiga 0 lar qo'shilgan matn:", text12.zfill(5))
# format() - matnga qiymatlarni joylashtiradi
name = "Alice"
age = 30
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(formatted_text)
# expandtabs() - matndagi tabulyatsiya belgilarini bo'shliqlarga aylantiradi
text13 = "Hello\tWorld\tPython"
print("Tabulyatsiya belgilarini bo'shliqlarga aylantirilgan matn:", text13.expandtabs(4))
# encode() - matnni belgilangan kodlashga aylantiradi
text14 = "Hello, World!"
encoded_text = text14.encode('utf-8')
print("Kodlangan matn:", encoded_text)
# decode() - kodlangan matnni asl holatiga qaytaradi
decoded_text = encoded_text.decode('utf-8')
print("Asl holatiga qaytarilgan matn:", decoded_text)   
# islower() - matndagi barcha harflar kichik ekanligini tekshiradi
text15 = "hello world"
print("Matndagi barcha harflar kichikmi?", text15.islower())
# isupper() - matndagi barcha harflar katta ekanligini tekshiradi
text16 = "HELLO WORLD"
print("Matndagi barcha harflar katta mi?", text16.isupper())
# istitle() - matndagi har bir so'zning birinchi harfi katta ekanligini tekshiradi
text17 = "Hello World"
print("Matndagi har bir so'zning birinchi harfi katta mi?", text17.istitle())
# maketrans() va translate() - matndagi belgilarni almashtirish uchun xarita yaratadi va qo'llaydi
text18 = "hello world"
translation_table = str.maketrans("hel", "123")
translated_text = text18.translate(translation_table)
print("Almashtirilgan matn:", translated_text)
# partition() - matnni ma'lum bir so'z bo'yicha uch qismga bo'ladi
text19 = "Python dasturlash tili"
parted_text = text19.partition("dasturlash")
print("Bo'lingan matn:", parted_text)
# rpartition() - matnni ma'lum bir so'z bo'yicha uch qismga bo'ladi (oxirgi uchrashuvdan)
text20 = "Python dasturlash tili dasturlash"
rparted_text = text20.rpartition("dasturlash")
print("Oxirgi uchrashuvdan bo'lingan matn:", rparted_text)
# splitlines() - matnni qatorlarga bo'ladi
text21 = "Hello World!\nWelcome to Python.\nEnjoy coding!"
lines = text21.splitlines()
print("Qatorlarga bo'lingan matn:", lines)
# isprintable() - matndagi barcha belgilar chop etiladiganligini tekshiradi
text22 = "Hello World!"
print("Matndagi barcha belgilar chop etiladimi?", text22.isprintable())
# bytes() - matnni baytlarga aylantiradi
text23 = "Hello"
byte_text = bytes(text23, 'utf-8')
print("Baytlarga aylantirilgan matn:", byte_text)
# ord() - belgining ASCII yoki Unicode kodini qaytaradi
char = 'A'
print("Belgining ASCII kodi:", ord(char))
# chr() - ASCII yoki Unicode kodidan belgini qaytaradi
code = 65
print("ASCII kodidan belgini qaytarish:", chr(code))
# format_map() - lug'atdagi qiymatlarni matnga joylashtiradi
data = {'name': 'Bobur', 'age': 25}
formatted_text2 = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_text2)
# isidentifier() - matnning yaroqli identifikator ekanligini tekshiradi
text24 = "variable_name"
print("Matn yaroqli identifikatormi?", text24.isidentifier())
# (Removed duplicate partition() demonstration)
# rpartition() - matnni ma'lum bir so'z bo'yicha uch qismga bo'ladi (oxirgi uchrashuvdan)
text26 = "Python dasturlash tili dasturlash"
rparted_text2 = text26.rpartition("dasturlash")
print("Oxirgi uchrashuvdan bo'lingan matn:", rparted_text2)
# splitlines() - matnni qatorlarga bo'ladi
text27 = "Hello World!\nWelcome to Python.\nEnjoy coding!"
lines2 = text27.splitlines()
print("Qatorlarga bo'lingan matn:", lines2)
# isprintable() - matndagi barcha belgilar chop etiladiganligini tekshiradi
text28 = "Hello World!"
print("Matndagi barcha belgilar chop etiladimi?", text28.isprintable())
