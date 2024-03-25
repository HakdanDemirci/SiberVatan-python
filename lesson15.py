"""
kelime=input("Lütfen kelime Giriniz:")
kelimenintersi=kelime[::-1]
print("girilen kelimenin tersi = %s " % (kelimenintersi))
if kelimenintersi == kelime :
    print("girilen kelime palindrom")
else:
    print("girilen kelime palindrom değil")
"""
"""
#bir kelimenin polindrom olup olmadıgını anlayan fonksiyon
kelimenintersi=kelime[::-1]
def polindrom_mu (kelime):
    temiz_kelime=kelime.upper()
    return temiz_kelime== temiz_kelime[::-1]

kelime=input("Lütfen kelime Giriniz:")
if polindrom_mu(kelime):
    print("bu polindrom bir kelimedir")
else:
    print("bu polindrom bir kelime değildir")

"""
"""
#kullanıcıdan iki liste alıp bu listenin ortak elemanlarını bulan bir fonksiyon
def ortak_elemanlar(list1, list2):
    ortakolanlar = []
    for eleman in list1:
        if eleman in list2:
            ortakolanlar.append(eleman)
    return ortakolanlar

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
ortakolanlar = ortak_elemanlar(list1, list2)
print("ortak elemanlar", ortakolanlar)
#benim yaptıgım

def ortak_elamanlar(liste1,liste2):
    ortaklar = liste= []
    for i in liste1:
        if i in liste2:
            liste.append(i)
    return ortaklar

liste1 = [1,2,3,4,5]
liste2 = [3,4,5,6,7]

ortaklar= ortak_elamanlar(liste1,liste2)
print=("listelerin ortak elamnaları",ortaklar)
#hocanın yaptıgı
"""
"""
dict={"anahtar1":"deger1","anahtar2":"deger2"}
print(dict)

anahtar=dict["deger1"]
print(anahtar)
#keylerden value degerlere geciş var ama value degerlerden key degrlere direkt geçiş yok
"""
"""
#verilan bir listedeki her bir elamanın frekansını(sıklığı) bulan bir fonksiyon yazınız
kullanici_girişi1=input("Lütfen 1 kelime Giriniz:")
kullanici_girişi2=input("Lütfen 1 harf Giriniz:")
strg=kullanici_girişi1
str_count=strg.count(kullanici_girişi2)
print(str_count)
#benim yaptığım (fonksiyon kullanılmadan)

def elaman_frekansi(liste1):
    frekanslar= {}
    for elaman in liste1:
        if elaman in frekanslar:
            frekanslar[elaman]+=1 
        else:
            frekanslar[elaman] =1

    return frekanslar

liste1=[2,3,5,7,7,9,96,3,5,2,6,8]

sonuc= elaman_frekansi(liste1)
for elaman,frekans in sonuc.items():
    print(f"{elaman}:{frekans}")
#hocanın yaptıgı doğru olan
"""

#verilen bir pozitif tam sayı için fibonacci dizisnin ilk n terimini hesaplayan bir fonksiyon programı
def fibonacci(n):
    fibonacci_sayıhesap = [0,1]
    for i in range (2,n):
        fibonacci_sayıhesap.append(fibonacci_sayıhesap[-1]+fibonacci_sayıhesap[-2] )
    return fibonacci_sayıhesap[:n]

n=10
print(fibonacci(n))
#benim yaptığım

def fibonacci(n):
    fibo= [0,1]
    for i in range(2,n):
        next= fibo[-1]+fibo[-2]
        fibo.append(next)
    return fibo

n=10
fibo=fibonacci(n)
print(f"{fibo}")
#abdülkadir hocanın yaptığı 
