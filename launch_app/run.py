from tkinter import *
from json_class import File#save_file, get_apps, del_app, add_app



class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.keys = ['app_name', 'path_name', 'start_hour_access', 'cooldown_hours'] 
        self.myfyds = [self.append_mode, self.launch_mode]
        self.apps = p.get_apps()

        # display buttons
        for j, txt in enumerate(self.myfyds):
            b = Button(self, text=txt.__name__, command=lambda j=j: [txt(), self.clicked(j)])
            b.grid(column=j, row=0)


    def append_mode(self):
        happs = []
        for i, header in enumerate(self.keys):
            Label(self, text=header).grid(column=i, row=1)

        for i, app in enumerate(self.apps):
            # display row values
            for col_num, key in enumerate(self.keys):
                val = app[str(i)][key]
                e = Entry()
                e.insert(0, val)
                e.configure(state=DISABLED, disabledbackground='#dfefef', disabledforeground='#0f0f0f')
                e.grid(column=col_num, row=i+2)

            b = Button(self, text=' - ', command=lambda i=i: [p.del_app(i), self.append_mode()])
            b.grid(column=4, row=i+2)

        r = len(self.apps)+2

        l = [Entry(bd=4) for _ in range(4)]
        [e.grid(column=i, row=r) for i, e in enumerate(l)]
            
        b = Button(self, text="+", command=lambda: [p.valid_data([l[0].get(), l[1].get(), l[2].get(), l[3].get()]), self.append_mode()])
        b.grid(column=4, row=r)


    def launch_mode(self):
        for i, app in enumerate(self.apps):
            lbl = Label(self, text=f"run {app[str(i)]['app_name']}")
            lbl.grid(row=i+1,column=0)
            b = Button(self, text='launch', command=lambda i=i: __import__('os').system(f"{app[str(i)]['path_name']}"))
            b.grid(row=i+1, column=1)


    def clicked(self, i):
        self.destroy()
        self.__init__()
        b = Button(self, text=self.myfyds[i].__name__, state=DISABLED)
        self.myfyds[i]()
        b.grid(row=0, column=i)



if __name__ == '__main__':
    p = File()
    a = App()
    a.mainloop()


