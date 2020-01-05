import tkinter as gui
def incrSize(event):
    i = f.cget('size')
    i = i+2
    f.configure(size=i)
    C.itemconfigure(t, font=f)
def decrSize(event):
    i = f.cget('size')
    i = i-2
    f.configure(size=i)
    C.itemconfigure(t, font=f)
win = gui.Tk()
C = gui.Canvas(win, height=500, width=500)
f = gui.font.Font(family='Times', size=13)
t = C.create_text(250,250, text="Hello world", font=f, justify="center")
C.bind()
C.focus_set()
C.bind("<Key-i>",incrSize)
C.pack()
C.bind("<Key-d>",decrSize)
C.pack()
