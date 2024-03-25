def hesaplasaate_gore_maas(saaticalisma, saatlikucret):
    if saaticalisma <= 40:
        maas = saaticalisma * saatlikucret
    else:
        normal_calisma_saati = 40
        fazlacalisma_saati = saati_calisma - 40
        maas = (normal_calisma_saati * saatlik_ucret) + (fazlacalisma_saati*saatlik_ucret*1.5)
    return maas 

def hesapla_komisyon(maas, odeme_kodu):
    if odeme_kodu == 1:
        toplam_maas = maas
    elif odeme_kodu == 2:
        toplam_maas = maas + 500
    else:
        print("Geçersiz ödeme kodu Lütfen tekrar deneyin")
        return None
    return toplam_maas

saatlik_ucret = 50
saati_calisma = int(input("Toplam çalışma saatiniz: "))
odeme_kodu = int(input("Ödeme kodunuzu giriniz\n =>1 Saatlik çalışan\n =>2: Komisyonla çalışan: "))

maas = hesaplasaate_gore_maas(saati_calisma, saatlik_ucret)
if maas is not None:
    toplam_maas = hesapla_komisyon(maas, odeme_kodu)
    if toplam_maas is not None:
        print("toplam maaşınız:", toplam_maas, "tl")

#benim yazdığım örnek
         
#soru: liste içerisinde bir şehre ait günlük ortlama sıcaklık bilgileri tutulmaktadır. günlük ortlama sıcaklk biilgileri -20 ile 40 derece arasındadır. 
#buna göre bu dziyi parametre olarak alan ve 

def sicalikaraligi(sicakliklar):
    sicaklikaralikları={
        "(-20)-(0)":0,
        "(0)-20":0,
        "(20)-(40)":0 
    }

    for sicaklik in sicakliklar:
        if -20 <= sicaklik < 0:
            sicaklikaralikları["(-20)-(0)"] +=1
        elif 0 <= sicaklik < 20:
            sicaklikaralikları["(-0)-20"] +=1
        elif 20 <= sicaklik < 40:
            sicaklikaralikları["(20)-(40)"] +=1

    for aralik,sayi in sicaklikaralikları.items():
        print(aralik,"arasında",sayi "tane sıcaklık var")
sicakliklistesi=[5,-15,25,12,2,]
sicalikaraligi(sicakliklistesi)







