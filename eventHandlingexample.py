import tkinter
def paint1(event):
    c.configure(bg = 'green')
def paint2(event):
    c.configure(bg = 'blue')
    
win = tkinter.Tk()
c = tkinter.Canvas(win, height = 500, width = 700)
c.pack()
c.bind('<Enter>', paint1)
c.bind('<Leave>', paint2)
