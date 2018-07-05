import cv2
import numpy as np
faceDetect = cv2.CascadeClassifier("C:\Python3.6\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml");
print(faceDetect)
cam=cv2.VideoCapture(0);

ret,img=cam.read();
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceDetect.detectMultiScale(gray,1.3,5);
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
cv2.imshow('Face',img);
cv2.waitKey(0)==ord('q')
cam.release()
cv2.destroyAllWindows()
