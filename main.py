from tkinter import Tk,Button,Label
from sudoku import Sudoku
from 

class Menu(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.display_menu()

    def display_menu(self):
        apps = [Sudoku]
        for i,app in enumerate(apps):
            b = Button(self)
            b["command"] = lambda: self.launch_app(app)
            Label(self, text=app.__name__).grid(row=0,column=i)
            b.grid(row=1, column=i)

    def launch_app(self, app):
        if app.__name__ == 'Sudoku':
            self.destroy()
            s = app()
            s.mainloop()

if __name__ == '__main__':
    m = Menu()
    m.mainloop()
