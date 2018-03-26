# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 09:58:55 2018

@author: omeralmaci
"""
##  MATH KÜTÜPHANESİNİN KAREKÖK FONKSİYONUNU DAHİL ETMEK
from math import sqrt
# Değişkenler
ogrenci = 0;deger = 0;matris = [];s=0 # liste degiskenleri
vizeort=0;vizesapma=0;vizekare=0 # vize degiskenleri
finalkare=0;finalsapma=0;finalort=0 # final degiskenleri
v_agirlik=0;f_agirlik=0 # agirlik degiskenleri
agirlikfark=0;agirlikkare=0;agirliksapma=0;agirlikort=0 # agirlik ortalama degiskenleri 

#GİRİŞ YAZISI

print("    #############################")
print("    #            SDÜ            #")
print("    #  Mekatronik Mühendisliği  #")
print("    # Python-Görsel Programlama #")
print("    #         1522709001        #")
print("    #     Ömer Faruk ALMACI     #")
print("    #                           #")
print("    #    Öğrenci Not Sistemi    #")    
print("    #       Versiyon :1.0       #")
print("    #############################")
#PROGRAM BAŞLANGICI
ogrenci = int(input("Lütfen not girişi yapılacak öğrenci sayısını giriniz : "))
deger = 4 # öğrenciadı-vizenotu-finalnotu-agırlıkortalaması
v_agirlik = float(input("Vize ağırlık oranını giriniz(%40 için - > 40) : "))
while(v_agirlik >= 100):
    print("Lütfen vize ağırlık oranlarını gözden geçiriniz.")
    v_agirlik = float(input("Vize ağırlık oranını giriniz(%40 için - > 40) : "))
v_agirlik = v_agirlik/100
f_agirlik = float(input("Final ağırlık oranını giriniz(%60 için -> 60) : "))
while(f_agirlik>=100):
    print("Lütfen final ağırlık oranlarını gözden geçiriniz.")
    f_agirlik = float(input("Final ağırlık oranını giriniz(%60 için -> 60) : "))
while(f_agirlik+v_agirlik>100):
    print("Lütfen vize+final ağırlık toplamlarının 100 olmasına dikkat ediniz.")
    v_agirlik = float(input("Vize ağırlık oranını giriniz(%40 için - > 40) : "))
    f_agirlik = float(input("Final ağırlık oranını giriniz(%60 için -> 60) : "))
f_agirlik = f_agirlik/100
#############SUTUNLARI SATIRLARA AYARLAMA
for i in range(ogrenci):
    matris += [[0] *deger]
######## VERİ GİRİŞ EKRANI   
for i in range(ogrenci):           
    for j in range(deger):
        if(j==0):
            sayi = int(input("%s . öğrencinin numarasını giriniz : " %(i+1)))
        if(j==1):
            sayi = int(input("%s numaralı öğrencinin vize notunu giriniz : " %(matris[i][0])))
            while(sayi <-2 or sayi >100):
                print("Lütfen vize notunu doğru giriniz!")
                sayi = int(input("%s numaralı öğrencinin vize notunu giriniz : " %(matris[i][0]))) 
        if(j==2):
            sayi = int(input("%s numaralı öğrencinin final notunu giriniz : " %(matris[i][0])))
            while(sayi<-2 or sayi>100):
                print("Lütfen final notunu doğru giriniz!")
                sayi = int(input("%s numaralı öğrencinin final notunu giriniz : " %(matris[i][0])))
        matris[i][j] = sayi
####TABLO EKRANI
print("")
print("\033[4mÖğrenci No   |  Vize  |  Final | Ortalama |  Harf  |\033[0m") 
##### AĞIRLIK ORTALAMASI HESABI
for i in range(ogrenci):
    matris[i][3]=round(((matris[i][1]*v_agirlik)+(matris[i][2]*f_agirlik)),3)
    vizeort=vizeort+matris[i][1]
    finalort=finalort+matris[i][2]
    agirlikort=agirlikort+matris[i][3]
    s=s+1
    
finalort=finalort/s
vizeort=vizeort/s
agirlikort=agirlikort/s

# VİZE İÇİN STANDART SAPMA HESABI
for i in range(ogrenci):
    vizefark=abs(matris[i][1]-vizeort)
    vizekare= vizekare + vizefark*vizefark
    vizefark=0
vizekare=vizekare/(s-1)
vizesapma=round(sqrt(vizekare),3)
  
# FİNAL İÇİN STANDART SAPMA HESABI
for i in range(ogrenci):
    finalfark=abs(matris[i][2]-finalort) # mutlak alma
    finalkare=finalkare + finalfark*finalfark
    finalfark=0
finalkare=finalkare/(s-1)
finalsapma=round(sqrt(finalkare),3) # virgülden sonra kaç basamak görünsün

# AĞIRLIK ORTALAMA İÇİN SAPMA HESABI
for i in range(ogrenci):
    agirlikfark=abs(matris[i][3]-agirlikort)
    agirlikkare=agirlikkare + agirlikfark*agirlikfark # karesi
    agirlikfark=0
agirlikkare=agirlikkare/(s-1)
agirliksapma=sqrt(agirlikkare) # karekök alma

# VERİLERİ BASMA
for i in range(ogrenci):           
    for j in range(deger):
        # | boşlukları ayarla!
        if(1 == (matris[i][j]/100)): 
            print (matris[i][j],end="  |   ",flush=False)
        elif(1<= (matris[i][j]/10) <10):
            print (matris[i][j],end="   |   ",flush=False)
        elif(0<= (matris[i][j]) <10):
            print (matris[i][j],end="    |   ",flush=False)
        else:
            print (matris[i][j],end="   |   ",flush=False)
    if(matris[i][3]<agirlikort-3*agirliksapma):
        print("FF   |")
    if(agirlikort-3*agirliksapma<matris[i][3]<agirlikort-2*agirliksapma):
        print("FD   |")
    if(agirlikort-2*agirliksapma<matris[i][3]<agirlikort-agirliksapma):
        print("DD   |")
    if(agirlikort-agirliksapma<matris[i][3]<agirlikort):
        print("DC   |")
    if(agirlikort+agirliksapma>matris[i][3]>agirlikort):
        print("CC   |")
    if(agirlikort+2*agirliksapma>matris[i][3]>agirlikort+agirliksapma):
        print("CB   |")
    if(agirlikort+3*agirliksapma>matris[i][3]>agirlikort+2*agirliksapma):
        print("BB   |")
    if(agirlikort+4*agirliksapma>matris[i][3]>agirlikort+3*agirliksapma):
        print("BA   |")
    if(matris[i][3]>agirlikort+4*agirliksapma):
        print("AA   |")
## HESAPLAMALARI VİRGÜLDEN SONRA 3 BASAMAK OLARAK AYARLAMA
agirliksapma=round(agirliksapma,3)
agirlikort=round(agirlikort,3)        
finalort=round(finalort,3)
vizeort=round(vizeort,3)
## ORTALAMALAR VE SAPMALARI BASMA
print("____________________________________________________")    
print("\nVize Ortalaması : %s \nVize Sapması    : %s \nFinal Ortalaması: %s \nFinal Sapması   : %s \nÇan Ortalaması  : %s   \nÇan Sapması     : %s" %(vizeort,vizesapma,finalort,finalsapma,agirlikort,agirliksapma))    
