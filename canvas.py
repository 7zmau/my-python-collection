from tkinter import *
def character(event):
    txt = 'You have pressed ' + event.char
    c.itemconfigure(t,text=txt)
win = Tk()
c = Canvas(win,height=600,width=800)
c.pack()
f = font.Font(family='Times',size=18,weight='bold')
t = c.create_text(100,100,text='Press any key',font = f)
c.focus_set()
c.bind('<Key>',character)
