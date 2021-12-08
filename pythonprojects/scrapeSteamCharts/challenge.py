import tkinter, tkinter.messagebox
from tkinter.constants import COMMAND


top = tkinter.Tk()
# Code to add widgets will go here...

def clickExitButton():
    
    exit()
def clickIButton():
    tkinter.messagebox.showinfo(title=None, message="Hello World!")

x = tkinter.Button(top, text="Exit",command = clickExitButton)


i = tkinter.Button(top, text="info", command = clickIButton)

i.pack()
x.pack()

top.mainloop()

