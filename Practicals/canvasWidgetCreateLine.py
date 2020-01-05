from tkinter import *
win = Tk()
c = Canvas(win,height=600,width=800)
c.pack()
c.create_line(400,150,300,500)
c.create_line(400,150,500,500)
c.create_oval(300,450,500,550)
