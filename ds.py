import tkinter
win = tkinter.Tk()
fr1 = tkinter.Frame(win,)
fr2 = tkinter.Frame(win,)

def Add():
    rs = int(e1.get())
    cr = float(e2.get())
    dl = rs * cr
    ans.config(text = "Amount in rupees:" + str(dl))
numberOne = tkinter.Label(fr1, text="Amount in dollars",).grid(row = 0, column = 0)
e1 = tkinter.Entry(fr1,)
e1.grid(row = 0, column = 1)
#a = e1.bind("<Return>", getA)
numberTwo = tkinter.Label(fr1, text="Conversion Rate:",).grid(row = 1, column = 0)
e2 = tkinter.Entry(fr1,)
e2.grid(row = 1, column = 1)
#e2.bind("<Return>", Add)
fr1.pack()
ans = tkinter.Label(fr2, text="", height=1)
ans.pack()
btn1 = tkinter.Button(fr2, text="Pata Laga", command=Add)
btn1.pack()
fr2.pack()
