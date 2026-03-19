def asal_mı(sayı):

    if (sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):


            if(sayı % i == 0):
                return False
        return True

while True:

    sayı=input("sayı:")

    if(sayı=="q"):
        print("program sonlandırılıyor...")

        break

    else:
        sayı=int(sayı)

        if(asal_mı(sayı)):
            print(sayı,"Asal Sayıdır.")

        else:
            print(sayı,"Asal Sayı Değildir.")





