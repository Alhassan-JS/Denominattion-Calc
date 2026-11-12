#Import necessary libraries
from tkinter import *

#Setting up Main Window
r = Tk()
r.geometry("400x300")
r. title("main")

def tw():
    t = Toplevel()
    t.geometry("180x100")
    t.title("Top Level")

    l2 = Label(t , text="This is toplevel window")
    l2.pack
    
    t.mainloop()

l = Label(r , text="This is root window") 
btn = Button(r, text = "Click here to open another window", command=tw )

l.pack()
btn.pack()

r.mainloop()