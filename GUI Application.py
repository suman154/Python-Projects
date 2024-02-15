# Create First GUI Application using Python-Tkinter
from tkinter import *

# Creating Main Window
root = Tk()

# root window title and dimension
root.title("My Calculator")

# set geometry (width,height)
root.geometry('350x200')

# all the widgets will be here
lbl = Label(root, text = "First GUI Application")  # creating a lable
lbl.grid()

# adding a label to the root Window
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display text when button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)

# button Widget with red color Text inside 
btn = Button(root, text = "Click me" ,
             fg = "blue", command=clicked)

# set button grid
btn.grid(column=2, row=0)

# execute tkinter
root.mainloop()


    

