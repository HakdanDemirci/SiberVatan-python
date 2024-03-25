"""
toplam=5
liste=[]
for i in range(toplam):
    deger=int(input("yeni değer gir: "))
    if deger %3 ==0:
        liste.insert(0,deger)
    else:
        liste.append(deger)

print("liste son hali: ",liste)
#insert ile veri eklmemnin appendden farkı 2 tane veri ekleyebiliyorsun + basına 0 yazdıgımız için hep 0. indise depolıyor sayıyı sonrasında ise 3e bolunebilienler listenin basında yani solda kalıyor
"""

class kişi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}{self.age}"

k1=kişi (name="nisa",age="16")
print(k1)


class soru:
    def __init__(self,soru,cevap):
        self.soru=soru
        self.cevap=cevap
    def dogrumu(self,tahmin):
        return self.cevap == tahmin
    
soru1= soru("baskent neresi","ankara")
soru2= soru("en kalabalık şehir","istanbul")
soru3= soru("en guzel şehir","konya")
#objeler oluşturup soruları ve cevapları atadım __init__ kullanarak

dogru_cevaplar =0
sorular=[soru1,soru2,soru3]
for i in sorular:
    cevap =input(i.soru)
    if i.dogrumu(cevap):
        dogru_cevaplar +=1
print(f"dogru cevap sayisi{dogru_cevaplar}")
#3 soru sorarak cevaplandırdım bu 3 soruyu kullanıcıya soruyorum ve enson dogru cevapları gösteriyor

