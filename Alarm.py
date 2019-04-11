import time
//Buraya dikkat kullanıcıdan alınan veriler her zaman string değerdedir, bu dolayıdır ki gelen verileri int çeviriyoruz
saat=int(input("Saat:" ))
Dakika=int(input("Dakika:" ))

while True:
    
    lc=time.localtime(time.time())#burada bilgisayarın saat ve zamanının alıyoruz
    if saat==lc.tm_hour and Dakika==lc.tm_min:#kullanıcıdan alınan deger ile pc deki degerleri kontrol ettiriyoruz
        print ("Saat Çaldı")
        break
    else:
        pass
print("Döngüden çıkıldı")
