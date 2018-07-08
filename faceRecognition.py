# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 00:47:00 2018

@author: mayank739
"""

import cv2
import numpy as np
import os
id1=int(input('Enter the user id'))
sampleNum=0
imagePaths=[os.path.join("images",f) for f in os.listdir("images")]

for imagePath in imagePaths:
    try:
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        if(ID==id1):
            sampleNum=sampleNum+1
    except:
        print(os.path.split(imagePath)[-1].split('.')[1],print(imagePath))  
breakNum = sampleNum
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("images/User."+str(id1)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('face',img)
    cv2.waitKey(1)
    if sampleNum>20+breakNum:
        break
    
cam.release()
cv2.destroyAllWindows()