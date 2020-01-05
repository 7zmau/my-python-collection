import tkinter
win = tkinter.Tk()
c = tkinter.Canvas(win, height=200, width=400)
c.pack()
c.create_arc(50, 50, 200, 200, start = 0, extent=90, style = 'chord')
