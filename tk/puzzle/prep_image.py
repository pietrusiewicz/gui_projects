import PIL.Image as Image#Image
import os
from tkinter import *
from select_file import Select
from az import az

class Imager:
    def __init__(self):
        self.file_name = ''
        s = Select()
        s.mainloop()
        self.thv = s.thv
        self.file_name = s.file_name

        self.cols,self.rows = s.cols, s.rows
        self.slice_picture(self.file_name)

    def slice_picture(self, filename='img.jpeg'):
        import PIL.Image as Image
        if "pieces" not in os.listdir():
            os.mkdir('pieces')
        #print('im',filename)
        im = Image.open(filename).convert("RGB")
        w,h = im.size
        rows, cols = self.rows, self.cols
        w2,h2 = w//cols, h//rows
        for i,hi in enumerate(range(h2, h+h2, h2)):
            for j,wi in enumerate(range(w2, w+w2, w2)):
                if cols <= j or rows <= i:
                    continue
                #out = im.crop((hi-h2, wi-w2, hi, wi))#.transpose(Image.ROTATE_270)
                out = im.crop((wi-w2, hi-h2, wi, hi))#.transpose(Image.ROTATE_270)
                if out.getcolors() != None:
                    if out.getcolors()[0][1] == (0,0,0):
                        print(out.getcolors())
                        continue
                thv = self.thv#5
                if thv == 0: thv = 1
                #wthv, hthv = self.wh[0]//thv, self.wh[1]//thv
                wthv, hthv = w2//thv, h2//thv
                out.thumbnail((wthv, hthv))
                #out.save(f'pieces/{az[i]}_{az[::-1][j]}.png')
                out.save(f'pieces/{az[i]}_{j}.png')
        self.pieces = os.listdir('pieces'); self.pieces.sort()

    def shuffled_pieces(self, pzzs):
        l2 = pzzs
        __import__('random').shuffle(l2)
        return l2


