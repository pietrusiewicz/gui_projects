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
            self.add_item(input("Name item: "))

        elif select == 2:
            key = self.get_key(int(input("number of item: ")))
            self.del_item(key)

        elif select == 3:
            key = self.get_key(int(input("number of item: ")))
            self.items[key] = not bool(self.items[key])

        self.menu()

    def get_key(self, index):
        return list(self.items)[index]

    def add_item(self, key):
        self.items[key] = False

    def del_item(self, index):
        key = self.get_key(index)
        del self.items[key]

    def mark_item(self, index):
        key = self.get_key(index)
        self.items[key] = not bool(self.items[key])


if __name__ == "__main__":
    t = Todolist()
    t.menu()

