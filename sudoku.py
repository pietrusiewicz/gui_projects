from tkinter import Tk, Button, Text
from threading import Thread
import time
from collections import Counter

class Sudoku(Tk):
    def __init__(self):
        Tk.__init__(self)

        # array represents str' nums
        self.nums = list(map( lambda x: str(x), list(range(1, 10)) ))

        # place array of Button objects what converts to Text
        self.squares = [[Button(self, width=0, height=0, command=lambda x=x,y=y: self.click(x,y)) for x in range(9)] for y in range(9)]
        self.place_squares()

        # check positions correct places
        t1 = Thread(target=self.check_win)
        t1.start()

    # place squares in board
    def place_squares(self): # {{{
        for y in range(9):
            for x in range(9):
                self.squares[y][x].grid(row=y, column=x) # }}}

    # clicked button
    def click(self, x,y): # {{{
        "change Button to Text"
        self.squares[y][x] = Text(self, width=2, height=1,bd=4)
        self.squares[y][x].grid(row=y, column=x) # }}}

    # game process
    def check_win(self): # {{{
        "function is executing while game"
        while True:
            # coloring groups
            self.check_correct_groups()
            time.sleep(1)
            for y in range(9):
                for x in range(9):
                    obj = self.squares[y][x]

                    # check correctness of tag square
                    if type(obj) == Button:
                        continue

                    # correcting Text value
                    t = obj.get('1.0','end').strip() #{{{
                    if len(t) > 0:
                        obj.delete('1.0', 'end')
                        if t[:1] in self.nums:
                            obj.insert('1.0', t[:1])  #}}}

            if self.is_end():
                self.end_scene() # }}}

    # check correct rows position 
    def check_correct_rows(self): # {{{
        for i in range(9):
            c = Counter()
            # row hasn't filled
            if len(set(self.squares[i])) != 9:
                break
            #if len(set(self.squares[i])) == 9:
            for j in range(9):
                t = self.squares[i][j]
                if type(t) != Text:
                    break
                # get Text value
                t = t.get('1.0','end')[:1].strip()
                #c.add(t)
                # add to Counter dict
                c[t] += 1

            # rows hasn't filled
            if sorted(list(c)) != self.nums:
                return False
        return True # }}}

    # check correct cols position 
    def check_correct_cols(self): # {{{
        #c = Counter()
        for i in range(9):
            c = Counter()
            # when row hasn't filled
            if len(self.squares[i]) != 9:
                break
            #if len(self.squares[i]) == 9:
            for j in range(9):
                t = self.squares[j][i]
                if type(t) != Text:
                    break
                #if type(t) == Text:
                t = t.get('1.0','end')[:1]
                c[t] += 1

            # check column repeatness
            if sorted(list(c)) != self.nums:
                return False
        return True # }}}

    """ 
    def check_correct_cols_n_rows(self): # {{{
        #c = Counter()
        for k in range(2):
            c = Counter()
            for i in range(9):
                if len(self.squares[i]) == 9:
                    for j in range(9):
                        #for t in [self.squares[j][i], self.squares[i][j]]:
                        t = self.squares[j][i] if k==0 else self.squares[i][j]
                        #t = self.squares[j][i]
                        if type(t) != Text:
                            break
                        #if type(t) == Text:
                        t = t.get('1.0','end')[:1]
                        c[t] += 1
                        if sorted(list(c)) != self.nums:
                            return False
            return True # }}}
    """ 

    # check correct groups position 
    def check_correct_groups(self): # {{{
        g = [[],[],[], [],[],[], [],[],[]]

        # first three rows
        for elem in self.squares[:3]:
            # 3 groups divided inside rows
            for i in range(3):
                # add one group to array
                g[i] += elem[i*3:(i+1)*3]

        # second three rows
        for elem in self.squares[3:6]:
            # 3 groups divided inside rows
            for i in range(3):
                # add one group to array
                g[i+3] += elem[i*3:(i+1)*3]
        
        # third three rows
        for elem in self.squares[6:9]:
            # 3 groups divided inside rows
            for i in range(3):
                # add one group to array
                g[i+6] += elem[i*3:(i+1)*3]

        for i in range(len(g)):
            if i%2:
                for item in g[i]:
                    item["bg"]="black"
                    item["fg"]="white"

        for i in range(9):
            c = Counter()

            if len(self.squares[i]) == 9:
                for j in range(9):
                    t = g[i][j]
                    if type(t) != Text:
                        break
                    t = t.get('1.0','end')[:1]
                    c[t] += 1

                if sorted(list(c)) != self.nums:
                    return False
            
        return True # }}}

    # check end of game
    def is_end(self): # {{{
        "check three condition of end sudoku"
        # check function in 125 line
        if not self.check_correct_groups():
            return False
        # check function in 82 line
        if not self.check_correct_cols():
            return False
        # check function in 59 line
        if not self.check_correct_rows():
            return False
        return True # }}}

    # scene of end
    def end_scene(self):
        "not working XDD"
        for i in range(9):
            for j in range(9):
                # it doesn't disable this text object
                self.squares[i][j]["state"] = "disabled"


if __name__ == '__main__':
    s = Sudoku()
    s.mainloop()
