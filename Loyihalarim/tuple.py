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

print(davlatlar)

print(len(davlatlar))

print(sorted(davlatlar))

print(sorted(davlatlar,reverse=True))

print(davlatlar)

print(reversed(davlatlar))

print(davlatlar.sort())

print(davlatlar.sort(reverse=True))

juft_sonlar=list(range(120,1201,2))

print(sum(juft_sonlar))

print(max(juft_sonlar)-min(juft_sonlar))

print(len(juft_sonlar))

print("Juft sonlar ro'yhatidagi oldingi 20 ta son:",juft_sonlar[:20],"Juft sonlar ro'yhatidagi oxirgi 20 ta qiymat:",juft_sonlar[20:])
