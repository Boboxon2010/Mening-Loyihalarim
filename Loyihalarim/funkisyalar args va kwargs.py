# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 17:56:31 2025

@author: Boboxon
"""

#hohlagancha qiymat kiritish mumkin bo'lgan funksiya

# def summa(*sonlar):
#     """Kiritilgan sonlar yigindisini hisoblovchi funksiya"""
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(summa(14,15,141,1,41,1,41,21,453,5468,74,1,846,4684,3,57,86))
# print(summa(65,5))
# print(summa(45,54))

"""  **kwargs  """

def avto_info(komponiya,model,**malumotlar):
    """Avtomobillar haqidagi malumotni qaytaruvchi funksiya"""
    malumotlar["komponiya"]=komponiya
    malumotlar["model"]=model
    return malumotlar
avto_info("BMW", "M5", mator="V8")


def kopaytma(*sonlar):
    
    
    natija=1
    for i in sonlar:
        i=int(i)
        natija*=i
    return natija
kopaytma(654,4,5)
print(kopaytma)
