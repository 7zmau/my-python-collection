import tkinter
"""def getA():
    return entryOne.get()
def getB():
    return entryTwo.get()"""
def Add():
    a = int(e1.get())
    b = int(e2.get())
    s = a + b
    ans.config(text="Sum is " + str(s))
def Subtract():
    a = int(e1.get())
    b = int(e2.get())
    s = a - b
    ans.config(text="Difference is " + str(s))
def Multiply():
    a = int(e1.get())
    b = int(e2.get())
    s = a * b
    ans.config(text="Product is " + str(s))

win = tkinter.Tk()
fr1 = tkinter.Frame(win,)
fr2 = tkinter.Frame(win,)

numberOne = tkinter.Label(fr1, text="Enter Number",).grid(row = 0, column = 0)
e1 = tkinter.Entry(fr1,)
e1.grid(row = 0, column = 1)
#a = e1.bind("<Return>", getA)
numberTwo = tkinter.Label(fr1, text="Enter Number",).grid(row = 1, column = 0)
e2 = tkinter.Entry(fr1,)
e2.grid(row = 1, column = 1)
#e2.bind("<Return>", Add)
fr1.pack()
ans = tkinter.Label(fr2, text="", height=1)
ans.pack()
btn1 = tkinter.Button(fr2, text="Add", command=Add)
btn1.pack(side="left")
btn2 = tkinter.Button(fr2, text="Subtract", command=Subtract)
btn2.pack(side="left")
btn3 = tkinter.Button(fr2, text="Multiply", command=Multiply)
btn3.pack(side="left")
fr2.pack()
e1.focus_set()
