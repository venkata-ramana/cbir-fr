
# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
import os
import cv2


def indexer():
    args={'index': 'index.csv', 'dataset': 'dataset'}
    cd = ColorDescriptor((8, 12, 3))
    output = open(args["index"], "w")
    i=0

    paths =[os.path.join(dirpath,f)
            for dirpath,dirnames,files in os.walk(args["dataset"])
            for f in files if (f.endswith('.jpg') | (f.endswith('.JPG')))]

    for imagePath in paths:
        if(imagePath.count('/')>1):
            choosenfile = imagePath.split('/')
            choosenfile = choosenfile[::-1]
            imageID = choosenfile[1]+'/'+choosenfile[0]
        else:
            imageID=imagePath[imagePath.rfind("/")+1:]

        image = cv2.imread(imagePath)
            # describe the image
        features = cd.describe(image)

            # write the features to file
        features = [str(f) for f in features]
        output.write("%s,%s\n" % (imageID, ",".join(features)))
        i+=1

	# close the index file

    output.close()
    return i
# USAGE
# python index.py --dataset dataset --index index.csv

