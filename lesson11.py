#basamakların aynı olup olmadığını ölçen program asıl yer 4. satır
def sayi_kontrol(sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str)) ==1:
        return 1
    else:
        return 0
    
A = [233,45,777,81,99999,36,90,88,11,61,513]
for sayi in A:
    if sayi_kontrol(sayi):
        print(f"{sayi}:basamakları aynı")
    else:
        print(f"{sayi}:basamakları farklı")

print("#######################################################################")

#CLASS SİSTEMİ
liste=[10,20,30]
print(type(liste))
#listenin tipini sorguladım

class Person:
    adress = "bilgi yok"
    def __init__(self,name,lname,adress,dogum):
        self.name = name
        self.lname = lname
        self.adress= adress
        self.dogum = dogum
    def intro(self):
        print("merhaba ben "+ self.name)
    def calculate(self):
        return 2024- self.dogum
p1 = Person(name="ali" ,lname="koç",adress="100.yıl",dogum=2000)
print(p1)
print("benim adım" ,p1.name)
print("benim adım" ,p1.name, "benim soyadım",p1.lname,"benim adresim",p1.adress,"doğum yılım",p1.dogum)

p2 = Person(name="nisa" ,lname="agaccioglu",adress="karabuk merkez",dogum=2008)
print(p2)
print("benim adım" ,p2.name)
print("benim adım" ,p2.name, "benim soyadım",p2.lname,"benim adresim",p2.adress,"doğum yılım",p2.dogum)

p1.intro()
p2.intro()
p1.yashesabı()
p2.yashesabı()




