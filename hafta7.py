'''
sayilar=[10,20,30,40,50]

toplam=0
print(sayilar[0])

for sayi in sayilar:
    toplam+=sayilar
print(toplam)

meyveler=["portakal","elma","kivi"]

for meyve in meyveler:
    print(meyve)

sayilar=[1,2,7,45,4,12,77,345,86,322,]
for sayilar in sayilar:
    if sayilar%2==0:
        print(sayilar)
     '''
x=0
sayi_listesi=[]
while x<5:
    sayi=(int(input("lütfen {}. sayıyı girin:".format(x+1))))
    sayi_listesi.append(sayi)
    x+=1
    print("girdiğin sayılar:",sayi_listesi)