from tkinter import *

root = Tk()
root.title("Celcius to Farenheit converter")

leftside = Frame(root)
middle = Frame(root)
rightside = Frame(root)
leftside.grid(row=1, column=1, rowspan=2)
middle.grid(row=1, column=2, rowspan=2)
rightside.grid(row=1, column=3, rowspan=2)

l1 = Label(leftside, text="Celcius")
l2 = Label(leftside, text="Farenheit")
e1 = Entry(middle, width=5)
e2 = Entry(middle, width=5)
b1 = Button(rightside, text="Convert C to F")
b2 = Button(rightside, text="Convert F to C")

l1.grid(row=1)
l2.grid(row=2)
e1.grid(row=1)
e2.grid(row=2)
b1.grid(row=1)
b2.grid(row=2)

###############################################


def ctof():
    temp1 = float(e1.get())
    cels = round((temp1*1.8)+32, 2)
    e2.delete(0, END)
    e2.insert(END, cels)


def ftoc():
    temp2 = float(e2.get())
    far = round((temp2-32)/1.8, 2)
    e1.delete(0, END)
    e1.insert(END, far)


b1.config(command=ctof)
b2.config(command=ftoc)
root.mainloop()
