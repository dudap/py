import random
import sys
class Liczba:
    def __init__(self,ma,mi):
        self._ma=ma
        self._mi=mi

    def getLiczba(self):

         return self._liczba
    def setLiczba(self):
         self._liczba=random.randint(self._mi,self._ma)



random.seed()
try:
    a=int(input("Podaj minimalna wartosc(Brak liczby konczy gre)\n"))
    b=int(input("Podaj maxymalna wartosc(Brak liczby konczy gre)\n"))
    c=Liczba(b,a)
    c.setLiczba()
    while True:
        try:
            s=int(input("Podaj liczbe(Brak liczby konczy gre)\n"))
            if int(c.getLiczba())<s:
                print("Za duza")
            elif c.getLiczba()>s:
                print("Za mala")
            else:
                print ("Trafiles\n")

                a=int(input("Podaj minimalna wartosc(Brak liczby konczy gre)\n"))
                b=int(input("Podaj maxymalna wartosc(Brak liczby konczy gre)\n"))
                c=Liczba(b,a)
                c.setLiczba()
                print("Wygenerowalem nowa wartosc")
        except ValueError:
            print("Zakonczyles")
            sys.exit()
except ValueError:
            print("Zakonczyles")
            sys.exit()