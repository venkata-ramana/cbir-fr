from Tkinter import *
import Tkinter as Tk
from PIL import Image, ImageTk
import facesearch
from tkFileDialog import *
import tkMessageBox as tkm
import ch_dim
import fd2, os



class Body(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def changedim(self):
        total=ch_dim.changeDim()
        tkm.showinfo('Changing Dimensions','Successfully Changed '+str(total)+' images dimensions, Results has stored in facesdataset directory')

    def callback(self):
        choosenfile = askopenfilename(parent=self.parent)
        # if(choosenfile):
        #     input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Sit back and relax we are seaching most similer results for, we will get back to you once we completed our search.')
        #     input_img_label.place(x=20, y=150)
        inputimage=choosenfile
        choosenfile = choosenfile.split('/')
        choosenfile = choosenfile[::-1]
        choosenfile = choosenfile[1] + '/' + choosenfile[0]
        result, dist, time = facesearch.faceRecognizer(choosenfile)
        self.showresults(result,inputimage,dist,time)

    def grabfaces(self):
        tkm.showinfo('Grabbing faces','Successfully Grabbed all faces from all images')
        fd2.grabfaces()


    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        canvas.create_rectangle(0, 0, 0, 0, outline="#06617C", fill="#06617C")
        canvas.pack(fill=BOTH, expand=1)
        path=os.getcwd() 	
        im = Image.open(path+'/bg.png')
        bgimage = ImageTk.PhotoImage(im)
        canvas.img = bgimage
        canvas.create_image(0, 0, anchor=NW, image=bgimage)

        gfaces = Button(canvas, text='Grab faces', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.grabfaces)
        gfaces.pack()
        canvas.create_window(400, 100, window=gfaces)

        chdim = Button(canvas, text='Change Dimensions', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.changedim)
        chdim.pack()
        canvas.create_window(650, 100, window=chdim)

        widget = Button(canvas, text='Upload file..!', fg='black', bg='#fff', highlightthickness=0,font=('calibri',10), command=self.callback)
        widget.pack()
        canvas.create_window(900, 100, window=widget)

    def showresults(self, result, input,dist,time):
        print "Result displaying";
        input_label = Label(self.parent, font=('calibri',11),bg='#fff',fg='black', text='Query Image')
        input_label.place(x=490, y=175)
        path1 = Image.open(input)
        path1 = path1.resize((250, 200), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(path1)
        input_img_label = Label(self.parent, image=img1)
        input_img_label.image = img1
        input_img_label.place(x=400, y=200)

        result_label = Label(self.parent, font=('calibri',11),bg='#fff',fg='black', text='Result from Query')
        result_label.place(x=770, y=175)
        path1 = Image.open(result)
        path1 = path1.resize((250, 200), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(path1)
        input_img_label = Label(self.parent, image=img1)
        input_img_label.image = img1
        input_img_label.place(x=700, y=200)
        i = 0
        total = 105
        perc = int(dist)
        while (i <= perc):
            total -= 5;
            i += 1

        # input_img_label = Label(self.parent, font=('calibri',13),bg='#fff',fg='black', text='Got '+str(total)+' % match..!')
        # input_img_label.place(x=580, y=410)

        input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Input Path:   '+input)
        input_img_label.place(x=400, y=460)

        input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Output Path:  '+result)
        input_img_label.place(x=400, y=490)

        input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Distance:  '+str(dist))
        input_img_label.place(x=400, y=520)

        input_img_label = Label(self.parent, font=('calibri',10),bg='#fff',fg='black', text='Time taken:  '+str(time)+' secs..')
        input_img_label.place(x=400, y=550)


def main():
    root = Tk.Tk()
    root.resizable(width=True, height=True)
    root.geometry('{}x{}'.format(1400, 770))
    
    root.title("Content Based Image Retrieval")                                     # setting up title of window
    # root.iconbitmap(bitmap='/home/venkat/images/logo.ico')						#setting up logo of window
    body = Body(root)
    root.mainloop()


if __name__ == '__main__':
    main()

