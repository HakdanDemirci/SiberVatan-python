#DONGULER

meyveler =["elma","kivi","limon","bogurtlen"]
print(meyveler[2])
#2. ondisteki  meyveyi yazdi.
print(meyveler)
#hepsini yazdi
sayilar = [10,20,30,40,50]
toplam=0
for sayi in sayilar:
    toplam+=sayi
print(toplam)
#burada tum sayilari topladik


meyveler =["elma","kivi","limon","bogurtlen"]
for meyve in meyveler:
    print(meyve)


sayilar=[2,3,6,7,8,89,43,76,34,23]
for sayi in sayilar:
    if (sayi%2==0):
        continue
    else:
        print(sayi)

#burda mod kullanarak yazilan sayilari sadece teklerini print ettik

#while(kosul):
sayi=int(input("bir sayi gir"))
sayac = 0
while sayac<=sayi:
    print(sayac)
    sayac+=1

#kullanicidan 5 sayi alip bos listeye ekleyen ve en sonunda ekrana yazdiran program.
liste = []
sayac=0
while sayac<5:
    sayi = int(input("sayi gir:"))
    liste.append(sayi)
    sayac+=1
    print(liste)
