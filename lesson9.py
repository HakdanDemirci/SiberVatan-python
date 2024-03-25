open("yenidosya.txt","w")
"w" write->yazma modu, yoksa oluşturur içeriği silip ekleme yapar
"a" Append -> ekleme modu 
"x" create -> oluşturma modu , aynısı varsa hata verir
"r" read -> okuma modu

file = open ("yenidosya.txt","w")
print(file)
file.close()

 file_dizin = open("C:/Users/USER/Desktop/a.text","w")
 file_dizin.close()
file = open ("yenidosya1.txt","w")
file.write("ADIMNİSA") 
file.close()
file=open("yenidosya1.txt","w", encoding='utf-8')
file.write("\n nisa")
file.close()

file = open ("yenidosya1.txt","w")
file.write("55555") 
file.close()
file=open("yenidosya1.txt","a", encoding='utf-8')
file.write("\n sefa")
file.close()
file = open("yenidosya2.txt","x")

try:
    file = open ("yenidosya.txt","r",encoding='utf-8')
    print(file)
except FileNotFoundError:
    print("hata")
finally:
    print("dosya kapandı")
    file.close()

for i in file:
    print(i,end="")


file = open("yenidosya.txt","r",encoding='utf-8')
icerik = file.read()
print(icerik)
icerik_karakter = file.read(0)
icerik_karakter = file.read(5)
print(icerik_karakter)
print(file.readline(),end="")
print(file.readline(),end="")

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
file.close()

with open("yenidosya.txt","r",encoding='utf-8') as file:
    content = file.read()
    print(content)
    file.seek(2)
    print(file.tell())
    content2 = file.read()
    print(content2)

with open("yenidosya.txt","r+",encoding='utf-8') as file:
    file.seek(20)
    file.write("siber vatan")

with open ("yenidosya.txt","r+",encoding='utf-8') as file:
 file.seek(0)
 file.write("samsun")

citylist=['karabük','samsun','izmir']
index = 1
with open ("a.txt","a",encoding='utf-8') as file:
    for i in citylist:
        if index == len(citylist):
            file.write(i)
        else:
            file.write(i+"\n")
        index+=1
    
import math as islem
sonuc=islem.sqrt(121)
print(sonuc)
sonuc=islem.factorial(5)
print(sonuc)

from math import *

print(factorial(5))
print(sqrt(5))
print(factorial(5))

import random 
sayilar=[0,1,2,3,4,5,6,7,8]
list=[]
i=0

while i!=6:
    list+=str(sayilar[random.randint(0,len(sayilar))])
    i+=1

print(list[0:7])

import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=""
i=0

while i!=6:
    list+=str(random.choice(sayilar))
    i+=1

print(list[0:7])

import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=[]
i=0

while i!=6:
    list.append(random.choice(sayilar))
    i+=1
print("before shuffle")
print(list)
random.shuffle(list)
print("after shuffle")
print(list)

import math
print(math.pow(6,6))

import kutuphane
sayi = kutuphane.sayimiz[2]
print(sayi)
