import random
from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.hour = self.get_time()
        self.display_bit_clock()
        self.text_places()

    def sprawdz(self):
        t = ''.join([str(int(t.get()[0])) if t.get() != '' else str(0) for t in self.texts])
        if t==self.hour[0].replace(":",""):
            l = Label(self, text="Congratulations!", fg="#99aa00", bg="#990000")
        else:
            l = Label(self, text="Try again", fg="#55aa00", bg="#aa0000")
        l.grid(row=self.size()[1], column=0, columnspan=self.size()[0])
        print(t)
        print(self.hour[0].replace(":", ""))

    def text_places(self):
        x,y = self.size() # x (width), y (height)
        #for i in range(x):
        self.texts = [Entry(self, width=2 ) for i in range(x)]
        [t.grid(column=i, row=y) for i, t in tuple(zip(list(range(x)),self.texts))]
        b = Button(self, text="sprawdz odp", command=self.sprawdz)
        b.grid(row=y+1, column=0, columnspan=x)

    def display_bit_clock(self):
        Label(self, text=self.hour[0]).grid(row=0, column=0, columnspan=6)
        for i, line in enumerate(self.hour[1]):
            for j, col in enumerate(line):
                if int(col): 
                    l = Label(self, text=col, bd=8, fg="white", bg="black")
                else: 
                    Label(self, text=col, bd=8, bg="black").grid(row=j+1, column=i)
                    l = Label(self, text=col, bd=3)
                l.grid(row=j+1, column=i)


    def get_time(self):
        s = [str(random.randrange(1, n+1)).zfill(2) for n in [12,60,60]]
        t, s = [sepa.join(s) for sepa in [":", ""]]
        s = [bin(int(n1))[2:].zfill(n2) for n1, n2 in tuple(zip(s, [2,4,3,4,3,4]))]
        return t,s

if __name__ == '__main__':
    a = App()
    a.mainloop()
