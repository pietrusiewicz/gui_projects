from tkinter import Tk, Button, Label, PhotoImage
from random import shuffle
from PIL import Image, ImageTk
import os
import sys

class Puzzle(Tk):
    def __init__(self, img='linus.png', dimensions='2x2'):
        Tk.__init__(self)
        self.img = img
        self.dimensions = list(map(int,dimensions.split('x')))
        self.randomize_puzzles()
        self.moves = 1
        self.selected = []
        self.show_puzzles()

    def randomize_puzzles(self):  # {{{
        w,h = self.dimensions
        #self.correct_puzzles = [[Button(self) for x in range(w)] for y in range(h)]
        self.correct_puzzles = [[(x,y) for x in range(w)] for y in range(h)]
        
        #self.imgs = self.get_imgs()
        #self.correct_puzzles = list(zip(self.correct_puzzles, imgs))

        self.puzzles = []
        for tup in self.correct_puzzles:
            self.puzzles += tup
        shuffle(self.puzzles)
        self.puzzles = [self.puzzles[y*w:(y+1)*w] for y in range(h)]
        # }}}

    def show_puzzles(self,koniec=0): # {{{
        w,h = self.dimensions
        #wycinki = [[crop_img(x,y) for x in range(len(self.correct_puzzles[y]))] for y in range(length_rows)]
        #for y, objs in enumerate(self.puzzles):
        for y in range(h):
            for x in range(w):
                tx, ty = self.puzzles[y][x]
                wycinek = self.get_crop(tx, ty)
                img2 = ImageTk.PhotoImage(wycinek)
                b = Button(self, image=img2)
                b.image=img2
                b.grid(row=y, column=x)
                if koniec:
                    b["state"]="disabled"
                    continue
                #tup, img = tup_img
                #wy = ImageTk.PhotoImage(img.crop((x*dx,y*dy,(x+1)*dx,(y+1)*dy)))
                #wycinek = pic.crop((tx*dx,ty*dy,(tx+1)*dx,(ty+1)*dy))
                b["command"] = lambda x=x,y=y: self.swap_puzzles([x,y])
                if self.selected != []:
                    if self.selected == [x,y]:
                        b["state"]="disabled"

    def swap_puzzles(self, xy): #{{{
        x,y = xy
        if self.moves % 2==0:
            x1,y1 = self.selected
            self.puzzles[y1][x1], self.puzzles[y][x]= self.puzzles[y][x], self.puzzles[y1][x1]
            self.selected = []
            if self.puzzles == self.correct_puzzles:
                self.win_screen()
        else:
            self.selected = [x,y]

        self.show_puzzles()
        self.moves += 1 # }}}

    def win_screen(self): # {{{
        w,h = self.dimensions
        for y in range(h):
            for x in range(w):
                #tx, ty = self.puzzles[y][x]
                wycinek = self.get_crop(x, y)
                img2 = ImageTk.PhotoImage(wycinek)
                b = Button(self, image=img2)
                b.image=img2
                b["state"]="disabled"
                b.grid(row=y, column=x)
        #self.show_puzzles(1)
        #s = self.size()
        l = Label(self, text="koniec gry")
        l.grid(row=0, rowspan=h, columnspan=w)
        b = Button(self, text="play again")
        b["command"] = lambda: [b.grid_forget(), l.forget(),self.randomize_puzzles(), self.show_puzzles()]
        b.grid(rowspan=h, columnspan=w) # }}}

    def get_crop(self,tx,ty):
        pic = Image.open(self.img)
        s = pic.size
        w,h = self.dimensions
        dx, dy = s[0]/w, s[1]/h
        return pic.crop((tx*dx,ty*dy,(tx+1)*dx,(ty+1)*dy))

if __name__ == '__main__':
    p = Puzzle()
    p.mainloop()
