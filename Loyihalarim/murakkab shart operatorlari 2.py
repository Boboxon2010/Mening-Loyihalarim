talabalar=[]
print("Talabalar ro'yxatini tuzamiz!")
while True:
    ism=input("Talabaning ismini kiriting yoki dasturni to'xtatish uchun exit kiriting:")
    if ism.lower()=="exit":
        break
    else:
        talabalar.append(ism.title())
print("Talabalar ro'yxati: ",talabalar)
print("Keling shu talabalarga baho qo'yamiz.")
baholanganlar={}
for i in talabalar:
    baho=input(f"Talaba {i}ning bahosini kiriting: ")
    baholanganlar[i]=baho
    
print(f"Baholangan talabalar:\n {baholanganlar}")

