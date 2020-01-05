from tkinter import *
win = Tk()
c = Canvas(win, height = 500, width = 500)
c.create_text(250, 250, text = 'Hello World')
c.pack()
