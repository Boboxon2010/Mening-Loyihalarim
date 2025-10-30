"""
ismlar=["Ixtiyor","Elbek","Ahrorbek"] #oddiy ro'yhat
familya=("Baxtiyorov","Jabborov","Komiljanov") #o'zgarmas ro'yhat
print("oddiy ro'yhat",ismlar)
print("o'zgarmas ro'yhat",familya)
ismlar.append("Mustafo")
#o'zgarmas ro'yhatga qiymat qo'shish
last_name=list(familya)
last_name.append("Davletov")
familya=tuple(last_name)
print(familya)
"""
#amaliyot
davlatlar=["O'zbekiston","Rossiya","Portugaliya","Fransiya","Qirg'iziston","Turkmaniston"]

print("davlatlar ro'yhati asl nusxasi:",davlatlar)

print("Davlatlar ro'yhatidagi elementlar soni:",len(davlatlar))

print("davlatlar ro'yhatini alifbo bo'yicha tartibi:",sorted(davlatlar))

print("davlatlar ro'yhatini teskari tartibi:",sorted(davlatlar,reverse=True))

print(davlatlar)

print("davlatlar ro'yhatini teskari tartibi",reversed(davlatlar))
davlatlar.sort()
print("davlatlar ro'yhatini alifbo bo'yicha tartibi:",davlatlar)
davlatlar.sort(reverse=True)
print("davlatlar ro'yhatini teskari tartibi:",davlatlar)

juft_sonlar=list(range(120,1201,2))

print("juft sonlar ro'yhatidagi qiymatlar yig'indisi:",sum(juft_sonlar))

print("Juft sonlar ro'yhatidagi elementlarning eng katta va eng kichikining farqi:",max(juft_sonlar)-min(juft_sonlar))

print("Juft sonlar ro'yhatidagi elementlar soni:",len(juft_sonlar))

print("Juft sonlar ro'yhatidagi oldingi 20 ta son:",juft_sonlar[:20],"Juft sonlar ro'yhatidagi oxirgi 20 ta qiymat:",juft_sonlar[20:])

