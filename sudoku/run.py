from tkinter import Tk, Button, Text
from threading import Thread
import time

class Sudoku(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.squares = [[Button(self, width=0, height=0, command=lambda x=x,y=y: self.click(x,y)) for x in range(9)] for y in range(9)]
        self.place_squares()
        t1 = Thread(target=self.work)
        t1.start()

    def place_squares(self):
        for y in range(9):
            for x in range(9):
                self.squares[y][x].grid(row=y, column=x)

    def click(self, x,y):
        self.squares[y][x] = Text(self, width=2, height=1,bd=4)
        self.squares[y][x].grid(row=y, column=x)

    def work(self):
        while True:
            time.sleep(1)
            for y in range(9):
                for x in range(9):
                    try:
                        print(self.squares[y][x].get('1.0','end')[:1])
                    except AttributeError:
                        pass
if __name__ == '__main__':
    s = Sudoku()
    s.mainloop()
