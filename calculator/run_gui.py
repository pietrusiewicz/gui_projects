import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.keyboard = [[7,8,9, '+'],
                         [6,5,4, '-'],
                         [3,2,1, '*'],
                         [0,'00','=', '/']]

    def menu(self):
        self.e = tk.Entry(self)
        self.e.grid(row=0, column=0, columnspan=4)
        for i in range(4):
            for j in range(4):
                b = tk.Button(self, text=f"{self.keyboard[i][j]}", width=3, height=2)
                b.grid(row=i+1, column=j)
                """
        b = tk.Button(self, text=f"{self.keyboard[3][0]}", width=3, height=2)
        b.grid(row=4, column=0)
        b = tk.Button(self, text=f"{self.keyboard[3][1]}", width=3, height=2)
        b.grid(row=4, column=1)
                """


if __name__ == '__main__':
    c = Calculator()
    c.menu()
    c.mainloop()
