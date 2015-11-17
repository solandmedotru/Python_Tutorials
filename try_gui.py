from tkinter import *

def bAaction():
    print("Thanks")

def bBaction():
    print("Hello")

window = Tk()

buttonA = Button(window, text="Press me!", command=bAaction)
buttonB = Button(window, text="Dont press!", command=bBaction)

buttonA.pack()
buttonB.pack()
