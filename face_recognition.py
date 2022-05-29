from fileinput import filename
from sys import path
from logging import root
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from unicodedata import name
from PIL import Image, ImageTk
import glob
from cv2 import drawFrameAxes, sort
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")
        self.root.wm_iconbitmap("icon.ico")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 40, "bold"), bg="black", fg="white")
        title_lbl.place(x=0,y=0,width=1480,height=45)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
        Back_Button.pack(side=RIGHT)
        # 1st
        img_top = Image.open("images/facer2.jpg")
        img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
        # 2nd
        img_bottom = Image.open(
            "images/facer1.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55,width=950,height=700)

       # button
        b1_1 = Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog, font=(
            "times new roman", 25, "bold"), bg="black",fg="green")
        b1_1.place(x=365,y=620,width=200,height=40)
    
    #======attendance=========
    def mark_attendance(self,i,r,n,d):
        with open('anuradha.csv','r+',newline='\n') as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(',')
                name_list.append(entry[0])
            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime('%H:%M:%S')
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    print('Encoding complete')

# =====face recog===============

    def face_recog(self):
        #def generate_dataset(frame,id):
            #cv2.imwrite("data/user."+str(id)+"."+str(img_id)+".jpg",frame)

        def draw_boundary(frame,classifier,scaleFactor,minNeighbors,color,text,clf):
            
            gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="chocobar@6",database="facedb",port=3306)
                my_cursor= conn.cursor()
                
                my_cursor.execute("select StudentId from student where StudentId="+str(id))
                i=my_cursor.fetchone()
                
                my_cursor.execute("select Roll from student where StudentId="+str(id))
                r=my_cursor.fetchone()
               
                my_cursor.execute("select Name from student where StudentId="+str(id))
                n=my_cursor.fetchone()
                
                my_cursor.execute("select Department from student where StudentId="+str(id))
                d=my_cursor.fetchone()
                
                
                if confidence>77:
                    
                    cv2.putText(frame,f"StudentId:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(frame,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(frame,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(frame,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(frame,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)

                coord=[x,y,w,h]

            return coord

      

            # face recog===================
        def recognize(frame,clf,faceCascade):
            coord=draw_boundary(frame,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return frame
     
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)


        while True:
            ret,frame=video_cap.read()
            frame=recognize(frame,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",frame)
           
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
