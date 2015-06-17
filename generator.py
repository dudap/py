import random

random.seed()
def new():
    global p
    return random.randint(0,99)
p=new()
while True:
    try:

        s=int(input("Podaj liczbe: \n"))
        if s>p:
            print("Za duza")
        elif s<p:
            print("Za mala")

        else :
            print("Tak w sam raz\n")
            print ("Nowa gra ")
            p=new()

    except ValueError:
        print("To nie liczba")
