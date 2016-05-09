from Tkinter import *
import Tkinter as Tk
from PIL import Image, ImageTk
import os,glob


class Body(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 0, 0, outline="#06617C", fill="#06617C")
        canvas.pack(fill=BOTH, expand=1)
        im = Image.open('/home/venkat/bg.png')
        bgimage = ImageTk.PhotoImage(im)
        canvas.img = bgimage
        canvas.create_image(0, 0, anchor=NW, image=bgimage)
        self.showresults()

    def showresults(self):
        c = 0
        r = 10
        path = '/home/venkat/CBIR/queries/'
        for imagePath in glob.glob(path+"*.png"):
            path1 = Image.open(imagePath)
            path1 = path1.resize((100, 100), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(path1)
            myvar = Label(self.parent,image=img1)
            myvar.image = img1
            myvar.place(x=c+30, y=r+10)
            c += 110
            if (c%1320==0):
                r += 110
                c=0


def main():
    root = Tk.Tk()
    #root.configure(background='cyan')
    root.resizable(width=True, height=True)
    # head = Header(root)

    root.geometry('{}x{}'.format(1400, 770))
    root.title("Content Based Image Retrieval -- show dataset")  # setting up title of window
    # root.iconbitmap(bitmap='/home/venkat/images/logo.ico')						#setting up logo of window
    body = Body(root)
    root.mainloop()


if __name__ == '__main__':
    main()
