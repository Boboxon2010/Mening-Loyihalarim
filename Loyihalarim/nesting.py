# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 11:27:44 2025

@author: Boboxon
"""

#nesting bu lug'at ichida lug'at, lug'at ichida ro'yhat , ro'yhat ichida lug'at , ro'yhat ichida ro'yhat saqlash uchun kerak
 
#ro'yhat ichida lug'at⬇️⬇️⬇️
car0 = {
        "Model": "Nexia 3",
        "rang": "qora",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
car1 = {
        "Model": "Nexia 2",
        "rang": "Oq",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
car2 = {
        "Model": "Nexia 1",
        "rang": "qora",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
car3 = {
        "Model": "Malibu 2",
        "rang": "Oq",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
car4 = {
        "Model": "Malibu turbo",
        "rang": "qora",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
car5 = {
        "Model": "Tracker premier",
        "rang": "qora",
        "Yili":2024,
        "yurgan yo'li km":"0 km"}
cars=[car0,car1,car2,car3,car4,car5] #nesting

for car in cars:
    if car["Model"]=="Nexia 1" or car["Model"]=="Nexia 2":
        car["rang"]="Moviy"
        
""" _________________________________________________"""
#Lugat ichida ro'yhat ⬇️⬇️⬇

dasturchilar={
    "Boboxon":['Python','HTML','CSS','JavaScript'],
    "Ixtiyor":['HTML','CSS'],
    "Elbek":['Python','HTML','CSS'],
    "Kamol":['Python','HTML','CSS'],
    "Muhammadali":['Pyhton','JavaScript','HTML','CSS'],
    "Baxtiyor":['HTML','CSS','Python']
    }
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()},",end='')

    