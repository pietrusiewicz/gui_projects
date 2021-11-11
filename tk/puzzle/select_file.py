from tkinter import *
from tkinter.filedialog import askopenfilename
from shutil import copyfile
import os

class Select(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.r = IntVar()
        try:
            self.ls = os.listdir('imgs')
            for i, f in enumerate(self.ls):
                Radiobutton(self, text=f, variable=self.r, value=i).grid(row=i)
                print(self.size())
            b2 = Button(self, text='+', command=self.add)
            self.tc = Text(self, width=3, height=1); self.tc.insert(INSERT, 5)
            self.tr = Text(self, width=3, height=1); self.tr.insert(INSERT, 5)
            b1 = Button(self, text='=>', command=self.forward)

            b2.grid(row=0, rowspan=self.size()[1],column=1)
            Label(self, text='num of cols').grid(row=self.size()[1], column=0)
            Label(self, text='num of rows').grid(row=self.size()[1], column=0)
            self.tc.grid(row=self.size()[1]-2, column=1)
            self.tr.grid(row=self.size()[1]-1, column=1)
            b1.grid(row=self.size()[1],column=0)
        except FileNotFoundError:
            os.mkdir('imgs')
            self.destroy()
            self.select_filename()

    def add(self):
        filename = askopenfilename()
        pwd_filename = os.getcwd()+'/imgs/'+filename.split('/')[-1]
        copyfile(filename, pwd_filename)
        self.destroy()
        self.__init__()

    def forward(self):
        i = self.r.get()
        # zmienne które idą dalej
        self.file_name = 'imgs/'+self.ls[i]
        w,h = (self.winfo_screenwidth(), self.winfo_screenheight())
        self.wh = (self.winfo_screenwidth(), self.winfo_screenheight())
        w2,h2 = __import__('PIL').Image.open(self.file_name).size
        self.thv = sum([w2//w, h2//h])
        self.cols, self.rows = int(self.tc.get('1.0', END)), int(self.tr.get('1.0', END))

        print(w,h)
        print(w2,h2)
        self.destroy()

