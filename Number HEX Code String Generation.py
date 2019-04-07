from tkinter import *

root = Tk()
root.title("Number to hex string converter")
topleft = Frame(root)
bottomleft = Frame(root)
topmiddle = Frame(root)
bottommiddle = Frame(root)
topright = Frame(root)
button = Frame(root)
cop = Frame(root)
topleft.grid(row=1, column=1)
bottomleft.grid(row=2, column=1)
topmiddle.grid(row=1, column=2)
bottommiddle.grid(row=2, column=2)
topright.grid(row=1, column=3, rowspan=5)
button.grid(row=3, column=1)
cop.grid(row=3, column=2)
fromtext = Label(topleft, text="from")
totext = Label(bottomleft, text="to")
fromnum = Entry(topmiddle)
tonum = Entry(bottommiddle)
output = Text(topright, height=5, width=10)
run = Button(button, text="Run")
copy = Button(cop, text="Copy to clipboard")
fromtext.grid()
totext.grid()
fromnum.grid()
tonum.grid()
output.grid()
run.grid()
copy.grid()


######### main formula #########
def formulate():
    output.delete(1.0, END)
    for x in range(int(fromnum.get()), int(tonum.get())+1):
        output.insert(END, str(x)+": "+str(hex(x))+"\n")


def copycode():
    root.clipboard_clear()
    root.clipboard_append(output.get(1.0, END))
    root.update()


run.config(command=formulate)
copy.config(command=copycode)


root.mainloop()
