from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import os
import numpy as np
import cv2


class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition system")
        
       
        title_label=Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"),bg="white", fg="red")
        title_label.place(x=0,y=0, width=1300, height=40) 
        
        #FIRST IMAGE
        
        img=Image.open(r"images/f4.jpg")
        img=img.resize((430,580),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        label1=Label(self.root, image=self.photoimg)
        label1.place(x=0, y=45, width=430, height=580)
        
         #SECOND IMAGE
        
        img1=Image.open(r"images/f5.webp")
        img1=img1.resize((850,580),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        label1=Label(self.root, image=self.photoimg1)
        label1.place(x=430, y=45, width=850, height=580)
        
        
        # ============button===================
        
        button_train=Button(label1,text="Face Recognition",command=self.face_recognition, cursor="hand2",font=("times new roman",14, "bold"),bg="RED", fg="white" )
        button_train.place(x=320, y=510, width=220, height=35)
        
        # ====================Atttendence=================================
    def mark_attendance(self,i,n,a,d):
        with open("face.csv","r+", newline="\n")as f:
            my_data=f.readlines()
            name_list=[]
            for line in my_data:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (a not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dte=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{a},{d},{dte},{d1},PRESENT")
                
        # =======================Face Recognition ==========================
        
    def face_recognition(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbours, color, text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            
            coordinates=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost", username="root", password="Rutuj@0207", database="criminal")
                mycursor=conn.cursor() 
                 
                mycursor.execute("select case_id from criminal where case_id="+str(id))
                i=mycursor.fetchone()
                i="+".join(i)
                mycursor.execute("select name from criminal where case_id="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)
                mycursor.execute("select crime_type from criminal where case_id="+str(id))
                a=mycursor.fetchone()
                a="+".join(a)
                mycursor.execute("select arrest_date from criminal where case_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)
                
                
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-45),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Crime Type:{a}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)
                    cv2.putText(img,f"Arrest Date:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)
                    
                    self.mark_attendance(i,n,a,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),3)
                 
                coordinates=[x,y,w,h]
            
            return coordinates
        
        def recognition(img,clf, faceCascade):
            coordinates=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, img=video_cap.read()
            img=recognition(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
              break
        video_cap.release()
        cv2.destroyAllWindows()
           
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
        