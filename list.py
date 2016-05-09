from Tkinter import *
from PIL import ImageTk, Image 
import glob
files = glob.glob('/home/venkat/images/img/*.png')
class App:
	def __init__(self, root):
		self.s =Scrollbar(root)
		self.s.pack(side=RIGHT,fill=Y)
		self.l =Listbox(root, yscrollcommand=self.s.set)
		self.l.pack(side=LEFT,fill=BOTH)
		self.l.bind('<<ListboxSelect>>', self.lol)
		self.s.config(command=self.l.yview)
		self.c =Label(root)
		self.c.pack()
		for f in files:
			self.l.insert(END, f)

	def lol(self, evt):
		path = files[self.l.curselection()[0]]
		img =ImageTk.PhotoImage(Image.open(path))
		self.c.image = img           # save reference
		self.c.configure(image=img)# configure the label
		self.c.pack()
root =Tk()
App(root)
root.mainloop()