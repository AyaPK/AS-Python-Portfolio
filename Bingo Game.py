from tkinter import *
from random import randint
import string
import os
import time

root = Tk()
root.geometry("700x150")
bingo = FALSE
bingo1 = FALSE
bingo2 = FALSE
bingo3 = FALSE
bingo4 = FALSE
bingo5 = FALSE
bingo6 = FALSE
bingo7 = FALSE
bingo8 = FALSE
bingo9 = FALSE
bgcolor = "#f0f0ed"
bingos = 0
matches = 0

### frames construction ###
maingrid = Frame(root, bg="black")
makebutton = Frame(root, bg=bgcolor)
lasttext = Frame(root, bg=bgcolor)
lastres = Frame(root, bg=bgcolor)
drawntext = Frame(root, bg=bgcolor)
drawnres = Frame(root, bg=bgcolor)
matchtext = Frame(root, bg=bgcolor)
matchchance = Frame(root, bg=bgcolor)
drawbutton = Frame(root, bg=bgcolor)
bingotext = Frame(root, bg=bgcolor)

maingrid.grid(row=1, column=1, rowspan=3, columnspan=3)
makebutton.grid(row=4, column=2)
lasttext.grid(row=1, column=5, sticky=E)
lastres.grid(row=1, column=6, sticky=W)
drawntext.grid(row=3, column=5, sticky=E)
drawnres.grid(row=3, column=6)
matchtext.grid(row=2, column=5, sticky=E)
matchchance.grid(row=2, column=6, sticky=W)
drawbutton.grid(row=5, column=2)
bingotext.grid(row=4, column=3, columnspan=4, rowspan=2)
#########################

## create visual ##
make = Button(makebutton, text="Make a new card")
lastdraw = Label(lasttext, text="You drew: ", justify=RIGHT)
lastnum = Label(lastres)
drawnnums = Label(drawntext, text="The drawn numbers are: ", justify=RIGHT)
drawnlist = Text(drawnres, height=6, width=50, font=("monotype", 5))
matchlab = Label(
    matchtext,
    text="The chance of pulling a match on the next draw is: ",
    justify=RIGHT,
)
matchperc = Label(matchchance, justify=LEFT)
draw = Button(drawbutton, text="Draw a number")
success = Label(bingotext, font=("Helvetica", 40))
make.grid()
lastdraw.grid()
lastnum.grid()
drawnnums.grid()
drawnlist.grid()
matchlab.grid()
matchperc.grid()
draw.grid()
success.grid()
###################


## set up empty card ##
bdthick = 1
bdcolor = "black"
space1 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space2 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space3 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space4 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space5 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space6 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space7 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space8 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space9 = Frame(maingrid, highlightthickness=bdthick, highlightbackground=bdcolor)
space1.grid(row=1, column=1)
space2.grid(row=1, column=2)
space3.grid(row=1, column=3)
space4.grid(row=2, column=1)
space5.grid(row=2, column=2)
space6.grid(row=2, column=3)
space7.grid(row=3, column=1)
space8.grid(row=3, column=2)
space9.grid(row=3, column=3)
#################

## make new card ##
num1 = Label(space1)
num2 = Label(space2)
num3 = Label(space3)
num4 = Label(space4)
num5 = Label(space5)
num6 = Label(space6)
num7 = Label(space7)
num8 = Label(space8)
num9 = Label(space9)

numarray = []


def makecard():
    global bingos
    global bingo
    global bingo1
    global bingo2
    global bingo3
    global bingo4
    global bingo5
    global bingo6
    global bingo7
    global bingo8
    global bingo9
    global numarray
    global drawnlist
    global drawnnumbers
    global success
    global matches
    global lastnum
    bingo1 = FALSE
    bingo2 = FALSE
    bingo3 = FALSE
    bingo4 = FALSE
    bingo5 = FALSE
    bingo6 = FALSE
    bingo7 = FALSE
    bingo8 = FALSE
    bingo9 = FALSE
    root.config(bg="#f0f0ed")
    bingos = 0
    success.config(text="")
    bingo = FALSE
    numarray = []
    matches = 0
    drawnnumbers = []
    drawnlist.delete(1.0, END)
    for x in range(0, 9):
        num = ""
        while num == "":
            newnum = randint(0, 99)
            if newnum not in numarray:
                num = newnum
                numarray.append(num)

    num1.config(text=numarray[0], bg="#f0f0ed", width=2)
    num2.config(text=numarray[1], bg="#f0f0ed", width=2)
    num3.config(text=numarray[2], bg="#f0f0ed", width=2)
    num4.config(text=numarray[3], bg="#f0f0ed", width=2)
    num5.config(text=numarray[4], bg="#f0f0ed", width=2)
    num6.config(text=numarray[5], bg="#f0f0ed", width=2)
    num7.config(text=numarray[6], bg="#f0f0ed", width=2)
    num8.config(text=numarray[7], bg="#f0f0ed", width=2)
    num9.config(text=numarray[8], bg="#f0f0ed", width=2)
    num1.grid()
    num2.grid()
    num3.grid()
    num4.grid()
    num5.grid()
    num6.grid()
    num7.grid()
    num8.grid()
    num9.grid()


##################
make.config(command=makecard)

## Generate number ##
drawnnumbers = []


def drawnumber():
    global bingo1
    global bingo2
    global bingo3
    global bingo4
    global bingo5
    global bingo6
    global bingo7
    global bingo8
    global bingo9
    global bingo
    global lastnum
    global bgcolor
    global bingos
    global matches
    global match1
    global match2
    global match3
    global match4
    global match5
    global match6
    global match7
    global match8
    global match9
    drawnum = ""
    if len(drawnnumbers) != 100:
        while drawnum == "":
            drawnew = randint(0, 99)
            if drawnew not in drawnnumbers:
                drawnum = drawnew
                drawnnumbers.append(drawnew)
                lastnum.config(text=drawnew)
                lastnum.grid()
                drawnlist.insert(END, str(drawnew) + " ")
                matches = matches + 1
        try:
            check = numarray.index(drawnew)
        except:
            check = "nothing"
        if check == 0:
            bingo1 = TRUE
            num1.config(bg="green")
            bingos = bingos + 1
        if check == 1:
            bingo2 = TRUE
            num2.config(bg="green")
            bingos = bingos + 1
        if check == 2:
            bingo3 = TRUE
            num3.config(bg="green")
            bingos = bingos + 1
        if check == 3:
            bingo4 = TRUE
            num4.config(bg="green")
            bingos = bingos + 1
        if check == 4:
            bingo5 = TRUE
            num5.config(bg="green")
            bingos = bingos + 1
        if check == 5:
            bingo6 = TRUE
            num6.config(bg="green")
            bingos = bingos + 1
        if check == 6:
            bingo7 = TRUE
            num7.config(bg="green")
            bingos = bingos + 1
        if check == 7:
            bingo8 = TRUE
            num8.config(bg="green")
            bingos = bingos + 1
        if check == 8:
            bingo9 = TRUE
            num9.config(bg="green")
            bingos = bingos + 1
    else:
        lastnum.config(text="There are no numbers left!!")
    if bingo1 and bingo2 and bingo3:
        bingo = TRUE
    if bingo3 and bingo4 and bingo5:
        bingo = TRUE
    if bingo7 and bingo8 and bingo9:
        bingo = TRUE
    if bingo1 and bingo4 and bingo7:
        bingo = TRUE
    if bingo2 and bingo5 and bingo8:
        bingo = TRUE
    if bingo3 and bingo6 and bingo9:
        bingo = TRUE
    if bingo1 and bingo5 and bingo9:
        bingo = TRUE
    if bingo3 and bingo5 and bingo7:
        bingo = TRUE
    if bingo == TRUE:
        global bgcolor
        root.config(bg="green")
        success.config(text="BINGO!")
    chance = float(((9 - bingos) / (100 - matches)) * 100)
    matchperc.config(text=str(round(chance, 2)) + "%")


draw.config(command=drawnumber)
#####################


root.mainloop()
