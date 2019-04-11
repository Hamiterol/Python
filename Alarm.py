import time

saat=int(input("Saat:" ))
Dakika=int(input("Dakika:" ))

while True:
    lc=time.localtime(time.time())
    if saat==lc.tm_hour and Dakika==lc.tm_min:
        print ("Saat Çaldı")
        break
    else:
        pass
print("Döngüden çıkıldı")