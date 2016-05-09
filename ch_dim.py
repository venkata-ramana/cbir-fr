import cv2,os,datetime
def changeDim():
    path=os.getcwd()
    i=0
    for root, dirs, files in os.walk(path+'/found_faces'):
        print "Total no of files found : "+str(len(files))
        for file in files:
            if (file.endswith(".jpg") | file.endswith(".png") | file.endswith(".PNG") | file.endswith(".JPG") | file.endswith(".jpeg") | file.endswith(".JPEG")):
                #shutil.copy(os.path.join(root, file),'/home/venkat/fd/found_faces')
                print file+" is processing ..."
                image = cv2.imread(path+'found_faces/'+str(file))
                size=(412,412)
                resized = cv2.resize(image, size, interpolation = cv2.INTER_AREA)
                now = datetime.datetime.now()
                cv2.imwrite(path+"facesdataset/"+file, resized)
                #cv2.imwrite(path+"resized/"+str(unicode(now.replace(microsecond=0)))+' '+str(i)+'.png', resized)
                i+=1

    return i