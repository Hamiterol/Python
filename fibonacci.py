a=0
b=1
sayi=int(input("bir sayı giriniz:"))
for each in range(0,sayi):
    c=a+b
    a=b
    b=c
    print("fibonacci :",b)