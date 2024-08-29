from random import randint

can = 3

sayi = randint(1,10)
while True:
    tahmin = int(input("Enter the 0-10 numbers :"))

    if sayi == tahmin:
        print("Doğru!!!")
        print("Canınız :",can)
        break
    else:
        print("Tekrar Deneyiniz")
        can = can - 1
        print(f"Canınız : {can}")

    if can == 0:
        print("Kaybettiniz...")
        print("Sayı : ", sayi)
        break