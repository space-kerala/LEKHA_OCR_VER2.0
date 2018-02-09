
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import json
import cv2
import math
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
import features
import make_word_original
from sklearn.preprocessing import normalize,Normalizer
from matplotlib import pyplot as plt
import pandas as pd


# In[2]:


#get_ipython().magic(u'matplotlib')
def plot(string='',*images):
    ncols=2
    nrows=int(math.ceil(len(images)/2.0))
    fig, ax = plt.subplots(nrows, ncols,gridspec_kw = {'wspace':0, 'hspace':0},facecolor='.5')
    plt.axis('off')
    for i in range(0,len(images)):
        plt.subplot(nrows,ncols,i+1),plt.imshow(images[i],cmap='gray')
        plt.text(0,0,string+'\n')
        plt.axis('off')
    plt.show()


# In[3]:


def cv_plot(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyWindow('image')


# In[4]:


def takecenteroid(cnt):
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    return int(cX)


# In[5]:


def lekha_run(im):
    conf = json.load(open('conf.json', 'r'))
    #image_path = conf['image_path']
    clf_path =conf['clf_path']
    data_path=conf['data_save_path']
    string=' '

    data=pd.read_pickle(data_path)
    X_sample,Y_label = data.drop("target",axis=1),data.target
    X_sample_n = Normalizer().fit(X_sample)
    classifier = joblib.load(clf_path)

    #im=cv2.imread(image_path,0)
    image_h,image_w=im.shape

    # scaned documents contain glyp impressions of other side
   
        
    
    img= cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,243,50)
    #kernel to join along horizontal 
    kernel_line = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],np.uint8)
    dilation = cv2.dilate(img,kernel_line,iterations = 6)
    #plot("sds",dilation)

    im, contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    avg_height_arr=[]

    for cnt in contours:
        x,y,w,h= cv2.boundingRect(cnt)
        if w*h > 1000:
            avg_height_arr.append(h)

    #detect average height of a line in document which should include punctuations

    #avg_height=np.mean(sorted(avg_height_arr,reverse=True)[2:9])
    #print(avg_height)
    if len(avg_height_arr)<9:
        avg_height=np.mean(sorted(avg_height_arr,reverse=True))
    else:
        avg_height=np.mean(sorted(avg_height_arr,reverse=True)[2:9])
    # wordarea , minimum of 2 letters 

    word_area=(avg_height*avg_height)/1.8

    kernel_chandrakala = np.array([[0,0,1,1,1],[0,0,1,1,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]],np.uint8)
    ker_width=kernel_chandrakala.shape[1]/2

    iteration=int(math.ceil((avg_height/(1.5*ker_width))))
    dilation = cv2.dilate(dilation,kernel_line,iterations = (iteration-5))
    #plot('lines',dilation)

    line_boxes=[]
    im, contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        x,y,w,h= cv2.boundingRect(cnt)

        if (h > (avg_height/1.7)) & (w>(avg_height+(ker_width*iteration*2))):

            line_boxes.append([x,y,image_w,y+h])

    line_boxes=sorted(line_boxes,key=lambda box: box[1])

    if len(line_boxes)==0:
        print ("no lines found")

    kernel_word = np.array([[1,1,1],[1,1,1],[1,1,1],[0,0,0],[0,0,0]],np.uint8)


    for box in line_boxes:

        line_image= img[box[1]:box[3],box[0]:box[2]]
        word_dilate= cv2.dilate(line_image,kernel_word,iterations = int(avg_height/10))
        w_h,w_w=word_dilate.shape
        #cv_plot(line_image)

        im_w, contours_w, hierarchy_w = cv2.findContours(word_dilate.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        word_boxes=[]

        for cnt in contours_w:
            x,y,w,h= cv2.boundingRect(cnt)
            if h >= (w_h/2):
                w_area=cv2.contourArea(cnt)
                if w_area>word_area:
                    word_boxes.append([x,0,x+w,w_h])

        if len(word_boxes)==0:
            continue
        word_boxes=sorted(word_boxes,key=lambda w_box: w_box[0])  

        for w_box in word_boxes:
            word_cut=line_image[w_box[1]:w_box[3],w_box[0]:w_box[2]]
            im_le, contours_le, hierarchy_we = cv2.findContours(word_cut.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            letters=sorted([cnt for cnt in contours_le if (cv2.contourArea(cnt)>10)],key=takecenteroid)

            char_list=[]
            for letter in letters:
                x_le,y_le,w_le,h_le=cv2.boundingRect(letter)
                #print w_le,h_le
                char=word_cut[y_le:y_le+h_le,x_le:x_le+w_le] 
                char_feature=np.array(features.HOG(char.copy()))
                char_feature=char_feature.reshape(1,-1)
                char_feature=X_sample_n.transform(char_feature)

                predicted_letter=classifier.predict(char_feature)
                if predicted_letter[0]=='ഠ' or predicted_letter[0]=='ം':
                    if h_le < avg_height/2:
                        predicted_letter[0]='ം'
                    else:
                        predicted_letter[0]='ഠ'
                char_list.append(predicted_letter[0])
                #cv_plot(char)

            #print char_list
            string=string+make_word_original.form_word(char_list)
            string=string+' '
        string=string+'\n'
    return string

