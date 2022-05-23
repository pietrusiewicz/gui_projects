from tkinter import Entry, Tk, Button, Label
from database import Database

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.d = Database()
        self.get_tasks()#self.d.get_tasks()
        print(self.tasks)
        self.display_tasks()

    def get_tasks(self):
        self.tasks = self.d.get_tasks()
        self.tasks= {} if self.tasks==None else self.tasks

    def display_tasks(self):
        [el.destroy() for el in self.grid_slaves()]
        for i, task in enumerate(self.tasks):
            e = Entry(self)
            e.grid(row=i, column=1)
            e.insert(0, task)
            e['state']='disabled'
            e['disabledforeground']="#224"

            c1 = Button(self, text=self.tasks[task], command=lambda t=task: self.adpm(3,t))
            c1.grid(row=i, column=2)
            c2 = Button(self, text="-1", command=lambda t=task: self.adpm(4,t))
            c2.grid(row=i, column=3)

            b1 = Button(self, text="-", command=lambda t=task: self.adpm(2,t))
            b1.grid(row=i, column=0)

        e = Entry(self)
        rowe = self.size()[1]
        e.grid(row=rowe, column=1)
        b2 = Button(self, text="+", command=lambda: self.adpm(1,e.get()))
        b2.grid(row=rowe, column=0)

    # add, del, plus, minus
    def adpm(self, c, task):
        if c == 1:
            self.d.add_task(task)
        if c == 2:
            self.d.del_task(task)
        if c == 3:
            self.d.plus_one(task)
        if c == 4:
            self.d.minus_one(task)
        self.tasks = self.d.get_tasks()
        self.display_tasks()

if '__main__' == __name__:
    a = App()
    a.mainloop()
