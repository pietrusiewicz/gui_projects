import tkinter as tk

try:
    from todolist import Todolist
except ImportError:
    from .todolist import Todolist 


class TodoListGui(Todolist):
    def __init__(self, master):
        self.m = master
        print(type(self.m))
        Todolist.__init__(self)
        #tk.Tk.__init__(self)
        #self.items = Todolist().items 

    def menu(self):
        self.refresh()
        btn_add = tk.Button(self.m, text="+") 
        btn_add["command"]=lambda: self.wrapper(self.add_item, self.e.get())
        for i, items in enumerate(self.items.items()):
            item, done = items
            btn_color = "green" if done else "red"

            l_item = tk.Label(self.m, text=f"'{i}) {item}'")
            btn_mark, btn_delete = [tk.Button(self.m, text=letter) for letter in " -"]
            btn_mark["command"]=lambda x=i : self.wrapper(self.mark_item, x)
            btn_mark["bg"] = btn_color

            btn_delete["command"]=lambda x=i: self.wrapper(self.del_item, x)

            for j,f in enumerate([l_item, btn_mark, btn_delete]):
                f.grid(row=i, column=j)
            """
            l_item.grid(row=i, column=0)
            btn_mark.grid(row=i, column=1)
            btn_delete.grid(row=i, column=2)
            """

        self.e = tk.Entry()

        nrow = len(self.items)
        self.e.grid(row=nrow, column=0)
        btn_add.grid(row=nrow, column=1)
        print(self.items)

    def wrapper(self, func, x):
        func(x)
        self.menu()

    def refresh(self):
        print(type(self.m))
        try:
            widgets = self.m.winfo_children()
            for widget in widgets:
                widget.destroy()
        except:
            pass


if __name__ == "__main__":
    r = tk.Tk()
    t = TodoListGui(r)
    t.menu()
    r.mainloop()
    
