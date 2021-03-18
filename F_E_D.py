import cv2
import numpy as np
import imutils
import tkinter
from tkinter import *


#load harr cascade classifer xml file attached in tutorial

face_classifer = cv2.CascadeClassifier(r'PATH')
eye_cascade = cv2.CascadeClassifier(r'PATH')
# create an object to hold the resource the video would be coming from
cap = cv2.VideoCapture(0)

main = tkinter.Tk()
main.title("GUI for Face and Eye") #designing main screen
main.geometry("300x300")

def F_E_D():
       while (True):
              #capture frame
              _,frame = cap.read()
        
              frame=imutils.resize(frame, width=700)
        
              #operations on frame happens here
              gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
              faces = face_classifer.detectMultiScale(gray)
              eyes = eye_cascade.detectMultiScale(gray)
        
        
              if faces != []:
                       for (x,y,w,h) in faces:
                                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
              if eyes != []:
                       for (x,y,w,h) in eyes:
                                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
        

        
              #print number of faces detected
              print('{} faces detected'.format(len(faces)))
              print('{} eyes detected'.format(len(eyes)))
        
              #show frame
              cv2.imshow('Face Detection', gray)
              
              #allow for 1 millisecond delay each loop where program can be quit by pressing 'q'
              if cv2.waitKey(1) & 0xFF == ord('q'):
                       break
        
       #release device or file held for video capture and close all windows
       cap.release()
       cv2.destroyAllWindows()


font1 = ('times', 14, 'bold')
uploadButton = Button(main, text="*_*", command=F_E_D, bg='skyblue')
uploadButton.place(x=100,y=150)
uploadButton.config(font=font1)  

main.config(bg='lemon chiffon')
main.mainloop()
