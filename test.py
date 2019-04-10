from tkinter import *

root = Tk()
root.config(bg="red")
root.title("Menu testing")

## preferences ##
def preferences():
    prefwindow = Toplevel()
    prefwindow.geometry("200x200")
    leftside = Frame(prefwindow)
    middle=Frame(prefwindow)
    rightside = Frame(prefwindow)
    leftside.grid(column=1, row=1, rowspan=3)
    rightside.grid(column=3, row=1, rowspan=3)
    middle.grid(column=2, row=4, rowspan=2)
    colourlabel = Label(leftside, text="choose a colour")
    fontlabel = Label(leftside, text="Font")
    fontlabel.grid(row=2)
    def colorlist():
        optionList = ('red', 'green', 'blue', 'purple', 'pink')
        v = StringVar()
        v.set(optionList[0])
        om = OptionMenu(rightside, v, *optionList)
        om.grid(column=1, row=2)

    def fontlist():
        optionList = ('arial', 'helvetica', 'monotype')
        v = StringVar()
        v.set(optionList[0])
        om = OptionMenu(rightside, v, *optionList)
        om.grid(column=1, row=2)
    colorlist()
    colourlabel.grid(row=1)
    savebutton = Button(middle, text="Save")
    savebutton.grid(column=2, row=2)

    def save():
        root.config(bg=v.get())
        texttochange.config(bg=v.get())
        prefwindow.destroy()

    savebutton.config(command=save)

## toolbar menu ##
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="save")
filemenu.add_command(label="load")
filemenu.add_separator()
filemenu.add_command(label="quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Preferences", command=preferences)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)

texttochange = Label(root, text="Use the settings menu to change me", bg="red")
texttochange.pack()



root.mainloop()