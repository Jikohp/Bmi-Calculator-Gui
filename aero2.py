from tkinter import *
import tkinter
from tkinter import messagebox
from lib2to3.fixer_util import Number
top = tkinter.Tk()

L1 = Label(top, text="Height in meters")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = LEFT)
L2 = Label(top, text="Weight in kg")
L2.pack( side = LEFT)
E2 = Entry(top, bd =5)

E2.pack(side = LEFT)

def helloCallBack():
    print("E1.get()"+E1.get())
    print("E2.get()"+E2.get())
    a = float(E1.get())
    b = float(E2.get())
    answer = b/(a*a)
    #messagebox.showinfo( “Hello Python”, “Hello World”)
    '''
    Below 18.5	Underweight
    18.5 - 24.9	Normal
    25 - 29.9	Overweight
    30.0 +	Obese
    '''
    print("answer"+str(answer))
    E3.insert(0, answer)
    answe=int(answer)
    if answe< 18.5:
        answer="Underweight"
    if answe<24.9 and answe>18.5:
        answer="Normal"
    if 25<answe and answe<29.9:
        answer="Overweight"
    if answe>30:
        answer="Obese"
    E4.insert(0, answer)

B = tkinter.Button(text ="Calculate ", command = helloCallBack)

B.pack(side = LEFT)

L3 = Label(top, text="Bmi ")
L3.pack( side = LEFT)
E3 = Entry(top, bd =5)

E3.pack(side = LEFT)
L4 = Label(top, text="How is Bmi Level")
L4.pack( side = LEFT)
E4 = Entry(top, bd =5)

E4.pack(side = LEFT)
top.mainloop()

 