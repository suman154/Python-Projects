# Write python program to create a simple GUI application
# calculator using tkinter

# import from tkinter module
from tkinter import *

# globally declare the experssion Variable
experssion = ""

# function to update experssion
# in the Text entry box

def press(num):
    # point out the global experssion variable
    global expression

    # concentration of 
    # current number with existing expression.
    expression = expression + str(num) 
    # update the expression by using set method
    equation.set(expression) 


# Function for Evaluation
def equalpress():
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

        

def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # create GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of gui window
    gui.geometry("270x150")

    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 

    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation) 

    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=70)
 
 
 # creating a Button widget
    button1 = Button(gui, text='1', fg='black', bg='red', 
                    command=lambda: press(1), height=1, width=7) 
    button1.grid(row=2, column=0)
    
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                    command=lambda: press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                    command=lambda: press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                    command=lambda: press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                    command=lambda: press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                    command=lambda: press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                    command=lambda: press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                    command=lambda: press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                    command=lambda: press(0), height=1, width=7) 
    button0.grid(row=5, column=0) 
 
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                command=lambda: press("+"), height=1, width=7) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                command=lambda: press("-"), height=1, width=7) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                    command=lambda: press("*"), height=1, width=7) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                command=equalpress, height=1, width=7) 
    equal.grid(row=5, column=2) 
 
    clear = Button(gui, text='Clear', fg='black', bg='red', 
                command=clear, height=1, width=7) 
    clear.grid(row=5, column='1') 
 
    Decimal= Button(gui, text='.', fg='black', bg='red', 
                    command=lambda: press('.'), height=1, width=7) 
    Decimal.grid(row=6, column=0) 
    
    # start the GUI 
    gui.mainloop() 

 


