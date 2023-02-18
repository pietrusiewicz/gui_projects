from tkinter import *
from args import *

_from_rgb = lambda rgb: "#%02x%02x%02x" % rgb
# Button wysiwyg editor
class Editor(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.btn = Button(self)
        keys = self.btn.keys()
        self.default_btn={key:self.btn[key] for key in keys}
        self.edit_button()
        self.btn.grid(row=0,rowspan=self.size()[1],column=2)

    def edit_button(self):
        geth3 = lambda h1, h2, h3: [print(_.get()) for _ in [h1,h2,h3]]
        def color_picker():
            v1,v2,v3 = IntVar(),IntVar(),IntVar()
            h1 = Scale(self, variable=v1, from_=0, to=255, length=17, width=15, bd=0, orient=HORIZONTAL,troughcolor='red', fg='gray')
            #h1.config(command=h1.config(bg=_from_rgb((v1.get(),0,0))))
            h2 = Scale(self, variable=v2, from_=0, to=255, length=17, width=15, bd=0, orient=HORIZONTAL,troughcolor='green', fg='gray')
            h3 = Scale(self, variable=v3, from_=0, to=255, length=20, width=15, bd=0, orient=HORIZONTAL,troughcolor='blue', fg='gray')
            h1.grid(row=0, column=0, ipadx=15, sticky=EW)
            h2.grid(row=0, column=1, ipadx=15, sticky=EW)
            h3.grid(row=0, column=2, ipadx=15, sticky=EW)
            Entry(self).grid(row=1,columnspan=3)
            b = Button(self, text='apply changes', command=lambda: geth3(h1,h2,h3))
            b.grid(row=self.size()[1], column=0, columnspan=2)
        e = []
        for i, key in enumerate(btnargs):
            Label(self, text=key).grid(row=i, column=0)
            e.append(Entry()); e[i].insert(0, str(self.default_btn[key]))
            e[i].grid(row=i, column=1)

        #b = Button(self, text='apply changes', command=lambda: [self.get_values(e), self.change_button(**self.vals)])
        #b.grid(row=self.size()[1], column=0, columnspan=2)

    def get_values(self, e):
        #self.vals = {k:e[i].get() for (i,k) in enumerate(list(self.btn.keys()))}
        self.vals = {k:e[i].get() for (i,k) in enumerate(btnargs)}

    def change_button(self, **kwargs):
        self.btn.config(**kwargs)


if __name__ == '__main__':
    e = Editor()
    e.mainloop()
