def fakt():
    
    sayi=int(input("Sayı:"))
    hesap=1
    if sayi==0:
        print("Faktöriyel:1")
        
    else:
        for each in range(1,sayi+1):
            hesap *=each
            
    print("Faktöriyel:",hesap)
    secim=int(input("1- Programdan çıkmak için 1 basınız"))
    if secim==1:
        print("Programdan kapatıldı!!")
    else:
        fakt()
fakt()