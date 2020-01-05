from tkinter import *
def paint(event):
    if event.x > 100 and event.x < 300 and event.y > 100 and event.y < 200:
        c.itemconfigure(r, fill='red')
    else:
        c.itemconfigure(r, fill='blue')


win = Tk()
c = Canvas(win,height=600,width=800)
c.pack()
r = c.create_rectangle(100,100,300,200)
c.bind('<Motion>',paint)
