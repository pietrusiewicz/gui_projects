import time
from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.display_bit_clock()


    def display_bit_clock(self):
        # get current time
        s = time.strftime("%H:%M:%S")
        Label(self, text=s).grid(row=0, column=0, columnspan=6)
        # get []
        s = [list(map(lambda x: bin(int(x.split()[0]))[2:], e.split()[0])) for e in s.split(":")]
        print(s)
        s = []
        i = 0
        # [['1','100'],['1100', '111']]
        for bins in s:
            print(bins)
            #digit = list(map(lambda x: int(x.split()[0]), digit))
            #for j, bins in enumerate(list(map(lambda x: bin(x)[2:], digit))):
            # ['1','100']
            j = 0
            for num in bins:
                if int(num): 
                    l = Label(self, text=num, bd=8, fg="white", bg="black")
                else:
                    print(0)
                    l = Label(self, text=num, bd=8, fg="black", bg="white")
                l.grid(row=j+1, column=i)
                j+=1
            i+=1

        """
        for i, line in enumerate(self.hour):
            for j, col in enumerate(line):
                if int(col): 
                    l = Label(self, text=col, bd=8, fg="white", bg="black")
                else: 
                    Label(self, text=col, bd=8, bg="black").grid(row=j+1, column=i)
                    l = Label(self, text=col, bd=3)
                l.grid(row=j+1, column=i)
        """

if __name__ == '__main__':
    a = App()
    a.mainloop()
