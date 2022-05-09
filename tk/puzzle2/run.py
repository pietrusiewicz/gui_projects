from tkinter import Tk, Label

class Puzzle(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.show_label()

    def show_label(self):
        Label(self, text="bedzie dobrze").pack()

if __name__ == '__main__':
    p = Puzzle()
    p.mainloop()
