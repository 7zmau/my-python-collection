from tkinter import *
def crtDot(event):
    x = event.x
    y = event.y
    c.create_oval(x-5,y-5,x+5,y+5, fill = 'red')

def clrDot(event):
    x = event.x
    y = event.y
    c.create_oval(x-8,y-8,x+8,y+8, fill = 'lightblue', outline = 'lightblue')
    
win = Tk()
c = Canvas(win, height=600, width=800, background='lightblue')
c.pack()
c.bind('<Button-1>', crtDot)
c.bind('<Button-3>', clrDot)
