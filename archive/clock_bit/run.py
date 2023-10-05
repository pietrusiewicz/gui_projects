import time
from tkinter import Tk, Label
from threading import Thread


#class App(Tk):
class App():
    def __init__(self, master):
        self.m = master
        #Tk.__init__(self)
        self.display_bit_clock()
        t1 = Thread(target=self.work)
        t1.start()

    # display digit clock
    def display_bit_clock(self):
        "display one or zero"
        # get current time
        s = time.strftime("%H:%M:%S")
        Label(self.m, text=s).grid(row=0, column=0, columnspan=6)
        # get []
        s = [list(map(lambda x: bin(int(x.split()[0]))[2:], e.split()[0])) for e in s.split(":")]

        # convert s to array
        l = [] # {{{
        for arr in s:
            l += arr # }}}

        # place Labels with spaces
        [[Label(self.m, text=" ",fg="#ececec", bg="#d2d2d2", bd=8).grid(row=y+1, column=x) for x in range(6)] for y in range(4)]

        # place one or zero value
        for i,bins in enumerate(l): # {{{
            # ['1','100']
            for j,num in enumerate(bins):
                if int(num): 
                    l = Label(self.m, text=num, bd=8, fg="white", bg="black")
                else:
                    l = Label(self.m, text=num, bd=8, fg="black", bg="white")
                l.grid(row=j+1, column=i) # }}}


    # execute sleep command in tkinter
    def work(self):
        "example of sleep command while tkinter program"
        while True:
            time.sleep(1)
            self.display_bit_clock()

if __name__ == '__main__':
    r = Tk()
    a = App(r)
    r.mainloop()
