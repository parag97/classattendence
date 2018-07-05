import cv2
import numpy as np
faceDetect = cv2.CascadeClassifier("C:\Python3.6\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml");
cv2.namedWindow("output", cv2.WINDOW_NORMAL)  
# Load an color image in grayscale
img = cv2.imread('test.jpg',0)
faces=faceDetect.detectMultiScale(img,1.2,2);
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),5)
cv2.imshow('output',img);
cv2.waitKey(0)==ord('q')
cv2.destroyAllWindows()
