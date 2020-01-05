from tkinter import *
def redChange():
    lbl.configure(fg='red')

def greenChange():
    lbl.configure(fg='green')

win = Tk()
c = Canvas(win, height=500, width=500)
c.create_text(100, 100, text='Hello World')
c.pack()
lbl = Label(win, text='Hello World',)
lbl.pack()
btn1 = Button(win, text='RED', command=redChange)
btn1.pack()
btn2 = Button(win, text='GREEN', command=greenChange)
btn2.pack()
