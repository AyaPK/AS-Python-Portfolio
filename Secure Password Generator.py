import random
import string
from tkinter import *

main = Tk()
main.geometry("500x150")
main.title("Aya's Password Generator")
pw = Label()

passspace = Frame(main, relief=SUNKEN, bg="grey")
passspace.pack(side=TOP)

pwlen = Scale(main, from_=8, to=32, orient=HORIZONTAL, length=400)
pwlen.pack(side=BOTTOM)

l1 = Label(text="Select Password Length")
l1.pack(side=BOTTOM)

paw = []
vari = []
lets = IntVar()
nums = IntVar()
specs = IntVar()

l2 = Label(passspace, text=paw)
l2.pack()

checkboxes = Frame(main)
checkboxes.pack(side=RIGHT)

speccheck = Checkbutton(checkboxes, text="Special Characters",
                        variable=specs).pack(side=TOP, anchor=W)
numcheck = Checkbutton(checkboxes, text="Numbers",
                       variable=nums).pack(side=TOP, anchor=W)
letcheck = Checkbutton(checkboxes, text="Letters",
                       variable=lets).pack(side=TOP, anchor=W)


def generate():
    paw = []
    if lets.get() == 0 and nums.get() == 0 and specs.get() == 0:
        paw.append("Please choose at least one password option")
    else:
        for x in range(0, pwlen.get()):
            newchar = ""
            while newchar == "":
                rand = random.randint(0, 2)
                if lets.get() == 1 and rand == 0:
                    newchar = random.choice(string.ascii_letters)
                    paw.append(newchar)
                if nums.get() == 1 and rand == 1:
                    newchar = random.choice(string.digits)
                    paw.append(newchar)
                if specs.get() == 1 and rand == 2:
                    newchar = random.choice(string.punctuation)
                    paw.append(newchar)

    temp = ''.join(paw)
    global vari
    vari = temp
    l2.config(text=temp)


def addToClipBoard():
    main.clipboard_clear()
    main.clipboard_append(vari)
    main.update()  # now it stays on the clipboard after the window is closed


b1 = Button(main, text="Generate new password", command=generate)
b1.pack()

b2 = Button(main, text="Copy to clipboard", command=addToClipBoard)
b2.pack()

main.mainloop()
