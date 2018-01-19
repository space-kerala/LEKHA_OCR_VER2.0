
# coding: utf-8

# In[25]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import cv2
import json
import numpy as np
from collections import namedtuple
from sklearn import svm
from sklearn.externals import joblib
from math import atan2, degrees, pi
import features
import make_word_original
from sklearn.preprocessing import normalize,Normalizer


# In[26]:

def lekha_run(im):
    conf = json.load(open('conf.json', 'r'))
    image_path = conf['image_path']
    clf_path =conf['clf_path']
    data=pd.read_pickle("data.pkl")
    X_sample = data.drop("target",axis=1)
    X_sample_n = Normalizer().fit(X_sample)


    #im = cv2.imread(image_path,0)
    img= cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,243,43)
    classifier = joblib.load(clf_path)
    MyStruct = namedtuple('MyStruct', 'line_no line_start line_end bowl_start bowl_end word_no char_pos x1 y1 wi hi label')
    NodeDb = []
    height,width=img.shape
    sump=np.zeros(height)
    sumvp=np.zeros(width)
    string=' '

    hor_pix_den=[0 for i in range(0,height)]
    for i in range(0,height):
        for j in range(0,width):
            sump[i]=sump[i]+img[i][j]
        sump[i]/=255
        if sump[i]<9:
            sump[i]=0
    noise =8
    fin=0
    lineno=0
    start=0

    for i in range (2,height):
        if(sump[i]>noise and sump[i-1]<(noise) and (sump[i-2]<noise)):
            if(fin==0):
                fin=1
                start = i
        elif(fin==1 and (i+2)<height and (sump[i+1]<noise and sump[i+2]<noise) and (i-start)>13) :
            fin=0
            end=i
            wordno=0
            l1=0
            l2=0
            precount=0
            for f in range(start,end):  
                k=np.absolute(precount-sump[f])
                if ((sump[f]>precount) and k>l1):
                    l1=k
                    b1=f
                elif((precount>sump[f]) and k>l2):
                    l2=k
                    b2=f
                precount=sump[f]
            Node = MyStruct(line_no=lineno,line_start=start,line_end=end,bowl_start=b1,bowl_end=b2,word_no=None,char_pos=None,x1 =None,y1 =None,wi =None,hi =None,label=None)
            lineno+=1

            #cv2.imshow('window',img[start:i,0:width])
            #cv2.waitKey(0)
            startw=0
            fin1=0
            word_space=(end-start)/5
            for p in range(0,width):
                for q in range(start,end):
                    sumvp[p]=sumvp[p]+img[q][p]
                sumvp[p]=int(sumvp[p]/255)
                if sumvp[p]<=2:
                    sumvp[p]=0
                #print sumvp[p]

            for p in range(0,width-8):
                arr=np.array(sumvp[p-10:p])
                arr1=np.array(sumvp[p:p+10])
                #print arr
                if (fin1==0 and  np.count_nonzero(arr)<=1 and np.count_nonzero(arr1)>=7):
                    startw=p
                    #cv2.line(im,(startw,start),(startw,end),(0,0,0),2)
                    fin1=1
                elif(fin1==1 and p-startw>=40 and np.count_nonzero(arr)>=7 and np.count_nonzero(arr1)<=1):
                    Node=Node._replace(word_no=wordno)
                    wordno+=1
                    endw=p
                    #cv2.line(im,(startw,start),(startw,end),(0,0,0),2)
                    fin1=0
                    #cv2.line(im,(endw,start),(endw,end),(0,0,0),2)
                    t=img[start:end,startw:endw].copy()
                    _,contours2, hierarchy = cv2.findContours(t.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                    if(len(contours2)==0):
                        print ('no line')
                    contours = []
                    for cnt in contours2:
                        if(cv2.contourArea(cnt)>6):
                            try:
                                contours.append(cnt)
                            except ValueError:
                                print ('error')
                                pass
                    Mset = [cv2.moments(cnt) for cnt in contours]
                    X = [int(M['m10']/M['m00']) for M in Mset]
                    index = [i for i in range(0,len(contours2))]
                    try:
                        X,index = zip(*sorted(zip(X,index)))
                    except:
                        h=1
                    char_list=[]

                    cn=1
                    for i in index:
                        cnt = contours[i]
                        x,y,w,h=cv2.boundingRect(cnt)
                        Node= Node._replace(char_pos=i)
                        Node= Node._replace(x1=x)
                        Node= Node._replace(y1=y)
                        Node= Node._replace(wi=w)
                        Node= Node._replace(hi=h)
                        char=t[y-1:y+h+1,x-1:x+w+1]
                        #cv2.imshow('char',char)
                        #cv2.waitKey(0)
                        up_diff=Node.bowl_start-Node.line_start
                        bw_diff=Node.bowl_end-Node.line_start
                        g_height=Node.y1+Node.hi
                        arr=np.zeros(4)
                        if(Node.y1<(up_diff-6)):
                            arr[0]=1
                        if(Node.y1<bw_diff+3 and (g_height)>(up_diff+(Node.bowl_end-Node.bowl_start)/2)):
                            arr[1]=1
                        if((g_height)>(bw_diff+4)):
                            arr[2]=1
                        if(Node.y1<(up_diff+3) and g_height>(bw_diff-4)):
                            arr[3]=1
                        #print arr
                        char_feature=np.array(features.HOG(char.copy()))
                        char_feature=X_sample_n.transform(char_feature.reshape(1,-1))
                        #char_feature1=np.array(char_feature +arr)
                        letter=classifier.predict(char_feature)


                        #print letter[0],"  ",arr
                        #.encode('utf-8')
                        Node=Node._replace(label=letter[0].decode('utf-8'))
                        NodeDb.append(Node)
                        char_list.append(letter[0])
                        #print char_list
                    string=string+make_word_original.form_word(char_list)
                    string=string+' '
            string=string+'\n'
    return string
    #f = open('test', 'w')
    #f.write(string.encode('utf8'))
    #f.close()


