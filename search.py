

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher

import cv2

def callback(file):
	args={'result_path': 'dataset', 'index': 'index.csv', 'query': ''}
	args['query']=file
	# # initialize the image descriptor
	cd = ColorDescriptor((8, 12, 3))
    #
	# # load the query image and describe it
	query = cv2.imread(args["query"])
	features = cd.describe(query)
    #
	# # perform the search
	searcher = Searcher(args["index"])
	results = searcher.search(features)
    #
	return results
# display the query
#cv2.imshow("Query", query)
#loop over the results
# count=0
# print "Note: lower % of matching shows maximum similarity." 
# for (score, resultID) in results:
# 	# load the result image and display it
# 	i=0
# 	total=100
	
# 	perc=int(score)
# 	while(i<=perc):
# 		total-=5+i;
# 		i+=1
		
	
# 	print "Image "+resultID +" got "+str(total+5)+"% similarity and "+'%2.3f'%score+" score.."
# 	result = cv2.imread(args["result_path"] + "/" + resultID)
# 	cv2.imwrite("/home/venkat/Review/output/"+str(score)+" "+resultID, result)
# 	count+=1
	

# print "Got "+str(count)+" similer results...."

# root = Tk()
# root.geometry('{}x{}'.format(1330, 760))
# root.title("Content Based Image Retrieval")	
# label=Label(root,text = 'Resultant similer images..')
# label.bind()
# c=0
# r=0
# path='/home/venkat/CBIR/dataset/'
# output='/home/venkat/CBIR/'
# print "Note: lower % of matching shows maximum similarity." 
# for (score, resultID) in results:
# 	# load the result image and display it
# 	i=0
# 	total=100
	
# 	perc=int(score)
# 	while(i<=perc):
# 		total-=5;
# 		i+=1
		
	
# 	print "Image "+resultID +" got "+str(total)+"% similarity and "+'%2.3f'%score+" score.."
# 	path1 = Image.open("/home/venkat/Review/dataset/"+resultID)
# 	path1=path1.resize((250, 250),Image.ANTIALIAS)
# 	img1 = ImageTk.PhotoImage(path1)
# 	myvar=Label(root,image = img1)
# 	myvar.image = img1
# 	myvar.grid(row=r,column=c)
# 	c+=250
# 	if(c>1000):
# 		r+=250
# 		c=0
	
	
# root.mainloop()

# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset