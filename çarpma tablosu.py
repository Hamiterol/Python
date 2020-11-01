# =============================================================================
# say=input("Bir sayı giriniz:")
# sayi=int(say)
# sayılar = [0,1,2,3,4,5,6,7,8,9,10]
# 
# for sayma in sayılar:
#     print(sayma,"*",sayi,"=",sayma * sayi)
#     
# =============================================================================

def carpma_tablosu():
    
    a=1
    b=1
    for x in range(0,10):
        for b in range(1,11):
            print(a,"*",b,"=",a*b)
            if b==10:
                print("-----------------------------------------")   
                a+=1
carpma_tablosu()  