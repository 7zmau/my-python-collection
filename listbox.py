from tkinter import *
win = Tk()
sb = Scrollbar(win, orient='horizontal')
sb.pack(side=RIGHT, fill=Y)
listvar = StringVar(value='C++ Java Python PHP Javascript')
lb = Listbox(win, listvariable=listvar, height=3, yscrollcommand=sb.set)
lb.pack()
