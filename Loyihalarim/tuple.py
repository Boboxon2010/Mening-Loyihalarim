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