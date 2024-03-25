#print("hello world")

#siber vatan

print("karabuk")

sayi=10
sayi=100
print(sayi) 
#100 ü çıktı verir


yas=10
YAS=100
print(yas)
#10 u çıktı verir


print(2**4)
 #ustunu alam islemi
print(2*4) 
#carpma islemi
print(2+4)
 #toplama
print(2-4) 
#cıkarma


#adi,yas,sehir=("ali",15,"konya")//sayılara tırnak konmuyo

kelime="merhaba\n dunya"
print (kelime)
#\n kullanarak kaçış dizgisi yaptık yani dunya alt satırda gozukcek

x,y,z=(4,5,6)

sayilar="10"
sayilar1="20"
print(sayilar+sayilar1) 
#string olarak algıladığı için 20 çıktısını verir

maas=17002
vergi=0.20
print(17002 - (17002*0.20))
#atamaları değişken içine yapınca daha kolay ve değiştirilmesi kolay olur
print(maas - (maas*vergi)) 
#eger boyle yaparsak daha kolay olur ,işlemleri değişken içinden yapmak daha saglıklı

isim="ahmet"
print("merhaba,"+ isim + "hosgeldin") 
#banka sistemi mesaj mantıgı

# = atamada kullanılır
# == değişkeni doğrulamada kullanıır
# <= küçük eşittir <=buyuk eşittir


sayi=-7
print("mutlak deger",abs(sayi)) 
#abs( ) mutlak deger alır


us=pow(2,3) 
#pow() sayı üssünü alır
print("sayi ussu",us)

from math import sqrt,ceil,floor 
#sqrt karekok alma yani sqrt ekliyoruz burdan
sayi=25
karekok=sqrt(sayi)
#sqrt() kullanarak sayını karekodu alınır
print("sayinin karekoku",karekok)

from math import ceil,floor 
#burda yine ceil ve flooru tanımlasım kütüphane gibi
ondalik=10.25
yukari= ceil(ondalik)
asagi= floor(ondalik)
print("yukari",yukari)
print("asagi",asagi)
