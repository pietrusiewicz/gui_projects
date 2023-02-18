class Todolist:
    def __init__(self):
        self.items = {}

    def menu(self):
        print("Items:")
        for item, done in self.items.items():
            print(f"\t'{item}': {done}")
        select = int(input("1) Add Item 2) Delete Item 3) Mark Item *) Exit\n"))
        if select == 1:
            self.items[input("Name item: ")] = False
        elif select == 2:
            n = int(input("number of item: "))
            del self.items[list(self.items[n])]
        elif select == 3:
            n = int(input("number of item: "))
            self.items[list(self.items[n])] = not bool(self.items[list(self.items[n])])
        self.menu()

if __name__ == "__main__":
    t = Todolist()
    t.menu()
    
