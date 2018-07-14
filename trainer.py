# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 15:59:36 2018

@author: mayank739
"""
def machineTrainer():
    import os
    import cv2
    import numpy as np
    from PIL  import Image
    import Tkinter
    import tkMessageBox
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    path='images'

    def getImagesWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        for imagePath in imagePaths:
            faceImg=Image.open(imagePath).convert('L')
            faceNp=np.array(faceImg,'uint8')
            ID=int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow('training',faceNp)
            cv2.waitKey(10)
        return np.array(IDs),faces

    Ids,faces=getImagesWithID(path)
    recognizer.train(faces,Ids)
    recognizer.save('trainingData.yml')
    cv2.destroyAllWindows()
    tkMessageBox.showinfo("Success", "Student Successfully Registered")
    



