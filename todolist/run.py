from tkinter import Tk, Label, Button, Entry

class Todolist(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.items = {'kowno':1, 'mixtape':0}
        self.display_items()

    def display_items(self):
        for widget in self.winfo_children():
            widget.destroy()
        for y, item in enumerate(self.items.keys()):
            Label(self).grid(row=y, column=0)
            b1 = Button(self, text=item, bg="red", bd=4, width=50)
            b1["command"] = lambda item=item: self.change_item(item)
            b1.grid(row=y, column=0)
            b2 = Button(self, text='-')
            b2["command"] = lambda item=item: self.delete_item(item)
            if self.items[item]:
                b1['bg']="green"
            b2.grid(row=y, column=1)
        e = Entry()
        e.grid(row=len(self.items), column=0)
        b = Button(self, text="+", command=lambda: self.change_item(e.get()))
        b.grid(row=len(self.items), column=1)

    def change_item(self, it):
        self.items[it] = False if it not in self.items else not self.items[it]
        self.display_items()

    def delete_item(self, it):
        del self.items[it]
        self.display_items()

if __name__ == '__main__':
    t = Todolist()
    t.mainloop()
