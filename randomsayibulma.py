from random  import randint
def oyun():
    print("3 adımda sayı bilme oyunu")
    sayi=int(input("Lütfen bir sayı giriniz: ")) 
    say=randint(0, 10)
    sayac=0
    if sayi<0 & sayi>10:
            print("0-10 arasında bir değer giriniz...")
    else:
        for döngü in range(0,3):
            if sayi==say:
                print("Tebrikler Sayıyı bildiniz.Sayı:",say)
                break
            else:
                sayac+=1
                if sayac==3:
                    print("Bilemediniz ve Oyun bitti Sayı:",say)
                    break
                else:
                    sayi=int(input("Lütfen bir sayı giriniz: ")) 
    secim=int(input("2- Oyundan çıkmak çikmak için 2 ye basınız"))
    if secim==2:
       print("Oyundan çıkış yapıldı!!!")
    else:
        oyun()
oyun()
   

    