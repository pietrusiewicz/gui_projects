import tkinter as tk

class MindMap:
    def __init__(self, master):
        self.m = master
        self.m.geometry("1280x720")
        self.tree = {}


    def display_tree(self):
        main_btn = tk.Button(self.m, text="glowna_mysl", command=self.enter_value)
        main_btn.place(x=640, y=360)
    

    def enter_value(self):
        e=tk.Entry(self.m)
        e.place(x=640, y=360)


if __name__ == '__main__':
    r = tk.Tk()
    m = MindMap(r)
    m.display_tree()
    r.mainloop()
