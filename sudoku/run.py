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
        nums = list(map( lambda x: str(x), list(range(10)) ))
        while True:
            time.sleep(1)
            for y in range(9):
                for x in range(9):
                    obj = self.squares[y][x]
                    # if self.squares[y][x] is object Text
                    if type(obj) == Text:
                        t = obj.get('1.0','end').strip()
                        if len(t) > 1:
                            if t[:1] not in nums:
                                obj.delete('1.0', 'end')
                            else:
                                obj.delete('1.0', 'end')
                                obj.insert('1.0', t[:1])


if __name__ == '__main__':
    s = Sudoku()
    s.mainloop()
