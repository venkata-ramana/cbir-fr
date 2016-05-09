from Tkinter import *
import Tkinter as Tk
from PIL import Image, ImageTk
import search as searcher
from tkFileDialog import *
import index, os
import tkMessageBox as tkm

class Body(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def callback(self):
        choosenfile = askopenfilename(parent=self.parent)
        dp.destroy()
        # if(choosenfile):
        #     input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Sit back and relax we are seaching most similer results for, we will get back to you once we completed our search.')
        #     input_img_label.place(x=20, y=150)
        inputimage=choosenfile
        choosenfile = choosenfile.split('/')
        choosenfile = choosenfile[::-1]
        choosenfile = choosenfile[1] + '/' + choosenfile[0]
        if not choosenfile.endswith('png') | choosenfile.endswith('.jpg'):
             tkm.showinfo('Error Message','Please choose image file only.')
        results = searcher.callback(choosenfile)
        self.showresults(results,inputimage)

    def indexit(self):
        self.indexer._name = 'Please wait indexing...'
        count=index.indexer()
        if(count==0):
            tkm.showinfo('Error Message','Folder is empty, please add images into dataset to index.')
        else:
            tkm.showinfo('Index Status','Successfully Indexed '+str(count)+' images.')

    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 0, 0, outline="#06617C", fill="#06617C")
        canvas.pack(fill=BOTH, expand=1)

        im = Image.open(path+'/bg.png')
        bgimage = ImageTk.PhotoImage(im)
        canvas.img = bgimage
        canvas.create_image(0, 0, anchor=NW, image=bgimage)

        self.indexer = Button(canvas, text='Index dataset', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.indexit)
        self.indexer.pack()
        canvas.create_window(500, 100, window=self.indexer)

        widget = Button(canvas, text='Upload file..!', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.callback)
        widget.pack()
        canvas.create_window(700, 100, window=widget)

    def showresults(self, results, input):
        path1 = Image.open(input)
        path1 = path1.resize((200, 150), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(path1)
        input_img_label = Label(self.parent, image=img1)
        input_img_label.image = img1
        input_img_label.place(x=600, y=20)

        input_img_label = Label(self.parent, font=('calibri',14),bg='#fff',fg='black', text='showing results for above query...')
        input_img_label.place(x=550, y=180)

        query = Button(self.parent, text='Upload another file..!', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.callback)
        query.place(x=395,y=120)
        c = 0
        r = 240
        for (score, resultID) in results:
            # load the result image and display it
            i = 0
            total = 105
            perc = int(score)
            while (i <= perc):
                total -= 5
                i += 1

            # print "Image " + resultID + " got " + str(total) + "% similarity and " + '%2.3f' % score + " score.."
            path1 = Image.open(path+"/dataset/" + resultID)
            path1 = path1.resize((250, 200), Image.ANTIALIAS)
            img1 = ImageTk.PhotoImage(path1)
            myvar = Label(self.parent,image=img1)
            myvar.image = img1
            myvar.place(x=c+30, y=r)
            output_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text=str(total)+'% match...'+'%2.3f dist' % score)
            output_img_label.place(x=c+30, y=r+205)
            c += 265
            if (c == 1325):
                r += 235
                c=0


root = Tk.Tk()
    #root.configure(background='cyan')
root.resizable(width=True, height=True)
path = os.getcwd()
root.geometry('{}x{}'.format(1400, 770))
root.title("Content Based Image Retrieval")  # setting up title of window
    # root.iconbitmap(bitmap='/home/venkat/images/logo.ico')						#setting up logo of window
body = Body(root)
im1 = Image.open(path+'/dp.png')
dpimg = ImageTk.PhotoImage(im1)
dp = Label(root, font=('calibri',10),bg='#fff',fg='black', image=dpimg)
dp.place(x=350, y=150)


root.mainloop()
