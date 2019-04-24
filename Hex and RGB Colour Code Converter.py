import random
from tkinter import *

defaultcolour = "#"
for x in range(0,6):
    rand = random.choice("ABCDEF0123456789")
    defaultcolour = (defaultcolour + rand)

root = Tk()
root.title("Aya's colour code converter")




leftside = Frame(root)
hexspace = Frame(leftside)
buttonspace = Frame(leftside)
rgbspace = Frame(leftside)

leftside.grid(row=1, column=1)
hexspace.grid(row=1, column=1, columnspan=2)
buttonspace.grid(row=2, column=1, rowspan=2, columnspan=2)
rgbspace.grid(row=4, column=1, rowspan=3, columnspan=2)

rightside = Frame(root)
rightside.grid(row=1, column=2)

hext = Label(hexspace, text="HEX code")
hext.grid(row=1, column=1)
hexentry = Entry(hexspace)
hexentry.grid(row=1, column=2)
hexentry.insert(END, defaultcolour)
button = Button(buttonspace, text="convert hex to RGB")
hexcopy = Button(buttonspace, text="Copy HEX code")
button.grid(column=1, row=1)
hexcopy.grid(row=1, column=2)
red = Label(rgbspace, text="Red")
green = Label(rgbspace, text="Green")
blue = Label(rgbspace, text="Blue")
red.grid(row=1, column=1)
green.grid(row=2, column=1)
blue.grid(row=3, column=1)
r1 = Entry(rgbspace, bg="#ff7b60")
g1 = Entry(rgbspace, bg="#60ff67")
b1 = Entry(rgbspace, bg="#6a60ff")
r1.insert(END, int(defaultcolour[1:-4], 16))
g1.insert(END, int(defaultcolour[3:-2], 16))
b1.insert(END, int(defaultcolour[5:], 16))
b1.grid(row=3, column=2)
g1.grid(row=2, column=2)
r1.grid(row=1, column=2)
button2 = Button(buttonspace, text="convert RGB to hex")
button2.grid(row=2, column=1)
rgbcopy = Button(buttonspace, text="Copy RGB code")
rgbcopy.grid(row=2, column=2)
output = Text(rightside, height=8, width=15, bg=defaultcolour)
output.pack(side=TOP)
randomcolour = Button(rightside, text="Generate random colour")
randomcolour.pack(side=BOTTOM)


def hextorgb():
    if hexentry.get()[0:] != "#" and len(hexentry.get()) == 6:
        hexentry.insert(0, "#")
    global output
    color = hexentry.get()
    r1.delete(0, END)
    g1.delete(0, END)
    b1.delete(0, END)
    output.config(bg=color)
    r1.insert(END, int(color[1:-4], 16))
    g1.insert(END, int(color[3:-2], 16))
    b1.insert(END, int(color[5:], 16))


button.config(command=hextorgb)


def rgbtohex():
    hexentry.delete(0, END)
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
    hexentry.insert(END, "#" + str(hexa).upper())


def copyhex():
    root.clipboard_clear()
    root.clipboard_append(hexentry.get())
    root.update()


def copyrgb():
    root.clipboard_clear()
    root.clipboard_append(str(r1.get())+", "+str(g1.get())+", "+str(b1.get()))
    root.update()

def rando():
    newcolor = "#"
    for x in range(0,6):
        randcol = random.choice("ABCDEF0123456789")
        newcolor = (newcolor + randcol)
    hexentry.delete(0, END)
    hexentry.insert(END, newcolor)
    r1.delete(0, END)
    r1.insert(END, int(newcolor[1:-4], 16))
    g1.delete(0, END)
    g1.insert(END, int(newcolor[3:-2], 16))
    b1.delete(0, END)
    b1.insert(END, int(newcolor[5:], 16))
    output.config(bg=newcolor)

randomcolour.config(command=rando)

rgbcopy.config(command=copyrgb)
button2.config(command=rgbtohex)
hexcopy.config(command=copyhex)


root.mainloop()
