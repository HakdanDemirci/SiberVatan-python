#STRİNG (dizi,koşul) İŞLEMLERİ# 
ad= "nisa"
soyad= "agaccioglu "
yas= 16
print("benim adım",ad,soyad,"yasım",yas)
#benim adım nisa agaccioglu yasım 16 çıktısı verdi 

karsilama= "  benim adım " + ad + " " + soyad + "yasın " +str(yas) + " hosgeldin" 
print(karsilama)
#str fonksiyonunun içine alip inte çevirebiliyoruz 
#benimadimnisa agacciogluyasın 16hosgeldin çıktısı verdi

uzunluk = len(karsilama)
print(uzunluk)
#karsilama diye tanımladğımız yerin uzunlugunu verir
# len() fonksiyonunu kullanıyoruz

print(karsilama[3])
#phyton yazılım dilinde indis 0 dan başlıyo ve indiste sayılar köşeli parantez ile yazılır

print(karsilama[-3])
#köşeli parantez içine - yazarsak buda sondaki karakteri vaeriyo

print(karsilama[4:10])
#4. ile 10. karakterler arasını veriyor

print(karsilama[0:10])
#0. ile 10. karakterler arasını veriyor

print(karsilama[:14])
#0. ile 14. karakterler arasını veriyor

print(karsilama[10:])
#10.karakterden baslayıp veriyor

print(karsilama[2:25:3])
#2. karakterden 25. karaktare kadar veriyor ama hepsinin 3. karakterini veriyor

print(karsilama[:-3])
#son 3 karakteri almıyor

print(karsilama[::-1])
#tersten yazıyor hepsini 

print(karsilama[::-5])
#tersten yazıyor ama 5 karakterden birisi

karsilama_upper=karsilama.upper()
print(karsilama_upper)
#karakterlerin hepsini buyutuyor

karsilama_lower=karsilama.lower()
print(karsilama_lower)
#karakterlerin hepsini kucultuyor

#karsilama_strip=karsilama.strip()
#print(karsilama_strip)
#boşluk karakterlerini temizliyor

karsilama_split=karsilama.split()
print(karsilama_split)
#her kelimeyi tek tek karsılıyor
#['benim', 'adımnisa', 'agacciogluyasın', '16hosgeldin'] çıktısı boyle

karsilama_split=karsilama.split()
print(karsilama_split)
print(karsilama_split[5])

 
karsilama_join="-".join(karsilama)
print(karsilama_join)
#her karakterin arasına - işareti koyuyor ,- -b-e-n-i-m- -a-d-ı-m- -n-i-s-a- -a-g-a-c-c-i-o-g-l-u- -y-a-s-ı-n- -1-6- -h-o-s-g-e-l-d-i-n çıktısı boyle

karsilama_find =karsilama.find("nisa")
print(karsilama_find)
# nisanın kaçıncı karakterde başladığını buluyor

karsilama_startswith=karsilama.startswith("8")
print(karsilama_startswith)
#parantezin içine yazdığım karakterle baslayıp başlmadığını konyrol ediyor örnek parantez içine 8 yazmışım false çıktısı vermiş

karsilama_endswith=karsilama.endswith("n")
print(karsilama_endswith)
#parantezin içine yazdığım karakterle sonlanıp sonlanmadığını kontrol ediyor örnek parantez içine n yazmışım true çıktısı vermiş
 
karsilama_replace=karsilama.replace("nisa","agaccioglu")
print(karsilama_replace)
#parantez içine yazdığım şeylerin yerini dğiştiriyor, benim adım agaccioglu agaccioglu yasın 16 hosgeldin çıktısı böyle olmuş




