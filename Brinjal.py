class Brinjal:

    

    

    def __init__(self, noOfBrinjals):

        import tkinter as tk
        
        self._noOfBrinjals = noOfBrinjals

        def addBrinjals():
            brinjalPic = tk.PhotoImage(file="C:\\Program Files\\Python35\\eggplant-04.jpg")
            c.create_image(image=brinjalPic)
            c.pack()
            
        win = tk.Tk()
        fr1 = tk.Frame(win)
        c  = tk.Canvas(fr1, width=800, height=400)
        #c.pack()
        fr2 = tk.Frame(win)
        btn1 = tk.Button(fr2, text="Add", command=addBrinjals).pack(side="left")
        #btn2 = tk.Button(fr2, text="Clear", command=removeBrinjals).pack(side="left")
        fr1.pack()
        fr2.pack()
