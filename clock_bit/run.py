import time
from tkinter import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.hour = self.get_time()
        self.display_bit_clock()


    def display_bit_clock(self):
        Label(self, text=self.hour).grid(row=0, column=0, columnspan=6)
        for i, line in enumerate(self.hour):
            for j, col in enumerate(line):
                if int(col): 
                    l = Label(self, text=col, bd=8, fg="white", bg="black")
                else: 
                    Label(self, text=col, bd=8, bg="black").grid(row=j+1, column=i)
                    l = Label(self, text=col, bd=3)
                l.grid(row=j+1, column=i)


    def get_time(self):
        s = "".join(time.strftime("%H:%M:%S").split(":"))
        print(s)
        return [bin(int(n1))[2:].zfill(n2) for n1, n2 in tuple(zip(s, [2,4,3,4,3,4]))]

if __name__ == '__main__':
    a = App()
    a.mainloop()
