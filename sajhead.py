
# coding: utf-8

# In[6]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[7]:


def bodyprint(im):
    img = np.zeros(im.shape, np.uint8)
    ret, gray = cv2.threshold(im, 250, 255,0)
    _,contours,hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    mask = np.zeros(im.shape, np.uint8)
    largest_area = sorted(contours, key=cv2.contourArea, reverse=True)
    cv2.drawContours(mask, largest_area, 1, (255,255,255), -1)
    removed = cv2.add(im, mask)
    
    i=0
    while(i<=10):
        i=i+1
        cs=cv2.contourArea(largest_area[i])
        if(im.size<=cs*15):
            cv2.drawContours(mask, largest_area, i, (255,255,255), -1)
            removed = cv2.add(im, mask)
            
    #blur = cv2.GaussianBlur(removed,(5,5),0)
    ret3,th2 = cv2.threshold(removed,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th3 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,41,11)
    
    
    _,contour, _ = cv2.findContours(th3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contour:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)    
    kernel = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]],np.uint8)
    dilation = cv2.dilate(img,kernel,iterations = 4)
    _,cont, _ = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    s2=[]
    for c in cont:
        rect = cv2.boundingRect(c)
        if cv2.contourArea(c) < 6000: continue
        x,y,w,h = rect
        s2.append([x,y,w,h])
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        
    return s2


# In[9]:


def boundary(im):
    
    img = np.zeros(im.shape, np.uint8)
    s2 = bodyprint(im.copy())
    ret, gray = cv2.threshold(im, 250, 255,0)
    _,contours,hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    mask = np.zeros(im.shape, np.uint8)
    largest_area = sorted(contours, key=cv2.contourArea, reverse=True)
    cv2.drawContours(mask, largest_area, 1, (255,255,255), -1)
    removed = cv2.add(im, mask)
    
    i=0
    while(i<=10):
        i=i+1
        cs=cv2.contourArea(largest_area[i])
        if(im.size<=cs*15):
            cv2.drawContours(mask, largest_area, i, (255,255,255), -1)
            removed = cv2.add(im, mask)
            
    #blur = cv2.GaussianBlur(removed,(5,5),0)
    ret3,th2 = cv2.threshold(removed,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    th3 = cv2.adaptiveThreshold(th2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,41,11)
    kernel = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],np.uint8)
    dilation = cv2.dilate(th3,kernel,iterations = 3)
    
    
    b = []
    _,cnt, _ = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnt:
        rect = cv2.boundingRect(c)
        #if cv2.contourArea(c) < 3000: continue
        x,y,w,h = rect
        b.append([x,y,w,h])
    _,cont, _ = cv2.findContours(th3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
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
        
        cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1) 
    for u in range(len(b)):
        sorted(f[u],key=lambda x: x[0])
    a = []
    for l in range(len(b)):
        m = []
        for x in range(len(f[l])-2):
            a=[f[l][x][2],f[l][x+1][2],f[l][x+2][2]]
            m.append(np.mean(a))
        
        f[l].append(np.mean(m))
    s=[]
    for r in range(len(b)):
         if f[r][len(f[r])-1]>=10:
            s.append([b[r][0],b[r][1],b[r][2],b[r][3]])
            cv2.rectangle(im,(b[r][0],b[r][1]),(b[r][0]+b[r][2],b[r][1]+b[r][3]),(0,255,0),2)
            #print f[r]
    return s,s2