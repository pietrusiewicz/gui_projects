from tkinter import Tk, Button, Text
from threading import Thread
import time
from collections import Counter

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
                    # check correctness of tag square
                    if type(obj) == Text: # {{{
                        t = obj.get('1.0','end').strip()
                        if len(t) > 1:
                            obj.delete('1.0', 'end')
                            if t[:1] in nums:
                                obj.insert('1.0', t[:1]) #}}}
            self.check_correct_cols()

    def check_correct_cols(self):
        #c = Counter()
        for i in range(9):
            c = Counter()
            #l = []
            for j in range(9):
                t = self.squares[j][i]
                if type(t) == Text:
                    t = t.get('1.0','end')[:1]
                    c[t] += 1
            if len(list(c)) == 9:
                print(f"kolumna {i} ulozona")
        

if __name__ == '__main__':
    s = Sudoku()
    s.mainloop()
