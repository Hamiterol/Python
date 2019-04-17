#burada kütüphanenimizi dahil ediyoruz
import numpy as np
#Sonrada kullanıcıdan deger alıyoruz tabi buraya dikkat kullanıcıdan alınan deger her zaman vertipi stringtir
deger=input("Bir değer giriniz: ")
#buradada alınan degeri listeleme yapıyoruz
listeleme=np.array(deger)
#en son olarak da for döngüsüne atayarak tek tek ekrana yazdırıyoruz!!!!
for each in deger:
    print(each)