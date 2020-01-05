from tkinter import *
def disp():
    u = e1.get()
    p = e2.get()
    string = "Username: " + u + "\nPassword: " + p
    lbl.configure(text=string)
win = Tk()
fr1 = Frame(win)
fr1.pack()
Label(fr1, text='Username:', expand=YES).pack(side=LEFT, padx=10, pady=5)
e1 = Entry(fr1)
e1.pack(side=LEFT)
fr2 = Frame(win)
fr2.pack()
Label(fr2, text='Password:', expand=YES).pack(side=LEFT, padx=10, pady=5)
e2 = Entry(fr2, show='*', expand=YES)
e2.pack(side=LEFT)
btn = Button(win, text='Login', command=disp, expand=YES)
btn.pack(ipadx=5,ipady=5)
lbl = Label(win, expand=YES)
lbl.pack()

