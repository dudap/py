import random
import sys
import tkinter
from tkinter import messagebox

class Liczba:
    def __init__(self):
        pass
    def getLiczba(self):

         return self._liczba
    def setLiczba(self,f,s):
         self._liczba=random.randint(f,s)

def end():
    sys.exit()
def sprawdz():


    try:
        s=int(e2.get())

        if int(liczba.getLiczba()<s):
            l5.config(text="Za duza")

            l6.config(text=str(licz(1)))
        elif liczba.getLiczba()>s:
            l5.config(text="Za mala")
            l6.config(text=str(licz(1)))

        else:
            messagebox.showinfo(title = "Gratulacje!!!!", message  = "Brawo Trafiles\n Twoja liczba prob wynosi ="+str(licz(1)))


            main1.quit()
            main1.destroy()
    except ValueError:
        l5.config(text="Podaj liczbe")
def licz(i):
    global j
    if i==0:
        j=0
    else:
        j=j+1
        return j
def quit():
    main1.quit()
    main1.destroy()
def new_game():
    if e.get()=='' or e1.get()=='' or not e.get().isdigit() or not e1.get().isdigit() :
        l.config(text=("Wprowadz min i max"))
    else:
        liczba.setLiczba(int(e.get()),int(e1.get()))
        global main1
        licz(0)
        main1=tkinter.Tk()
        global l5
        l5=tkinter.Label(main1,text="Wprowadz liczbe")
        b2 = tkinter.Button(main1, text = "Sprawdz", command = sprawdz)
        b5 = tkinter.Button(main1, text = "Zakoncz", command = quit)
        global e2
        e2=tkinter.Entry(main1)
        global l6
        l6=tkinter.Label(main1, text="Liczba pro="+str(0))
        l5.pack()
        e2.pack()
        b2.pack()
        b5.pack()
        l6.pack()
        main1.mainloop()
def help():
    messagebox.showinfo(title = "OPIS", message  = "\
                              Zgadnij jaka to liczba\n\n\
W polach min i max wpisujemy liczby bedace koncami przedzialu\n\
w postaci <min,max> a nastepnie zgadujemy wylosowana przez komputer liczbe")
liczba=Liczba()
random.seed()
main=tkinter.Tk()

b=tkinter.Button(main ,text= "zakoncz" , command=end)
l=tkinter.Label(main,text="Zgadnij liczbe")
e=tkinter.Entry(main)
e1=tkinter.Entry(main)
b9=tkinter.Button(main,text="Opis",command=help)
b3 = tkinter.Button(main, text = "Nowa gra", command = new_game)
l3=tkinter.Label(main,text="Podaj min")
l1=tkinter.Label(main,text="Podaj max")

l.pack()
l3.pack()
e.pack()
l1.pack()
e1.pack()
b3.pack()
b9.pack()
b.pack()
main=main.mainloop()

