from tkinter import Tk, Button
from random import shuffle

class Puzzle(Tk):
    def __init__(self, img='', dimensions='10x10'):
        Tk.__init__(self)
        self.dimensions = dimensions.split('x')
        self.randomize_puzzles()
        self.moves = 1
        self.selected = []
        self.show_puzzles()

    def randomize_puzzles(self):  # {{{
        w,h = list(map(int, self.dimensions))
        l = [[Button(self, text=f"{x},{y}", command=lambda x=x,y=y: self.swap_puzzles((x,y))) for x in range(w)] for y in range(h)]
        self.puzzles = []
        for line in l:
            self.puzzles += line
        shuffle(self.puzzles)
        self.puzzles = [self.puzzles[y*w:(y+1)*w] for y in range(h)]
        # }}}

    def show_puzzles(self):
        w,h = list(map(int, self.dimensions))
        for y in range(h):
            for x in range(w):
                #b1 = Button(self, text=f"{self.puzzles[y][x]}", command=lambda x=x,y=y: self.swap_puzzles((x,y)))
                b = self.puzzles[y][x]
                b.grid(column=x, row=y)

    def swap_puzzles(self, xy):
        x,y = xy
        if self.moves % 2==0:
            x1,y1 = self.selected
            self.puzzles[y1][x1], self.puzzles[y][x]= self.puzzles[y][x], self.puzzles[y1][x1]
            print(self.puzzles)
            #for i,j in [[x,y], [x1,y1]]:
            #b = self.puzzles[y][x]
            #b.grid(column=x, row=y)
            #b = self.puzzles[y1][x1]
            #b.grid(column=x1, row=y1)
            self.selected = []
                #b1 = Button(self, text=f"{self.puzzles[j][i]}", command=lambda i=i,j=j: self.swap_puzzles((i,j))).grid(column=i, row=j)
            #Button(self, text=f"{self.puzzles[y][x]}", command=lambda x=x,y=y: self.swap_puzzles((x,y))).grid(column=x, row=y)
            #Button(self, text=f"{self.puzzles[y1][x1]}", command=lambda x1=x1,y1=y1: self.swap_puzzles((x1,y1))).grid(column=x1, row=y1)
        else:
            self.selected = [x,y]
        self.moves += 1
        self.show_puzzles()

if __name__ == '__main__':
    p = Puzzle()
    p.mainloop()
