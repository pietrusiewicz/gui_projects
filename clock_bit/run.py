import time
from tkinter import Tk, Label
from threading import Thread


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
        l = []
        for arr in s:
            l += arr
        [[Label(self, text=" ",fg="#ececec", bg="#d2d2d2", bd=8).grid(row=y+1, column=x) for x in range(6)] for y in range(4)]
        # ['1','100','1100', '111']
        for i,bins in enumerate(l):
            # ['1','100']
            for j,num in enumerate(bins):
                if int(num): 
                    l = Label(self, text=num, bd=8, fg="white", bg="black")
                else:
                    l = Label(self, text=num, bd=8, fg="black", bg="white")
                l.grid(row=j+1, column=i)
        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        time.sleep(1)
        self.display_bit_clock()

if __name__ == '__main__':
    a = App()
    a.mainloop()
