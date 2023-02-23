import tkinter as tk

class Todolist(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.items = {}

    def menu(self):
        #print("Items:")
        for i, items in enumerate(self.items.items()):
            item, done = items
            btn_color = "green" if done else "red"

            l_item = tk.Label(self, text=f"'{i}) {item}'")
            btn_mark = tk.Button(self, text=" ", bg=btn_color, command=lambda x=i : self.mark_item(x))
            btn_delete = tk.Button(self, text="-")

            l_item.grid(row=i, column=0)
            btn_mark.grid(row=i, column=1)
            btn_delete.grid(row=i, column=2)

        self.e = tk.Entry()
        btn_add = tk.Button(self, text="+", command=self.add_item)

        nrow = len(self.items)
        self.e.grid(row=nrow, column=0)
        btn_add.grid(row=nrow, column=1)
        #select = int(input("1) Add Item 2) Delete Item 3) Mark Item *) Exit\n"))
        """
        if select == 1:
            self.add_item()

        elif select == 2:
            key = self.get_key()
            del self.items[key]

        elif select == 3:
            key = self.get_key()
            self.items[key] = not bool(self.items[key])
        """

    def add_item(self):
        self.items[self.e.get()] = False
        self.menu()

    def del_item(self, n):
        key = self.get_key(n)
        del self.items[key]

    def mark_item(self, n):
        key = self.get_key(n)
        self.items[key] = not bool(self.items[key])
        self.menu()


    def get_key(self, n):
        return list(self.items)[n]




if __name__ == "__main__":
    t = Todolist()
    t.menu()
    t.mainloop()
    
