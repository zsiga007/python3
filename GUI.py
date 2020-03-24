from tkinter import *
master = Tk()
master_rgb = "#%02x%02x%02x" % (128, 192, 200)
var=IntVar()
c = Checkbutton(master, text="Expand", variable=var)
c.pack()
separator = Frame(height=5, bd=5, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()
w = Message(master, text="hello")
w.pack()

mainloop()

## or

from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()
