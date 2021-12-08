import tkinter
from tkinter.constants import COMMAND


top = tkinter.Tk()
# Code to add widgets will go here...

def clickExitButton():
    
    exit()


w = tkinter.Button (top, text="Ex",command = clickExitButton)
w.pack()

top.mainloop()

