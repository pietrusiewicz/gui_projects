from tkinter import *

class App1(Tk):
    def __init__(self):
        Tk.__init__(self)


class App2(App1):
    def __init__(self, cVals=[0,0,0], vals=['-99','-25','-5','+5','+25','+99']):
        App1.__init__(self)
        self._from_rgb = lambda rgb : "#%02x%02x%02x" % rgb
        self.cVals, self.vals = cVals, vals
        self.grid_buttons()
        
    def grid_buttons(self):
        after_add = lambda: self.shuffle_buttons()
        for i, color in enumerate(['red', 'green', 'blue']):
            for j, val in enumerate(self.vals):
                b = Button(self, bg=color, fg='white', text=val.zfill(3), command=lambda i=i, val=val: self.add_val(i, int(val)))
                b.grid(row=i+1, column=j)
        shuffle_button = Button(self, command=after_add, text='shuffle_buttons')
        shuffle_button.grid(row=0, columnspan=6)

    def shuffle_buttons(self):
        #vals = ['-99','-25','-5','+5','+25','+99']
        l0 = [[-99, -25, -5, 0, 5, 25],[-25, -5, 0, 5, 25, 99]]
        l = tuple(zip(l0[0], l0[1]))
        randomvals = lambda : [repr(__import__('random').randrange(i[0], i[1])).zfill(3) for i in l]
        valerian = lambda c: [f"{c}{val[1:]}" for val in randomvals()]
        val_full = lambda: valerian('-')[:3] + valerian('+')[3:]
        self.vals = val_full()
        self.grid_buttons()


    def add_val(self, i, sVal):
        if (self.cVals[i] + sVal) > 255 or (self.cVals[i]+sVal < 0):
            pass
        else:
            self.cVals[i] += sVal
        rvh = [itr for itr in self.cVals]
        rvh = self._from_rgb((rvh[0],rvh[1],rvh[2]))
        lbl = Label(self, text=rvh, bg=rvh, fg='white')
        lbl.grid(row=4,column=0,columnspan=3)
        print(self.cVals)
        bc = Button(self, text="copy to clipboard", command=lambda: self.copy(rvh))
        bc.grid(row=4, column=3, columnspan=8)

    def copy(self, heks):
        self.clipboard_clear()
        self.clipboard_append(heks)
        self.update()



if __name__ == '__main__':
    a = App2()
    a.mainloop()


