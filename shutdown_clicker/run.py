from tkinter import Tk, Button
import time
from threading import Thread

class Program(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.dest_time = time.time()+200
        self.display_button()

    def display_button(self):
        self.b = Button(self, command=self.click, bd=3, width=10)
        self.b.grid(row=0, column=0)

        # time to execute command
        diff = int(self.dest_time-time.time())

        self.b["text"] = f"{diff}"
        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        time.sleep(0.6)
        if time.time() >= self.dest_time:
            print("hello world")
        self.display_button()

    def click(self):
        self.dest_time += 1

if __name__ == '__main__':
    p = Program()
    p.mainloop()
