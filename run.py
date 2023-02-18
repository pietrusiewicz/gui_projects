class Todolist:
    def __init__(self):
        self.items = {}
        self.menu()

    def menu(self):
        print("Items:")
        for item, done in self.items():
            print(f"\n\t{item}: {done}")
