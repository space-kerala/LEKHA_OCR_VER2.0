# -*- coding: utf-8 -*-
import os
import codecs
import cv2
import features
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn.preprocessing import normalize
train_set = []
samples=[]
responses=[]

alist_filter = ['png','jpg','bmp','gif']
rootDir ="/home/kamara/lekha/train_images/"
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' %dirName)
    file_path = os.path.join(dirName,'utf8')
    line_path=os.path.join(dirName,'lab.txt')
    arr=np.genfromtxt(str(line_path),dtype=None)
    fp=codecs.open(str(file_path),"r",'UTF-8')
    label_u=(fp.readline().strip()).encode('UTF-8')
    print label_u ,len(fileList)
    for fname in fileList:
        if fname[-3:] in alist_filter:
            responses.append(label_u)
            file_path = os.path.join(dirName, fname)
            im=cv2.imread(str(file_path),0)
            #print file_path
            im = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,243,50)
            #cv2.imshow('k',im)
	    #cv2.waitKey(0)
            samples.append(np.append(features.find_feature(im.copy()),arr))
	    #s=[label_u.decode('utf-8'),features.find_feature(im.copy())]
            #print s
	    #train_set.append(s)
        elif fname=='utf8':
            continue
            """file_path = os.path.join(dirName, fname)
            fp=codecs.open(str(file_path),"r",'utf-8')
            label_u=fp.read(1).encode('utf-8')
            print label_u"""
samples = np.array(samples,np.float32)
np.savetxt('feature_array.txt', samples)
np.savetxt('response_array.txt', responses,fmt="%s")
#X_sample = np.loadtxt('feature_array.txt')
#Y_label=np.genfromtxt('response_array.txt',dtype=None)

#X_normal=normalize(X_sample, norm='max', axis=1, copy=True)
#responses = np.array(responses,np.float32)
#clf=svm.SVC(decision_function_shape='ovo',C=140,probability=True,gamma=1)
#clf.set_params(kernel='rbf').fit(X_sample,Y_label)
#joblib.dump(clf, 'svm/svm_data.lekha')

