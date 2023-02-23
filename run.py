class Todolist:
    def __init__(self):
        self.items = {}

    def menu(self):
        print("Items:")
        for i, items in enumerate(self.items.items()):
            item, done = items
            print(f"\t'{i}) {item}': {done}")
        select = int(input("1) Add Item 2) Delete Item 3) Mark Item *) Exit\n"))
        if select == 1:
            self.items[self.add_item()] = False
        elif select == 2:
            """
            n = int(input("number of item: "))
            key = list(self.items)[n]
            """
            key = self.get_key()
            del self.items[key]
        elif select == 3:
            """
            n = int(input("number of item: "))
            key = list(self.items)[n]
            """
            key = self.get_key()
            self.items[key] = not bool(self.items[key])
            """
            if self.items[key]:
                self.items[key] = False
            else:
                self.items[key] = True
            """
        self.menu()

    def get_key(self):
        return list(self.items)[int(input("number of item: "))]

    def add_item(self):
        return input("Name item: ")


if __name__ == "__main__":
    t = Todolist()
    t.menu()
    
