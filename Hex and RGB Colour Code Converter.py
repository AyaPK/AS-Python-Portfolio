from tkinter import *

root = Tk()
root.title("Aya's colour code converter")

leftside = Frame(root)
leftside.pack(side=LEFT)

rightside = Frame(root)
rightside.pack(side=RIGHT)

entry = Entry(leftside)
entry.pack()
button = Button(leftside, text="convert hex to RGB")
button.pack()
r1 = Entry(leftside, bg="#ff7b60")
g1 = Entry(leftside, bg="#60ff67")
b1 = Entry(leftside, bg="#6a60ff")
b1.pack(side=BOTTOM)
g1.pack(side=BOTTOM)
r1.pack(side=BOTTOM)
button2 = Button(leftside, text="convert RGB to hex")
button2.pack(side=BOTTOM)
output = Text(rightside, height=8, width=5)
output.pack(side=RIGHT)


def changecolor():
    if entry.get()[0:] != "#" and len(entry.get()) == 6:
        entry.insert(0, "#")
    global output
    color = entry.get()
    r1.delete(0, END)
    g1.delete(0, END)
    b1.delete(0, END)
    output.config(bg=color)
    r1.insert(END, int(color[1:-4], 16))
    g1.insert(END, int(color[3:-2], 16))
    b1.insert(END, int(color[5:], 16))


button.config(command=changecolor)


def changergb():
    entry.delete(0, END)
    hexa = ""
    if len(hex(int(r1.get()))[2:]) == 2:
        hexa = str(hexa) + hex(int(r1.get()))[2:]
    else:
        hexa = str(hexa) + "0" + hex(int(r1.get()))[2:]
    if len(hex(int(g1.get()))[2:]) == 2:
        hexa = str(hexa) + hex(int(g1.get()))[2:]
    else:
        hexa = str(hexa) + "0" + hex(int(g1.get()))[2:]
    if len(hex(int(b1.get()))[2:]) == 2:
        hexa = str(hexa) + hex(int(b1.get()))[2:]
    else:
        hexa = str(hexa) + "0" + hex(int(b1.get()))[2:]
    output.config(bg="#" + str(hexa))
    entry.insert(END, "#" + str(hexa))


button2.config(command=changergb)

root.mainloop()
