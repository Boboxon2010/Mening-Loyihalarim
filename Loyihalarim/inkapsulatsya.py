# #python bu dasturlash tilida inkapsulatsiya (encapsulation) - bu ma'lumotlarni va ularni boshqarish uchun kerakli metodlarni bir joyga to'plash va tashqi muhitdan himoya qilish konsepsiyasidir. Inkapsulatsiya yordamida biz ma'lumotlarni yashirish va faqat kerakli metodlar orqali ularga kirish imkoniyatini yaratamiz.
# from uuid import uuid4
# a= uuid4()

# class Shaxs:
#     foydalanilganlik_soni=0
#     def __init__(self,ism,familiya,yosh,tyil,jshr):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.tyil = tyil
#         self.__id = jshr
#         Shaxs.foydalanilganlik_soni+=1
#     def get_jshr(self):
#         return self.__id
#     def get_name(self):
#         return self.ism
#     def get_surname(self):
#         return self.familiya
#     def get_age(self):
#         return self.yosh
#     def get_birth_year(self):
#         return self.tyil
#     def get_class_foydalanilganlik_soni(cls):
#         return cls.foydalanilganlik_soni
# talaba = Shaxs('kamolbek','ruzmamatov',14,2010,'123456789')
# print(talaba.get_name().title(),talaba.get_surname().title(),talaba.get_age(), talaba.get_birth_year())
# print(talaba.get_jshr())

# t1=Shaxs("Kamoltoy","Murodov",14,2010,'123456789')
# t2=Shaxs("Ixtiyor","Baxtiyorov",14,2010,'123456789')
# t3=Shaxs("Umidbek","Matyakubov",14,2010 ,'123456789')
# t4=Shaxs("Sardor","Murodov",14,2010,'123456789')
# print(Shaxs.get_class_foydalanilganlik_soni())
from uuid import uuid4
class mashina:
    def __init__(self,nomi,rangi,km):
        self.nomi = nomi
        self.rangi = rangi
        self.__kuzov_raqami = uuid4()
        self.__km = km
    def get_mashina_nomi(self):
        return self.nomi.title()
    def get_mashina_rangi(self):
        return self.rangi.title()
    def get_kuzov_raqami(self):
        return self.__kuzov_raqami
    def get_km(self):
        return f"{self.get_mashina_nomi()} ning probegi: {self.__km} km"
    def get_kuzov_raqami(self):
        return f"{self.get_mashina_nomi()} ning kuzov raqami: {self.__kuzov_raqami}"
mashina1 = mashina('nexia','oq',100000)
print(mashina1.get_mashina_nomi(), mashina1.get_mashina_rangi())
print(mashina1.get_km())
print(mashina1.get_kuzov_raqami())
    