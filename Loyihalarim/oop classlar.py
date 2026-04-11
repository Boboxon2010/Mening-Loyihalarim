from datetime import datetime
dt = datetime.now()
class Talaba:
    def __init__(self,ism,familya,otasining_ismi,tyil):
        self.name = ism
        self.familya = familya
        self.tyil = tyil
        self.ochestva = otasining_ismi
    def FIO(self):
        return f"{self.familya.title()} {self.name} {self.ochestva}"
    def yoshi(self):
        return f"{dt.year-self.tyil}-yoshda"


t1 = Talaba('kamolbek','ruzmamatov','vohidjonovich',2010)
t2 = Talaba('ixtiyor','baxtiyorov','anvarbekovich',2010)
t3 = Talaba('umidbek','matyakubov','umirbekovich',2010)

print(t1.FIO(), t1.yoshi(), t2.FIO(), t2.yoshi(), t3.FIO(), t3.yoshi())

