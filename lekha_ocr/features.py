#    Lekha Ocr version 2.0 - Convert your malayalam documents and images to editable text
#    Copyright (C) 2018 Space-kerala (Society For Promotion of Alternative Computing and Employment)

#    Lekha Ocr version 2.0 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Lekha Ocr version 2.0 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import cv2
import numpy as np
from math import sqrt,atan2,floor

def find_feature(char):
	return np.array(zonewise_hu5(char)+htow_ratio(char)+find_blobs(char)+feature_hu2(char.copy())[:-6]+HOG(char.copy()),np.float32)

def feature_hu2(img):
	h1,contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	moments = [0,0,0,0,0,0,0,0,0,0,0,0]
	if(len(contours)==0):
		return moments
	X = [cv2.contourArea(C) for C in contours]
	t=[i for i in range (0,len(contours))]
	X,t = zip(*sorted(zip(X,t),reverse=True))
	list = []
	for i in range (0,2):
		try:
			cnt = contours[i]
			if(cv2.contourArea(cnt)<4):
				[list.append(0.0) for j in range(0,6)]
				continue
			mom = cv2.HuMoments(cv2.moments(cnt))
			moments=mom[:-1]
			[list.append(m[0]) for m in moments]
		except IndexError:
			[list.append(0.0) for j in range(0,6)]
	return list

def zonewise_hu5(img):#diagonal with more contours
	global ter
		#temporary,contours, hierarchy = CV_
	# contours=[];
	h1,contours,h=cv2.findContours(img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE);
	# print(contours);
	X = [cv2.contourArea(C) for C in contours]
	t=[i for i in range (0,len(contours))]
	try:
		X,t = zip(*sorted(zip(X,t),reverse=True))
	except ValueError:
		cv2.imwrite('error_temp.png',img)
		print ('no countours')
		exit
	cnt = contours[t[0]]
	x,y,w,h=cv2.boundingRect(cnt)
	for i in range(x,x+w):
		for j in range(y,y+h):
			if(cv2.pointPolygonTest(cnt,(i,j),False)==-1):
				img[j,i]=0
	im = img[y-1:y+h+1,x-1:x+w+1]
	feature_rect=zonewise_hu_rect(im.copy())


	height,width=im.shape
	box = img[0:1,0:1]
	box[0,0]=0
	box = cv2.resize(box,(width,height))
	img4=[]
	[img4.append(box.copy())for i in range(0,4)]
	i=0
	for i in range (0,height):
		j=(int)(i*width/height)
		for k in range(0,width):
			if(k<j):
				img4[0][i,k]=im[i,k]
				img4[0][height-i-1,k]=im[height-i-1,k]
			elif(k>width-j):
				img4[2][i,k]=im[i,k]
				img4[2][height-i-1,k]=im[height-i-1,k]
			else:
				img4[1][i,k]=im[i,k]
				img4[3][height-i-1,k]=im[height-i-1,k]
		if (j>width/2):
			break
	i=0
	feature = []
	for img in img4:
		feature = feature+feature_hu2(img)
	return feature+feature_rect
def find_blobs(im):
	params=cv2.SimpleBlobDetector_Params()
	params.filterByArea=True
	params.minArea=10
	params.filterByConvexity=True
	params.minConvexity=0.87
	detector=cv2.SimpleBlobDetector_create(params)
	keypoints=detector.detect(im)
	# print len(keypoints)
	return [len(keypoints)]
def htow_ratio(im):
	h,w=im.shape
	q=0
	for i in range(h):
		for j in range(w):
			if im.item(i,j)==255:
				q+=1
	# print [h/w,(q/(h*w))]
	return [h/w,(q/(h*w))]
def zonewise_hu_rect(img):
	feature = []
	hight,width = img.shape
	if (hight < 4 or width < 4):
		[feature.append(0.0) for i in range(0,48)]
		return feature
	img4=[];
	img4.append(img[0:int(hight/2),0:int(width/2)]);
	img4.append(img[0:int(hight/2),int(width/2):width]);
	img4.append(img[int(hight/2):hight,0:int(width/2)]);
	img4.append(img[int(hight/2):hight,int(width/2):width]);
	for im in img4:
		feature = feature+feature_hu2(im)
	return feature

def HOG(Img, no_divs=3, no_bins=6):

    n_HOG = no_divs*no_divs*no_bins;
    pi = 3.14
    #Initialize output HOG vector
    HOG = [0.0]*n_HOG

    #Apply sobel on image to find x and y orientations of the image
    Icv = Img#.getNumpyCv2()

    Ix = cv2.Sobel(Icv, ddepth = cv2.CV_32F, dx=1, dy=0, ksize=3)
    Iy = cv2.Sobel(Icv, ddepth = cv2.CV_32F, dx=0, dy=1, ksize=3)
    # print (len(Ix),len(Ix[0]))
    Ix = Ix.transpose()#(1,0,2)
    Iy = Iy.transpose()#(1,0,2)
    height,width = Img.shape
    cellx = width/no_divs     #width of each cell(division)
    celly = height/no_divs    #height of each cell(division)

    #Area of image
    img_area = height * width

    #Range of each bin
    BIN_RANGE = (2*pi)/(no_bins)

    m=0
    # print (Img.size)
    # print (Ix.shape)

    while m < no_divs:
        n = 0
        while n < no_divs:
            i = 0
            while i < cellx:
                j=0
                while j < celly:
                    # print (m*cellx+i)
                    # print (n*celly+j)
                    px = Ix[int(m*cellx +i), int(n*celly+j)]
                    py = Iy[int(m*cellx+i), int(n*celly+j)]

                    #grad value
                    grad = sqrt(px*px + py*py)
                    #normalized grad value
                    norm_grad = grad/img_area
                    #print norm_grad
                    #Angle
                    angle = atan2(py,px)
                    if(angle < 0):
                        angle = angle+ 2*pi
                    nth_bin = floor(float(angle/BIN_RANGE))
                    #nth_bin = angle*(180/pi)%180
                    #print nth_bin
                    HOG[((m*no_divs+n)*no_bins + int(nth_bin))] += norm_grad
                    j=j+1
                i= i+1
            n=n+1
        m=m+1

    return np.array(HOG,np.float32)
# img=cv2.imread('home.png',0);
# im = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,243,50)
# q=HOG(im)
# print (len(q))
