from tkinter import *


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        #self.board = board
        self.board = [['','',''], ['','',''], ['','','']]
        #self.xo = xo
        self.xo = 'X'
        self.grid_buttons()
        self.moves = []

    def grid_buttons(self):
        for i, line in enumerate(self.board):
            for j, val in enumerate(line):
                n = j + i*3
                if val == 'X':
                    b = Button(self, text=val, height=5, width=5, bg='#f00')
                if val == 'O':
                    b = Button(self, text=val, height=5, width=5, bg='#00f', fg='#fff')
                if val not in ('O','X'):
                    b = Button(self, text=val, height=5, width=5, command=lambda n=n: self.place_x_or_o(n, self.xo))
                b.grid(row=i, column=j)

    
    def place_x_or_o(self, place, xo):
        if place not in self.moves:
            self.moves.append(place)
            #print('wykonuje sie', place, xo)
            for y, line in enumerate(self.board):
               for x, val in enumerate(line):
                    n = x + y*3
                    if n == place:
                        self.board[y][x] = xo
            chxo = lambda n: 'O' if n == 'X' else 'X'
            self.xo = chxo(xo)
            self.grid_buttons()
            self.win_condition(chxo(self.xo))
        else:
            pass
 
    def win_condition(self, xo):
        brd = self.board
        for i in range(len(self.board)):
            if brd[0][i] == brd[1][i] == brd[2][i] and brd[0][i]!='':
                self.win_show(xo, [[0, i],[1, i],[2, i]])
            if brd[i][0] == brd[i][1] == brd[i][2] and brd[i][0]!='':
                self.win_show(xo, [[i, 0],[i, 1],[i, 2]])
            if brd[1][1] != '':
                if brd[0][0] == brd[1][1] == brd[2][2]:
                    self.win_show(xo, [[0, 0],[1, 1],[2, 2]])
                if brd[0][2] == brd[1][1] == brd[2][0]:
                    self.win_show(xo, [[0, 2],[1, 1],[2, 0]])

    def win_show(self, o, places):
        Label(self, text=f"{o} won a game").grid(columnspan=3, row=4)
        for i, line in enumerate(self.board):
            for j, val in enumerate(line):
                if [i,j] in places:
                    b = Button(self, height=5, width=5, bg='#ee00ee', state=DISABLED, text=val)
                #n = j + i*3
                else:
                    b = Button(self, height=5, width=5, state=DISABLED, text=val)
                b.grid(row=i, column=j)
        Button(self, text='play again',command=lambda: [self.destroy(), self.__init__()]).grid(row=5, columnspan=3)



if __name__ == '__main__':
    g = Game()
    g.mainloop()
