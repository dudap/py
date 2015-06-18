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
        elif liczba.getLiczba()>s:
            l5.config(text="Za mala")
        else:
            messagebox.showinfo(title = "Gratulacje!!!!", message  = "Brawo Trafiles")


            main1.quit()
            main1.destroy()
    except ValueError:
        l5.config(text="Podaj liczbe")

def new_game():
    if e.get()=='' and e1.get()=='':
        l.config(text=("Wprowadz min i max"))
    else:
        liczba.setLiczba(int(e.get()),int(e1.get()))
        global main1
        main1=tkinter.Tk()
        global l5
        l5=tkinter.Label(main1,text="Wprowadz liczbe")
        b2 = tkinter.Button(main1, text = "Sprawdz", command = sprawdz)
        b5 = tkinter.Button(main1, text = "Zakoncz", command = end)
        global e2
        e2=tkinter.Entry(main1)
        l5.pack()
        e2.pack()
        b2.pack()
        b5.pack()
        main1.mainloop()
liczba=Liczba()

main=tkinter.Tk()

b=tkinter.Button(main ,text= "zakoncz" , command=end)
l=tkinter.Label(main,text="Zgadnij liczbe")
e=tkinter.Entry(main)
e1=tkinter.Entry(main)

b3 = tkinter.Button(main, text = "Nowa gra", command = new_game)

l3=tkinter.Label(main,text="Podaj min")
l1=tkinter.Label(main,text="Podaj max")

l.pack()
l3.pack()
e.pack()
l1.pack()
e1.pack()
b3.pack()
b.pack()
main=main.mainloop()

