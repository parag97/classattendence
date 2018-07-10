import cv2
import numpy as np
import os

rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('trainingData1.yml')
id1=0
names={1:"MAYANK",6:"MAYANK",3:"PARAG",4:"PARAG",5:"ANKUR",7:"AKHIL"}
font=cv2.FONT_HERSHEY_SIMPLEX
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
sampleNum=0
imagePaths=[os.path.join("images",f) for f in os.listdir("images")]
for imagePath in imagePaths:
    try:
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        if(ID==id1):
            sampleNum=sampleNum+1
    except:
        print(os.path.split(imagePath)[-1].split('.')[1],print(imagePath))  
while(True):
    ret,img=cam.read()
    if ret is True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        continue
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        for imagePath in imagePaths:
            try:
                ID=int(os.path.split(imagePath)[-1].split('.')[1])
                if(ID==id1):
                    sampleNum=sampleNum+1
            except:
                print(os.path.split(imagePath)[-1].split('.')[1],print(imagePath)) 
            cv2.imwrite("images/User."+str(id1)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id1,conf=rec.predict(gray[y:y+h,x:x+w])
        cv2.putText(img,names[id1],(x,y+h),font,1,(0,0,255))
    cv2.imshow('face',img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()