
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


# coding: utf-8

# In[6]:


import numpy as np
import cv2
from matplotlib import pyplot as plt
from scipy.stats import mode

# In[7]:

def itervalue(img):
    htArray = []
    _,contours,ju= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.boundingRect(c)
        if rect[3] <= 5: continue
        htArray.append(rect[3])
    htArray.sort()
    a =mode(htArray)
    d=a[0]
    return d


def layout(im):
    ret3,th2 = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th3 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY_INV,41,11)
    kernel = np.array([[0,1,0],[0,1,0],[0,1,0]],np.uint8)
    dilation = cv2.dilate(th3,kernel,iterations = 2)
    _,contours,hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    largest_area = sorted(contours, key=cv2.contourArea, reverse=True)
    max_img=im.size*0.7
    for i in range(len(largest_area)):
        rect = cv2.boundingRect(largest_area[i])
        x,y,w,h=rect
        if(im.size<=w*h*20) and (w*h<=max_img):
            cv2.rectangle(th3,(x,y),(x+w,y+h),0,-1)
    h,b=heading(th3.copy())
    return h,b
    
def heading(im):
    md=itervalue(im.copy())
    img = np.zeros(im.shape, np.uint8)   
    #blur = cv2.GaussianBlur(removed,(5,5),0)
    kernel = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],np.uint8)
    dilation = cv2.dilate(im,kernel,iterations = 3*md)
    
    
    b = []
    _,cnt, _ = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnt:
        rect = cv2.boundingRect(c)
        if cv2.contourArea(c) < 3000: continue
        x,y,w,h = rect
        b.append([x,y,w,h])
    _,cont, _ = cv2.findContours(im, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    f=[]
    for q in range(len(b)):
        f.append([])
    for c in cont:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        
            for a in range(len(b)):
                if (cX in range(b[a][0],b[a][0]+b[a][2])) and (cY in range(b[a][1],b[a][1]+b[a][3])):
                    rec = cv2.boundingRect(c)
                    f[a].append([cX,cY,rec[3]])
            
        else:
            cX, cY = 0, 0
    for u in range(len(b)):
        sorted(f[u],key=lambda x: x[0])
    a = []
    for l in range(len(b)):
        m = []
        for x in range(len(f[l])-2):
            a=[f[l][x][2],f[l][x+1][2],f[l][x+2][2]]
            m.append(np.mean(a))
        
        f[l].append(np.mean(m))
    hd=[]
    for r in range(len(b)):
         if f[r][len(f[r])-1]>=md+2:
            hd.append([b[r][0],b[r][1],b[r][2],b[r][3]])
            cv2.rectangle(im,(b[r][0],b[r][1]),(b[r][0]+b[r][2],b[r][1]+b[r][3]),(0,0,0),-1)
    
    bd=body(im.copy(),md)
    return hd,bd

def body(im,iv):
    kernel = np.array([[0,1,0],[0,1,0],[0,1,0]],np.uint8)
    dilation = cv2.dilate(im,kernel,iterations = 2*iv)
    _,cont, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    b=[]
    for c in cont:
        _,ct, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        con = sorted(ct, key=cv2.contourArea, reverse=True)
        if not con:break
        rect = cv2.boundingRect(con[0])
        if cv2.contourArea(con[0]) < 6000: continue
        x,y,w,h = rect
        #if w*h <= 0.5*im.size:
        cv2.rectangle(dilation,(x,y),(x+w,y+h),(0,0,0),-1)
        b.append([x,y,w,h])
    
    
    return b

# In[9]:


