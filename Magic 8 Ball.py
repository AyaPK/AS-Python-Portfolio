from random import *
from tkinter import *
import ctypes


answers = [
    'yes',
    'no',
    'maybe'
]

main = Tk()
main.title("8Ball")
#  begins to generate variable labels to keep it tidy
l3 = Label()
ans = Label()
lnew = Label()
lnew1 = Label()
lList = Label()
lList1 = Label()

#  sets geometry
main.geometry("500x500")
main.grid_propagate(False)


# generate answer
def generate():
    # Generates a random number to match the var length
    num = randint(0, len(answers) - 1)
    answer = answers[num]  # takes the answer based on the given number
    ans.config(text="You asked: " + q1.get(), wraplength=200,
               justify=LEFT)  # starts updating labels
    l3.config(text="The 8ball says... " + answer +
              "!!!", wraplength=300, justify=LEFT)
    ans.grid(row=2, column=1, sticky=W)
    l3.grid(row=2, column=2, columnspan=2, sticky=W)

# add new answer


def newAns():
    answers.append(q2.get())  # adds the entry to the array
    lnew.config(text="new answer added: ")  # updates labels
    lnew.grid(row=4, column=1)
    lnew1.config(text=q2.get())
    lnew1.grid(row=4, column=2)

# list available answers


def listAns():
    lList.config(text="The current available answers are: ", wraplength=100)
    lList.grid(row=7, column=1)
    lList1.config(text=answers, wraplength=100, justify=LEFT)
    lList1.grid(row=7, column=2)

# break the ball :(


def breakBall():
    # intentional ctype error to crash the program
    p = ctypes.pointer(ctypes.c_char.from_address(5))
    p[0] = b'x'


# Add default labels
l1 = Label(text="Ask a question!")
l1.grid(row=1, column=1, sticky=W)
l2 = Label(text="Add a new answer!")
l2.grid(row=3, column=1, sticky=W)

q1 = Entry(main)
q1.grid(row=1, column=2, sticky=W)

q2 = Entry(main)
q2.grid(row=3, column=2, sticky=W)


# add default buttons
b1 = Button(main, text="Ask!", command=generate).grid(row=1, column=3)
b2 = Button(main, text="Add new answer", command=newAns).grid(row=3, column=3)
b3 = Button(main, text="List answers", command=listAns).grid(row=5, column=2)
b4 = Button(main, text="Break the ball",
            command=breakBall).grid(row=5, column=3)


main.mainloop()