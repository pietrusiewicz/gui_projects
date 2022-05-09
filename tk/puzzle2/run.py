from tkinter import Tk, Button

class Puzzle(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.show_label()

    def show_label(self):
        Button(self, text="bedzie dobrze").pack()

if __name__ == '__main__':
    p = Puzzle()
    p.mainloop()
