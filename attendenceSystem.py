# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:11:19 2018

@author: mayank739
"""

from Tkinter import *
import cv2
import numpy as np
import sqlite3
import tkMessageBox
import trainer
import faceRecognition

window=Tk()
window.title("Attendence System")
window.geometry('512x512')
lbl1=Label(window,text="Attendence System",font=("Arial Black",20))
lbl1.grid(row=0,column=3,sticky='')
#window.configure(height=500,width=900)

    
def form():
    
    lbl2=Label(window,text="Student Id:")
    lbl2.grid(row=4,column=2)
    Id=Entry(window,width=30)
    Id.grid(row=4,column=3)
    lbl3=Label(window,text="Student Name:")
    lbl3.grid(row=5,column=2)
    Name=Entry(window,width=30)
    Name.grid(row=5,column=3)
    lbl4=Label(window,text="Branch:")
    lbl4.grid(row=6,column=2)
    Branch=Entry(window,width=30)
    Branch.grid(row=6,column=3)
    lbl5=Label(window,text="Year:")
    lbl5.grid(row=7,column=2)
    Year=Entry(window,width=30)
    Year.grid(row=7,column=3)
    btn2=Button(window,text="Register",command=lambda: faceRecognition.registerStudent(Id.get(),Name.get(),Branch.get(),Year.get()))
    btn2.grid(row=8,column=2)
    btn3=Button(window,text="Train Camera",command=trainer.machineTrainer)
    btn3.grid(row=8,column=3)
    
    buttons=[lbl2,Id,lbl3,Name,lbl4,Branch,lbl5,Year,btn2,btn3]
    def remove():
        for button in buttons:
            button.grid_forget()
        btn4.grid_forget()
            
    
    btn4=Button(window,text="exit",command=remove)
    btn4.grid(row=8,column=4)
    
        
    
    
btn0= Button(window,text="Add New Student", command=form) 
btn0.grid(row=3,column=2)

btn1= Button(window,text="Take Attendence") 
btn1.grid(row=3,column=4)
window.mainloop()