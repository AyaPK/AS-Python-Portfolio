from tkinter import *

main = Tk()
main.title("Aya's Fizzbuzz Solution")
main.geometry("500x200")

instructions = Frame(main, bd=2)
label1 = Frame(main, bd=2)
label2 = Frame(main)
entry1 = Frame(main, bd=3)
entry2 = Frame(main, bd=3)
entry3 = Frame(main, bd=3)
entry4 = Frame(main, bd=3)
button1 = Frame(main, takefocus=1)
output = Frame(main, padx=11)
scrollarea = Frame(main)

main.grid_rowconfigure(1)
main.grid_columnconfigure(0)

instructions.grid(row=4, column=1, columnspan=3, sticky=W)
label1.grid(row=1, column=1, sticky=W)
label2.grid(row=2, column=1, sticky=W)
entry1.grid(row=1, column=2, sticky=EW)
entry2.grid(row=1, column=3, sticky=EW)
entry3.grid(row=2, column=2, sticky=EW)
entry4.grid(row=2, column=3, sticky=EW)
button1.grid(row=3, column=3, sticky=EW)
output.grid(row=1, column=5, rowspan=8, columnspan=2, sticky=E)
scrollarea.grid(row=1, column=10, rowspan=8, sticky=W)

l1 = Label(label1, text="Choose numbers")
l2 = Label(label2, text="Choose words")
num1 = Entry(entry1)
num2 = Entry(entry2)
fizz = Entry(entry3)
buzz = Entry(entry4)
go = Button(button1, text="Go!")
result = Text(output, height=8, width=10)
scroller = Scrollbar(scrollarea, command=result.yview)
ins = Label(instructions, text="Type the two numbers you'd like to Fizzbuzz on thoe top row\nand choose the two words you'd like to represent\ntheir multiples on the bottom row")
l1.grid()
l2.grid()
ins.grid()
fizz.grid()
buzz.grid()
num1.grid()
num2.grid()
go.grid()
result.grid()
scroller.grid(ipady=50)

array = []
ready = 0


def calculate():
    result.delete(1.0, END)
    for x in range(1, 100):
        if x % int(num1.get()) == 0 and x % int(num2.get()) == 0:
            result.insert(END, str(fizz.get() + buzz.get()) + "\n")
        elif x % int(num1.get()) == 0:
            result.insert(END, str(fizz.get()) + "\n")
        elif x % int(num2.get()) == 0:
            result.insert(END, str(buzz.get()) + "\n")
        else:
            result.insert(END, str(x) + "\n")


go.config(command=calculate)

main.mainloop()
