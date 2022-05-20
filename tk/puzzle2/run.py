from tkinter import Tk, Button,Label
from random import shuffle

class Puzzle(Tk):
    def __init__(self, img='', dimensions='2x2'):
        Tk.__init__(self)
        self.dimensions = dimensions.split('x')
        self.randomize_puzzles()
        self.moves = 1
        self.selected = []
        self.show_puzzles()

    def randomize_puzzles(self):  # {{{
        w,h = list(map(int, self.dimensions))
        self.correct_puzzles = [[Button(self, text=f"{x},{y}") for x in range(w)] for y in range(h)]
        print(self.correct_puzzles)
        self.puzzles = []
        for line in self.correct_puzzles:
            self.puzzles += line
        shuffle(self.puzzles)
        self.puzzles = [self.puzzles[y*w:(y+1)*w] for y in range(h)]
        # }}}

    def show_puzzles(self): # {{{
        for y, objs in enumerate(self.puzzles):
            for x, btn in enumerate(objs):
                btn["command"] = lambda x=x,y=y: self.swap_puzzles([x,y])
                btn.config({"bg":"#d9d9d9", "activebackground":"#ececec"})
                btn.grid(column=x, row=y) # }}}

    def swap_puzzles(self, xy):
        x,y = xy
        if self.moves % 2==0:
            x1,y1 = self.selected
            self.puzzles[y1][x1], self.puzzles[y][x]= self.puzzles[y][x], self.puzzles[y1][x1]
            self.selected = []
            self.show_puzzles()
            if self.puzzles == self.correct_puzzles:
                self.win_screen()
        else:
            self.puzzles[y][x].config(bg="yellow", activebackground="orange")
            self.selected = [x,y]
        self.moves += 1

    def win_screen(self):
        s = self.size()
        [[btn.config(state="disabled") for btn in objs] for objs in self.puzzles]
        l = Label(self, text="koniec gry")
        l.grid(row=0, rowspan=s[0], columnspan=s[1])
        b = Button(self, text="play again")
        b["command"] = lambda: [b.grid_forget(), l.forget(),self.randomize_puzzles(), self.show_puzzles()]
        b.grid(rowspan=s[1], columnspan=s[0])
    
        
if __name__ == '__main__':
    p = Puzzle()
    p.mainloop()
