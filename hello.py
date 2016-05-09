from Tkinter import *
from PIL import Image, ImageTk
import glob
master = Tk()
scrollbar=Scrollbar(master)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(master, yscrollcommand=scrollbar.set)
for imagePath in glob.glob("/home/venkat/images/img/"+"*.png")
	
	i=listbox.insert(END,str(i))

listbox.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=listbox.yview)
mainloop()

