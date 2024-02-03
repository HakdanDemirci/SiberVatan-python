'''
a=90
b="sibervatan"

num1,num2,num3=5,55,65
print("sayilar",num1,num2,num3)

num1=num1+50
num2=num2+55
num3=num3+90

num1*=num2

numbers=(50,55,66)
print(type(numbers))
num1,num2,num3,num4=numbers

print(num4)


a,b,c,d=50,100,50,70

sonuc=(a > b)
print(sonuc)

sonuc=(a==c)
print(sonuc)

sonuc=(a>d)
print(sonuc)

sonuc=(a!=c)
print(sonuc)

username1="cekü"
username2="arif"

username_input=input("kullanici adini gir:")

sonuc=(username1.lower()==username_input.lower())
sonuc1=(username2.lower()==username_input.lower())
sonuc2=(sonuc!=sonuc1)
print("eşleşme sonucu:",sonuc2)


users={
    "garavel.usta@gora.com.tr":"garavel123",
    "216.robot@gora.com.tr":"robot123"
}
input_mail=input("mail gir:")
input_sifre=input("şifre gir la:")

sonuc_mail=(input_mail in users.keys())
sonuc_sifre=(input_sifre in users.values())

sonuc_final=(int(sonuc_mail==sonuc_sifre))

print("eşleşme durumu:",sonuc_final)

fruits={"elma","ayva","portakaaal","çilek"}
print("kivi" in fruits)

x=y=[10,20,30]
z=[10,20,30]
print(x is y)
print(x is z)
print(x==z)

vize_not=int(input("vize notunu gir:"))
final_not=int(input("final notunu gir:"))
vize_sonuc=(vize_not*0.4)
final_sonuc=(final_not*0.6)
sınav_not=(vize_sonuc+final_sonuc)>50
sınav_not>=50
print("geçme durumu..:",sınav_not)

sayi=int(input("sayi gir lo:"))
tek_cift=(sayi>0)and(sayi%2==0)
print("tek mi çift mi..:",tek_cift)

x=98
y=23
if(x>y):
    print("x sayısı daha büyüktür",x)
elif(x==y):
    print("sayilar eşit")
else:
    print("y daha büyüktür",y)
    
kullanici_takim=input("takım adı gir la gardeş:".lower())
if kullanici_takim=="Galatasaray".lower():
    print("en sevdiğiniz renkler: sarı ve kırmızı")
elif kullanici_takim=="fenerbahçe".lower():
    print("en sevdiğiniz renkler: siyah ve beyaz")
elif kullanici_takim=="Kardemir Karabük Spor".lower():
    print("en sevdiğiniz renler:bordo ve lacivert")
else:
    print("sevdğiniz renk yok!!")
   
sifre="apocan123"
kullanici_adi="hako"

girilen_kullanici=input("kullanıcı adı gir:")
girilen_sifre=(input("şifre gir:"))

if(girilen_kullanici==kullanici_adi)and(girilen_sifre!=sifre):
    print("kullanıcı adı doğru ama şifre yanlış")

elif girilen_kullanici!=kullanici_adi and girilen_sifre==sifre:
    print("şifre doğru ancak kullanıcı adı yanlış")

elif girilen_kullanici!=kullanici_adi and girilen_sifre!=sifre:
    print("ikiside yanlış")

else:
    print("giriş başarılı")
    
sayi1=int(input("sayı gir la:"))
sayi2=int(input("2.sayıyı gir la:"))
yapilmasi_istenen_islem=input("yapılması istenen işlemi giriniz:")
if yapilmasi_istenen_islem=="çarpma":
    print(sayi1*sayi2)
elif yapilmasi_istenen_islem=="çıkarma":
    if sayi1>sayi2:
        print(sayi1-sayi2)
    else:
       print(sayi2-sayi1)
elif yapilmasi_istenen_islem==("toplama"):
    print(sayi1+sayi2)
elif yapilmasi_istenen_islem==("bölme"):
    print(sayi1/sayi2)
else:
    print("hatalı işlem")
    '''