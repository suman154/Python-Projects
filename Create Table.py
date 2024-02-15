from tkinter import*

class Table:

    def __init__(self, root):

        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='green', font=('Arial',14, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])