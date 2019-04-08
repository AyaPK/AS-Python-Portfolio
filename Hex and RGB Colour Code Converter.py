from tkinter import *

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
hexentry.insert(END, "#F0F0ED")
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
r1.insert(END, "240")
g1.insert(END, "240")
b1.insert(END, "237")
b1.grid(row=1, column=2)
g1.grid(row=2, column=2)
r1.grid(row=3, column=2)
button2 = Button(buttonspace, text="convert RGB to hex")
button2.grid(row=2, column=1)
rgbcopy = Button(buttonspace, text="Copy RGB code")
rgbcopy.grid(row=2, column=2)
output = Text(rightside, height=8, width=15)
output.pack(side=RIGHT)


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


rgbcopy.config(command=copyrgb)
button2.config(command=rgbtohex)
hexcopy.config(command=copyhex)


root.mainloop()
