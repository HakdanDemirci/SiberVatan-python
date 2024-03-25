"""
file=open("yenidosya2.txt","w",encoding="utf-8") #buraya utf-8 kodunu ekleyerek farklı yazı tiplerini eklemeyi sağlıyoruz
file.write("Nisanur Ağaçcıoğlu") #dosyanın içine bişeyler eklemek için bu komutu kullanıyoruz
#file.close()

import os
os.getcwd()
'D:\\calisma\\python'
os.getcwdb()
b'D:\\calisma\\python'

import os
print(os.getcwd())
"""

import os
gecerli_dizin= os.getcwd()
print(gecerli_dizin)

for i in os.listdir(gecerli_dizin):
    print(i)

new_directory= os.path.join(gecerli_dizin,"yeni dizin"):
os.mkdir(new_directory)
print(f"{new_directory}oluştu")

os.chdir(new_directory)
print(f"{new_directory}dizinine gidildi.")

dosya_yolu= os.path.join(new_directory,"example.txt")
with open(dosya_yolu,"w",encoding="utf-8") as file:
    file.write("hellö wörld")

os.remowe("example.txt")

os.chidr(gecerli_dizin)

os.rmdir("yeni_dizin")
print("actiğim dizini sildim")




 
