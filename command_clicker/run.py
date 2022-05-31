from tkinter import Tk, Button
import time
from threading import Thread
from sys import argv, exit
from os import system

class Program(Tk):
    def __init__(self):
        Tk.__init__(self)
        # own command if given, default poweroffs
        self.command = ''.join(argv[1:]) if len(argv) > 1 else "systemctl poweroff"
        self.dest_time = time.time()+200
        self.display_button()

    def display_button(self):
        # declare a button
        self.b = Button(self, command=self.click, bd=3, width=10)
        self.b.grid(row=0, column=0)

        # place text in self.b (16 line)
        self.b["text"] = f"{self.diff()}"
        t1 = Thread(target=self.work)
        t1.start()

    def work(self):
        time.sleep(0.6)
        # when difference is equal or less zero
        if self.diff() <= 0:
            # execution of commsnd
            system(self.command)
            self.end_sequence()
        self.display_button()

    def click(self):
        self.dest_time += 4

    # time to execute command
    def diff(self):
        return int(self.dest_time-time.time())

    def end_sequence(self):
        self.destroy()
        exit()
if __name__ == '__main__':
    p = Program()
    p.mainloop()
