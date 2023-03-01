import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.keyboard = [['7','8','9',  '+'],
                         ['6','5','4',  '-'],
                         ['3','2','1',  '*'],
                         ['0','00','C', '/']]

    def menu(self):
        self.e = tk.Entry(self)
        self.e["xscrollcommand"]=lambda: tk.Label(self, text=f"= {eval('{{self.e.get()}}')}").grid(row=0, column=0, columnspan=4, sticky='E')
        self.e.grid(row=0, column=0, columnspan=4, sticky='W')
        for i in range(4):
            for j in range(4):
                b = tk.Button(self, text=f"{self.keyboard[i][j]}", width=3, height=2)
                b["command"] = lambda x = self.keyboard[i][j]: self.press_button(x)
                #print(b.__dir__())
                b.grid(row=i+1, column=j)

    def press_button(self, letter):
        t = self.e.get() + letter
        if letter=='C':
            self.e.delete(0, len(t))

        else:
            self.e.delete(0, len(t))
            [self.e.insert(0, let) for let in t[::-1]]

    def del_e(self):
        t = self.e.get()
        t.pop()
        self.e.delete(0, len(t))
        [self.e.insert(0, let) for let in t[::-1]]
    
    def get_result(self):
        result = eval(f"{self.e.get()}")
        tk.Label(self, text=f"= {result}").grid(row=0, column=0, columnspan=4, sticky='E')

if __name__ == '__main__':
    c = Calculator()
    c.menu()
    c.mainloop()
