#FONKSİYONLAR# PHAYTONDA DEF 

def selamdunya():
    print("hello world")

selamdunya()
#fonksiyonun içindeki ile dışındaki aynı olmak zorunda değil
#kenardaki çizgi fonksiyonun içindekileri yani çalışcak olanları belirtir

def hosgeldin(name):
    print("hoşgeldin " + name)
hosgeldin("nisa")
#kendimiz direkt isim tanımlıyoruz

input_name=input("adınızı giriniz :")
#burda kullanıcıda isim alıyoruz
def hosgeldin(input_name):
    print("hoşgeldin " + input_name)
hosgeldin(input_name)


def hosgeldin(name):
     print("hosgeldin "+name)
name=input("isim giriniz:")

hosgeldin(name)


def fonksiyon(sehir= "konya"):
    print("en sevdiğim şehir "+sehir)

fonksiyon("istanbul")
#istanbul değerini gönderdğimiz için en sevdiğim şehir istanbul çıktısının alırız
fonksiyon()
#burdada değer göndermediğimiz için en sevdiğim şehir konya çıktısını alırız

#örnek
def sayi(x):
    x=x+5
    return x

sonuc =sayi(10)
print(sonuc)
#sonuc değerinin içine 10 eklicek sonuç 15 olucak

def sayi(x,y):
    z=x+y
    return z
sonuc=sayi(5,6)
print(sonuc)
#iki parametreyi toplama fonksiyonu

def topla(num1,num2):
    toplam= num1+num2
    return toplam

sonuc=topla(10,50)
print(sonuc)
#yukardakiyle aynı çalışıyo /çalışmadı tekrar bak

def fonk_tuple(*argv):
    for arg in argv:
        print(arg)

fonk_tuple("selam", "naber", "naılsın", "iyidir")


#kullanıcıdan sayı alınıp o sayıya kadar olan çift sayıları fonksiyon içinde bulup bir listeye ekleyin ve listeyi yazdırın
#append range ve list kullanılıcak 
#örnek:
#sayı girniz:8
#output: çift sayılar (0,2,4,8)

def ciftSayi(n):
    ciftsayi_list=[]
    for i in range(0,n+1):
        if i % 2 == 0:
            ciftsayi_list.append(i)
    return ciftsayi_list

limit= int(input("bir üst sınır giriniz: "))
print("çift sayilar", ciftSayi(limit))

"""
#fonksiyonlarla hesap makinesi yapımı
def toplama(num1,num2):
    return num1+num2

def çıkarma(num1,num2):
    return num1-num2

def çarpma (num1,num2):
    return num1*num2

def bolme (num1,num2):
    if num1==0:
        print("tanımsız işlem")
        return 0
    else:
        return num1/num2
    
def faktöriyel(num1):
    return 
    
#fonksiyon tanımlamaları perogramın en üstüne yapılır

devam=True
while (devam):

    print("toplama icin 1")
    print("cikarma icin 2")
    print("carpma icin 3")
    print("bölme icin 4")
    print("faktöriyel icin 5")
    print("çıkmak icin 6'yi tuşlayınız")
    
    secim=int(input("lütfen tercihte bulununuz"))
    num1= int(input("1.sayıyı giriniz"))
    num2= int(input("2.sayıyı giriniz"))

   

    if secim==1:
        sonuc=toplama(num1,num2)

    elif secim==2:
        sonuc=çıkarma(num1,num2)

    elif secim==3:
        sonuc=çarpma(num1,num2)

    elif secim==4:
        sonuc=bolme(num2,num2)

    elif secim==5:
        devam=False

    elif secenek==6:
        sonuc=faktöriyel(num1)

#bunlar çalışmayan kodlar
"""


def toplam(num1,num2):
    return num1+num2
def çıkarma(num1,num2):
    return num1-num2
def çarpma(num1,num2):
    return num1*num2
def bölme(num1,num2):
    if num2==0:
        print("tanımsız")
        return 0
    else:
        return num1/num2
def faktöriyel(num1):
    if num1==0:
        return 1
    else:
        return num1*faktöriyel(num1-1)
devam_etsinmi=True
while (devam_etsinmi):
    print("-*-*-*-*-*-*hosgeldiniz-*-*-*-*-*-*-*")
    print("toplama için 1")
    print("çıkarma için 2")
    print("çarpma için 3")
    print("bölme için 4")
    print("çıkmak için 5")
    print("faktöriyel için 6")
    secenek=int(input("secenegin ne:"))
    num1=int(input("sayı gir"))
    num2=int(input("sayı2 gir"))
    sonuc=0
    if secenek==1:
        sonuc=toplam(num1,num2)
    elif secenek==2:
        sonuc=çıkarma(num1,num2)
    elif secenek==3:
        sonuc=çarpma(num1,num2)
    elif secenek==4:
        sonuc=bölme(num1,num2)
    elif secenek==5:
        devam_etsinmi=False
    elif secenek==6:
        sonuc=faktöriyel(num1)
    else:
        print("geçerli sayı giriniz")

    print(sonuc)
