# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 00:47:00 2018

@author: mayank739
"""

import cv2
import numpy as np
import sqlite3
from Tkinter import *
import tkMessageBox


def addStudent(id,name,branch,year):
    conn=sqlite3.connect("attendence.db")
    cursor=conn.cursor()
    query="SELECT * FROM student WHERE Id="+str(id)
    data=cursor.execute(query)
    isRecordExist=0
    for row in data:
        isRecordExist=1
    if (isRecordExist==1):
        query="UPDATE student SET Name="+str(name)+",Branch="+str(branch)+", Year="+str(year)
        cursor.execute(query)
    else:
        query="INSERT INTO student (Id,Name,Branch,Year) Values("+str(id)+",'"+str(name)+"','"+str(branch)+"',"+str(year)+")"
        cursor.execute(query)
    conn.commit()
    conn.close()

def registerStudent(id,name,branch,year):
    
    sampleNum=0
    addStudent(id,name,branch,year)
    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)

    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("images/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(100)
        
        cv2.imshow('face',img)
        cv2.waitKey(1)
        if sampleNum>20:
            break
    
    cam.release()
    cv2.destroyAllWindows()
    tkMessageBox.showinfo("Success", "Student Successfully Registered")
