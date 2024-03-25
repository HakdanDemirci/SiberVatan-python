# YENİ VERİ TİPLERİ VE LİSTELER #
#list
liste=[1,2,3,4,5]
#list tanımlrken köşeli parantez kullanıyoeuz

print(liste)
print(liste[2])
print(type(liste))

liste[2]=7
print(liste) 
#atama sağdan sola yapılır

alt_liste= liste[2:4]
print(alt_liste)
#2. ile 4. karakteri veriyor

#tuple
tuple=(10,20,30)
print(tuple)
print(tuple[1])

#tuple[1]=50
#print(tuple)
#hata verir

alt_tuple= tuple[1:4]
print(alt_tuple)

#kumeler(sets)
kume={100,200,300,400,500,100}
print(kume)
#birden fazla aynı dğeri yazarsan sana aynı degeri vemez ve hep farklı sırada verir

kume.add(700)
print(kume)
#yine farklı ve karışık sekilde verir

print(type(kume))
#set çıktısını verir, <class 'set'> bu çıktıyoı verdi

kume.update([400,900])
print(kume)
#güncelleme yaptı


#dict (dictionary, sözlük)

dict={"anahtar1":"deger1","anahtar2":"deger2"}
print(dict)
#{'anahtar1': 'deger1', 'anahtar2': 'deger2'} çktısı verdi

deger=dict["anahtar1"]
print(deger)
#deger1 çıktısını verdi


#DÖNÜŞÜMLER#

kume_list=list(kume)
print("kume to list",kume_list)
#kumeyi listeye çevirdik
print(type(kume_list))

kume_tuple= set(tuple)
print("tuple to kume",kume_tuple)
#kumeyi tuple cevirdik


list_keys=list(dict.keys())
print(type(list_keys))
print(list_keys)
#anahtarı listeye ceviriyor

list_values=list(dict.values())
print(type(list_values))
print(list_values)
#degri listeye ceviriyor


sayilar=[10,8,5,3,15]
en_buyuk=max(sayilar)
en_kucuk=min(sayilar)
print(en_buyuk)
print(en_kucuk)
#en buyuk ve en kucuk sayilari min vr max faonksiyonu sayesinde yazdırıyor

sayilar.append(20)
sayilar.append(1)
#append listeye yeni degr ekler

yeni_en_buyuk=max(sayilar)
yeni_en_kucuk=min(sayilar)
#yeniden tanımladik çünkü 1i ve 20i ekledik

print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayilar)
#yeni degerlerle birlikte yazdırıyor hepsini


#KUYRUK YAPILARI:
#FIFO ve LIFO
#FIFO = ilk giren ilk çıkar
#LIFO = son giren ilk çıkar

sayilar.pop()
print(sayilar)
#son girilen sayıyı çıkarıyor

sayilar.sort()
print(sayilar)
#sayiları buyukluk kçüklüğüne göre sıraya soktu, alfabetik sıraya görede sıralar

sayilar.reverse()
print(sayilar)
#tersten yazıyor yani en son girilen başa yazılıyor

print(sayilar.count(10))
#içinde kaç tane 10 olduğunu ölçer

aralik = range(1,100)
print(list(aralik))
#1 ile 100 arasındaki sayıları veriyor range=aralık

import random
rastgele_sayi= random.randint(1,100)
print("tutulan sayi",rastgele_sayi)
#rastgele sayı tutmak için yapılan işlem randint:rastgale tam sayı





