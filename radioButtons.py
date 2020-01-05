import tkinter as gui
def disp():
    val = v.get()
    c.delete('all')
    if val==1:
        c.create_oval(100,100,400,400)
    if val==2:
        c.create_rectangle(100,100,400,300)
    if val==3:
        c.create_polygon(250,50,100,350,400,350, fill='', outline='black')
win = gui.Tk()
c = gui.Canvas(win, height=500, width=500)
c.pack()
v = gui.IntVar()
r1 = gui.Radiobutton(win, text='Circle', variable=v, value=1, command=disp)
r1.pack()
r1 = gui.Radiobutton(win, text='Rectangle', variable=v, value=2, command=disp)
r1.pack()
r1 = gui.Radiobutton(win, text='Traingle', variable=v, value=3, command=disp)
r1.pack()
