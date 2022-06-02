from tkinter import Tk, Button, Text

class Sudoku(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.squares = [[Button(self, width=0, height=0, command=lambda x=x,y=y: self.click(x,y)) for x in range(9)] for y in range(9)]
        self.place_squares()

    def place_squares(self):
        for y in range(9):
            for x in range(9):
                self.squares[y][x].grid(row=y, column=x)

    def click(self, x,y):
        Text(self, width=2, height=1,bd=4).grid(row=y, column=x)

if __name__ == '__main__':
    s = Sudoku()
    s.mainloop()
