from tkinter import *

root = Tk()

top = Frame()
bottom = Frame()
top.grid(column=1, row=1)
bottom.grid(column=1, row=2)

entry = Entry(top)
entry.grid(row=1, column=1)
entry2 = Label(top, text="0")
entry2.grid(row=2, column=1)

class Calculate:
    num1 = ""
    num2 = ""
    calc = ""
    ans = ""
    def getFirstNumber(self, sign):
        if self.ans == "":
            self.num1 = entry.get()
            entry2.config(text=sign+" "+self.num1)
            entry.delete(0, END)
        else:
            self.num1 = self.ans
            entry2.config(text=sign + " " + self.num1)
            entry.delete(0, END)
    def minus(self):
        self.getFirstNumber(Calculate, "-")
        self.calc = "minus"
    def plus(self):
        self.getFirstNumber(Calculate, "+")
        self.calc = "plus"
    def divide(self):
        self.getFirstNumber(Calculate, "÷")
        self.calc = "divide"
    def multiply(self):
        self.getFirstNumber(Calculate, "x")
        self.calc = "multiply"
    def modulo(self):
        self.getFirstNumber(Calculate, "modulo")
        self.calc = "modulo"
    def calculate(self):
        self.num2 = entry.get()
        entry.delete(0, END)
        if self.calc == "minus":
            self.ans =  str(round(float(self.num1) - float(self.num2), 2))
        if self.calc == "plus":
            self.ans =  str(round(float(self.num1) + float(self.num2), 2))
        if self.calc == "divide":
            self.ans =  str(round(float(self.num1) / float(self.num2), 2))
        if self.calc == "multiply":
            self.ans =  str(round(float(self.num1) * float(self.num2), 2))
        if self.calc == "modulo":
            self.ans =  str(round(float(self.num1) % float(self.num2), 2))
        entry2.config(text=self.ans)
        entry.delete(0, END)
        self.num1 = ""
        self.num2 = ""
        self.calc = ""

    def cancel(self):
        entry.delete(0, END)
        self.num1 = ""
        self.num2 = ""
        self.calc = ""
        entry2.config(text="0")

press1 = Button(bottom, text="1", command=lambda: entry.insert(END, "1"), width=3)
press1.grid(row=1, column=1)
press2 = Button(bottom, text="2", command=lambda: entry.insert(END, "2"), width=3)
press2.grid(row=1, column=2)
press3 = Button(bottom, text="3", command=lambda: entry.insert(END, "3"), width=3)
press3.grid(row=1, column=3)
press4 = Button(bottom, text="4", command=lambda: entry.insert(END, "4"), width=3)
press4.grid(row=2, column=1)
press5 = Button(bottom, text="5", command=lambda: entry.insert(END, "5"), width=3)
press5.grid(row=2, column=2)
press6 = Button(bottom, text="6", command=lambda: entry.insert(END, "6"), width=3)
press6.grid(row=2, column=3)
press7 = Button(bottom, text="7", command=lambda: entry.insert(END, "7"), width=3)
press7.grid(row=3, column=1)
press8 = Button(bottom, text="8", command=lambda: entry.insert(END, "8"), width=3)
press8.grid(row=3, column=2)
press9 = Button(bottom, text="9", command=lambda: entry.insert(END, "9"), width=3)
press9.grid(row=3, column=3)
press0 = Button(bottom, text="0", command=lambda: entry.insert(END, "0"), width=3)
press0.grid(row=4, column=2)
pressMinus = Button(bottom, text="-", command=lambda: Calculate.minus(Calculate), width=3)
pressMinus.grid(row=1, column=4)
pressCalc = Button(bottom, text="Enter", command=lambda: Calculate.calculate(Calculate))
pressCalc.grid(row=5, column=4)
pressPlus = Button(bottom, text="+", command=lambda: Calculate.plus(Calculate), width=3)
pressPlus.grid(row=2, column=4)
pressDivide = Button(bottom, text="÷", command=lambda: Calculate.divide(Calculate), width=3)
pressDivide.grid(row=3, column=4)
pressTimes = Button(bottom, text="x", command=lambda: Calculate.multiply(Calculate), width=3)
pressTimes.grid(row=4, column=4)
PressC = Button(bottom, text="C", command=lambda: Calculate.cancel(Calculate), width=3)
PressC.grid(row=5, column=5)
pressModulo = Button(bottom, text="Mod", command=lambda: Calculate.modulo(Calculate), width=3)
pressModulo.grid(row=4, column=3)

root.mainloop()
