# -*- coding: utf-8 -*-
"""
Created on Fri Jul 06 00:31:58 2018

@author: mayank739
"""

import cv2
import numpy as np

rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('trainingData1.yml')
id=0
names={1:"MAYANK",6:"MAYANK",3:"PARAG",4:"PARAG",5:"ANKUR",7:"AKHIL"}
font=cv2.FONT_HERSHEY_SIMPLEX
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        cv2.putText(img,names[id],(x,y+h),font,1,(0,0,255))
    cv2.imshow('face',img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
