import Tkinter as tk
import cv2
import cv2.cv as cv
from PIL import Image, ImageTk
import datetime, os
import fd2

cap = cv2.VideoCapture(0)

def capture():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)
    vis = frame.copy()
    #draw_rects(vis, rects, (0, 255, 0),1)
    for x1, y1, x2, y2 in rects:
        roi = gray[y1:y2, x1:x2]
        vis_roi = vis[y1:y2, x1:x2]
        subrects = detect(roi.copy(), nested)
        #draw_rects(vis_roi, subrects, (255, 0, 0),0)

    now = datetime.datetime.now()
    cv2.imwrite(str(unicode(now.replace(microsecond=0)))+'.jpg',  vis[y1:y2,x1:x2])

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('{}x{}'.format(screen_width, screen_height))
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root,width=screen_width)
lmain.place(x=0,y=0,width=screen_width,height=screen_height-200)

##3E0404
panel = tk.Button(root, bg='#3E0404',text='Capture',command=capture,fg='#fff',font=('calibri',10),highlightthickness=0)
panel.place(x=(screen_width/2)-100,y=screen_height-150,width=200,height=50)


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color,opt):
    for x1, y1, x2, y2 in rects:
        rect=cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        if opt:
	        font = cv2.FONT_HERSHEY_SIMPLEX
	        cv2.putText(img,'Face',(x1,y1-5), font, 1,color,2)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)
    vis = frame.copy()
    draw_rects(vis, rects, (0, 255, 0),1)
    for x1, y1, x2, y2 in rects:
        roi = gray[y1:y2, x1:x2]
        vis_roi = vis[y1:y2, x1:x2]
        subrects = detect(roi.copy(), nested)
        draw_rects(vis_roi, subrects, (255, 0, 0),0)

    cv2image = cv2.cvtColor(vis, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk 
    lmain.configure(image=imgtk,)
    lmain.after(10, show_frame)

def grab_faces():
    tkm.showinfo('Grabbing faces','Successfully Grabbed all faces from all images')
    fd2.grabfaces()



import sys, getopt
args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
try: video_src = video_src[0]
except: video_src = 0
args = dict(args)
cascade_fn = args.get('--cascade', "./haar/haarcascade_frontalface_alt.xml")
nested_fn  = args.get('--nested-cascade', "./haar/haarcascade_eye.xml")

cascade = cv2.CascadeClassifier(cascade_fn)
nested = cv2.CascadeClassifier(nested_fn)

show_frame()
root.mainloop()