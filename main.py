import random
from liste import kelimeler

def oyna():
    kelime = kelimeler[random.randint(1,len(kelimeler))]
    uzunluk = len(kelime)
    #print(kelime)
  
    bosluk = kelime.count(' ')
    kelimesayi = bosluk +1

    kullanilanHarfler = []

    hak = (uzunluk-bosluk) *2
    kelime2 = [*uzunluk*"-"]

    ##bosluk gelen yerler
    bosluklar = []
    i=0
    while i!=uzunluk:
        if kelime[i]==' ':
            bosluklar.append(str(i))
        i+=1
    #print(bosluklar)

    i=0
    j=0

    if bosluk !=0:
        while i!=uzunluk-1:
            if j<=len(bosluklar)-1:
                if str(i) == bosluklar[j]:
                    kelime2[i]=' '
                    j+=1
            else:
                break
            i+=1
            
            
    ## kazanma kaybetme kontrolü  
    bilinenHarf =0          
    while hak>0 and str(kelime2).find('-')!=-1:
        print("daha önce kullanılan harfler: "+str(kullanilanHarfler))
        print(str(kelime2)+" {} harf {} kelime {} hak".format(uzunluk-bosluk-bilinenHarf,kelimesayi,hak))

            ##tahmin yapma kısmı
        tahmin = input("tahminde bulunun: ")
        if len(tahmin)>1 and tahmin ==kelime:
            break
        hak-=1
        

        if str(kullanilanHarfler).find(tahmin)!=-1:
            print("bu harfi daha önce kullandınız. tekrar deneyin.")
        
        else:
            kullanilanHarfler.append(tahmin) 

        if(kelime.find(tahmin)==-1):
            print("hatalı deneme lütfen tekrar deneyiniz.")
        else:
            print("bir harf tahmin ettiniz!")
            bilinenHarf+=1
            bilinen = []
            i=0
            while i!=uzunluk:
                if kelime[i]==tahmin:
                    bilinen.append(str(i))
                i+=1        
            i=0
            j=0
          
            while i!=uzunluk:
                if j<=len(bilinen)-1:
                    if str(i) == bilinen[j]:
                        kelime2[i]=tahmin
                        j+=1
                else:
                    break
                i+=1  
          

    if hak == 0 :
        if str(kelime2).find('-')!=-1:
            print("kazandınız.")
            print("kelime: {}".format(kelime))
        else:
            print("kaybettiniz.")
            print("kelime: {}".format(kelime))
    else:
        print("kazandınız.")
oyna()