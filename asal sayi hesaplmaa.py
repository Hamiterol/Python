say=input("Bir sayı giriniz:")

sayi=int(say)


if (sayi==2 ):
    print("Girdiğiniz sayi hem asaldır hemde çift sayıdır",sayi)
elif(sayi%2==0):
    print("Girilen sayı asal sayı değildir:",sayi)
else:
    print("Girdiğiniz sayı asaldır:",sayi)
