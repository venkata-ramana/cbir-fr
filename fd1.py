import numpy as np
import cv2
import cv2.cv as cv
import Image, sys
import datetime

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "./haar/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', ".haar/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = cv2.VideoCapture(0)
    
    #while True:
    _, img = cam.read()    # Take each frame
    #img = cv2.imread(sys.argv[1])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    i=0
    rects = detect(gray, cascade)
    vis = img.copy()
    #draw_rects(vis, rects, (0, 255, 0))
    for x1, y1, x2, y2 in rects:
        roi = gray[y1:y2, x1:x2]
        vis_roi = vis[y1:y2, x1:x2]
        subrects = detect(roi.copy(), nested)
        #draw_rects(vis_roi, subrects, (255, 0, 0))
        now = datetime.datetime.now()
        cv2.imwrite('./found_faces/'+str(unicode(now.replace(microsecond=0)))+' '+str(i)+'.png', vis[y1:y2,x1:x2])
        i+=1
    	# eye co-ordinates will be saved in subrects distance btwn eyes can calculate using subrects


    if(i==0):
        print "No faces detected, please check camera or check brightness!"
cv2.destroyAllWindows()
