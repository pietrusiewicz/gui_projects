from tkinter import *
from prep_image import Imager
import os, math

im = Imager()
# i want add pillow connect to lay better pieces

class Puzzle(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.zerone, self.xy = 0, [0, 0]
        l = im.pieces
        length = len([_ for _ in l if _[0]=='A'])#int(math.sqrt(len(l)))
        self.create_puzzles = lambda l: [l[i-length:i] for i in range(length, len(l)+length, length)]
        self.raw_puzzles = self.create_puzzles(l)
        self.puzzles = self.create_puzzles(l)
        print(self.puzzles)
        #self.puzzles = self.create_puzzles(im.shuffled_pieces(l))
        #print(self.puzzles)
        self.grid_puzzles()

    # display puzzles
    def grid_puzzles(self):
        for i, row in enumerate(self.puzzles):
            for j, piece in enumerate(row):
                img = PhotoImage(file=f'./pieces/{piece}')
                b = Button(self, text=piece,image=img, command=lambda i=i, j=j: self.swap_puzzle(j,i))
                b.image=img
                b.grid(row=i, column=j)

    # change places of selected puzzle
    def swap_puzzle(self, x, y):
        if self.zerone == 0:
            self.zerone = 1
            self.xy = [x,y]
            img = PhotoImage(file=f"pieces/{self.puzzles[y][x]}")
            b = Button(self, text=self.puzzles[y][x], image=img, state=DISABLED)
            b.image=img
            b.grid(row=y, column=x)
        else:
            self.zerone = 0
            x2,y2 = self.xy[0], self.xy[1]
            self.puzzles[y2][x2],self.puzzles[y][x] = self.puzzles[y][x],self.puzzles[y2][x2]
            for x,y in [[x,y],[x2,y2]]:
                img = PhotoImage(file=f"pieces/{self.puzzles[y][x]}")
                b = Button(self, text=self.puzzles[y][x], image=img, command=lambda i=y, j=x: self.swap_puzzle(j,i))
                b.image=img
                b.grid(row=y, column=x)
            if self.raw_puzzles == self.puzzles:
                self.win_show()

    # display end of game
    def win_show(self):
        for i, row in enumerate(self.puzzles):
            for j, piece in enumerate(row):
                img = PhotoImage(file=f"pieces/{piece}")
                b = Button(self, image=img, state=DISABLED)
                b.image=img
                b.grid(row=i, column=j)
        l = Label(self, text="brawo ułożyłeś puzzle")
        s = self.size()
        l.grid(row=s[0],columnspan=s[1]+1)
        b = Button(self, text='play again', command=lambda: [self.destroy(), self.__init__()])
        b.grid(row=s[0]+1, columnspan=s[1]+1)
        #print(self.puzzles)


if '__main__' == __name__:
    g = Puzzle()
    g.mainloop()
