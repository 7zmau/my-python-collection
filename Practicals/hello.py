from tkinter import *
win = Tk()
c = Canvas(win, height=400, width=572)
c.pack()
v = IntVar()
def disp():
    val = v.get()
    c.delete('all')
    if val==1:
        c.create_oval(10,10,100,100)
    elif val==2:
        c.create_rectangle(10,10,100,100)
    elif val==3:
        c.create_polygon(30,30,60,60,90,90, fill='red',outline='black')

r1 = Radiobutton(win, text='Circle', variable=v, value=1, command=disp)
r1.pack()
r2 = Radiobutton(win, text='Rectangle', variable=v, value=2, command=disp)
r2.pack()
r3 = Radiobutton(win, text='Triangle', variable=v, value=3, command=disp)
r3.pack()
