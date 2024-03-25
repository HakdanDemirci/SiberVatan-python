#gecenki hesap makinesindeki faktöriyel fomksiyonu
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n* faktoriyel(n-1)
sayi=4
print(faktoriyel(sayi))

#rekarsif fonksiyon soru tipi klasık faktoriyel


#ERROR HANDLİNG BUGÜNÜN KONUSU
x="global değişken"
#buna bir yazdıma işlemi yapmadığımız için ilk basta local sonra global değişken yazdırır ekrana
def function():
    x="local degişken"
    print(x)
function()
print(x)

#print(a)
#NameError: name 'a' is not defined =bu hatayı veriyor cumku a tanımlı değil

#int("a19")
#ValueError: invalid literal for int() with base 10: 'a19' =olmicak bir şeyin içine olmicak bir hata yapmışız gibi düşünebiliriz kadir hoca öyle dedi

#print(10/0)
#ZeroDivisionError: division by zero = sıfıra bolunme hatası

#print("hello" world)
#SyntaxError: invalid syntax. Perhaps you forgot a comma?= yazım hatası oldugunu bildirir
"""
While True:
    try:
        x=int(input("x giriniz: "))
        y=int(input("y giriniz: "))
        print(x/y)
    #except ZeroDivisionError:
        #print("sıfıra bölünme hatası")
    #except ValueError:
        #print("x ve y için sayısal deger giriniz:")
    except Exception as ex:
        print("bilgiler yanlış",ex)
    else:
        break
    finally:
        print("her sey yolunda") #hatalı kod var
"""
while True:
    try:
        x=int(input("x gir:"))
        y=int(input("y gir:"))
        print(x/y)
    except Exception as ex:
        print("bilgiler yanlis",ex)
    else:
        break
    finally:
        print("her sey yolunda")

"""
try:
    x=int(input("x giriniz: "))
    y=int(input("y giriniz: "))
    print(x/y)
except ZeroDivisionError as ex:
    print("sıfıra bölünme hatası")
else:
    break
finally:
    print("her sey yolunda") 

try:
    x=int(input("x giriniz: "))
    y=int(input("y giriniz: "))
    print(x/y)
except ValueError as ex:
    print("x ve y için sayısal deger giriniz")
else:
    break
finally:
    print("her sey yolunda") #hatalı kodlar var
"""
while True:
    try:
        x=int(input("x gir:"))
        y=int(input("y gir:"))
        print(x/y)
    except Exception as ex:
        print("bilgiler yanlis",ex)
    else:
        break
    finally:
        print("her sey yolunda")


try:
        x=int(input("x gir:"))
        y=int(input("y gir:"))
        print(x/y)
except ZeroDivisionError:
        print("sıfıra bölnme hatası")


import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("parola en az 8 karakter")
    elif not re.search("[a-z]",parola):
        raise Exception("parola kucuk harf icermelidir.")
    elif not re.search ("[A-Z]",parola):
        raise Exception("Parola buyuk harf icermelidir")
    
password="12345678aZ@"
try:
    parola_kontrol(password)
except Exception as ex:
    print(ex)
else:
    print("parola oluşturma başsarılı")

#regular expression kutuphanesine bak ödev
#ve özel karakter eklenebilir yap ödev



