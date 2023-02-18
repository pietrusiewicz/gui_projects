from tkinter import Tk, Button, Label, PhotoImage
from random import shuffle
from PIL import Image, ImageTk
import os
from sys import argv

class Puzzle(Tk):
    "class needs two arguments"
    def __init__(self, img='', dimensions='2x2'):
        Tk.__init__(self)
        self.moves = 1
        self.selected = []

    # prepare puzzles
    def randomize_puzzles(self):  # {{{
        # number of elements in row/column
        w,h = self.dimensions

        # create 2D array where [row[column]]
        self.correct_puzzles = [[Button(self, text=f"{x},{y}") for x in range(w)] for y in range(h)]

        # convert puzzles to array
        self.puzzles = []
        for tup in self.correct_puzzles:
            self.puzzles += tup

        # shuffle puzzles in array
        shuffle(self.puzzles)

        # convert array to 2D array drawing [row[column]]
        self.puzzles = [self.puzzles[y*w:(y+1)*w] for y in range(h)]
        # }}}

    # display puzzles
    def show_puzzles(self): # {{{
        # number of elements in row/column
        w,h = self.dimensions

        # for loop [ROW[column]]
        for y in range(h):
            # for loop [row[COLUMN]]
            for x in range(w):
                # get single puzzle from self.puzzles
                b = self.puzzles[y][x]
                b.grid(row=y, column=x)

                # image is entered
                if self.img: # {{{

                    # crop entered image
                    # by variables declared (50 line)
                    wycinek = self.get_crop(tx, ty)

                    # set cropped image
                    # to needed class 
                    img = ImageTk.PhotoImage(wycinek)
                    # and needed key
                    b.image=img # }}}

                # what command is executed after click this element
                b["command"] = lambda x=x,y=y: self.swap_puzzles([x,y])
                
                # any time ago button was disabled
                b["state"] = "normal"
                
                # this is a clicked element
                if self.moves % 2 and self.selected == [x,y]:
                    b["state"]="disabled"  # }}}
    
    # swap elements
    def swap_puzzles(self, xy): #{{{
        "method does swapping puzzles after click"
        # first clicked element
        x,y = xy

        # two elements are clicked
        if not (self.moves % 2):
            
            # second clicked element
            x1,y1 = self.selected

            # replace two elements
            self.puzzles[y1][x1], self.puzzles[y][x]= self.puzzles[y][x], self.puzzles[y1][x1]

            # clear coordinates of elements in self.selected
            self.selected = []


            # puzzles are placed
            if self.puzzles == self.correct_puzzles:
                self.win_screen()

        # one element is clicked
        else:
            self.selected = [x,y]

        # refresh puzzles table
        self.show_puzzles()

        # incrementing number of moves
        self.moves += 1 # }}}

    # scene of win
    def win_screen(self): # {{{
        w,h = self.dimension
        
        # place "koniec gry"
        Label(self, text="koniec gry").grid(row=h-1, rowspan=h, columnspan=w)

        # button what play again
        b = Button(self, text="play again")
        b["command"] = lambda: [b.grid_forget(), b.forget(),self.randomize_puzzles(), self.show_puzzles()]
        b.grid(row=h, rowspan=h, columnspan=w) # }}}

    # get a crop of image
    def get_crop(self,tx,ty): # {{{
        pic = Image.open(self.img)
        s = pic.size
        w,h = self.dimensions
        dx, dy = s[0]/w, s[1]/h
        return pic.crop((tx*dx,ty*dy,(tx+1)*dx,(ty+1)*dy)) # }}}

if __name__ == '__main__':
    p = Puzzle()
    p.img = argv[1] if len(argv) > 1 else ''
    dims = "10x10"
    p.dimensions = list(map(int, dims.split('x')))
    p.randomize_puzzles()
    p.show_puzzles()
    p.mainloop()
