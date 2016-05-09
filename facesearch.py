from pyfaces import pyfaces
import sys,time


# if __name__ == "__main__":
def faceRecognizer(input_img_path,egfaces=1,thrshld=1):
    try:
        start = time.time()
        argsnum=len(sys.argv)
        #print "args:",argsnum
        # if(argsnum<5):
        #     print "usage:python pyfacesdemo imgname dirname numofeigenfaces threshold "
        #     sys.exit(2)                
        imgname=input_img_path
        dirname='/home/venkat/Review/facesdataset/'
        
        pyf=pyfaces.PyFaces(imgname,dirname,egfaces,thrshld)
        match, dist=pyfaces.PyFaces.getMatchFile(pyf)
        end = time.time()
        tim=(end-start)
        return (match, dist, tim)
    except Exception,detail:
        print detail.args
        print "usage:python pyfacesdemo imgname dirname numofeigenfaces threshold "

