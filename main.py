from cgitb import text
import string
from time import strftime
import time
from tkinter import*
from tkinter import ttk
import tkinter
from datetime import datetime
from matplotlib.pyplot import title
from student import Student
from PIL import Image, ImageTk
import subprocess, sys
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x710+0+0")
       self.root.title("HOME PAGE")
       self.root.wm_iconbitmap("icon.ico")

       #first img
       img=Image.open("images/pic1.jpg")
       img=img.resize((500,130),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)

       #secimg
       img1=Image.open("images/face3.jpg")
       img1=img1.resize((500,130),Image.ANTIALIAS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)

       #thirdimg
       img2=Image.open("images/pic2.jpg")
       img2=img2.resize((500,130),Image.ANTIALIAS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=500,height=130)

       #bg img
       img3=Image.open("images/pic3.png")
       img3=img3.resize((1530,710),Image.ANTIALIAS)
       self.photoimg3=ImageTk.PhotoImage(img3)

       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35,"bold"), bg="white", fg="purple")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       #time======================================
       def time():
          string = strftime('%H:%M:%S %p')
          lbl.config(text = string)
          lbl.after(1000, time)
       lbl = Label(title_lbl,font=('times new roman',20,'bold'),background='white',foreground='blue')
       lbl.place(x=5,y=0,width=110,height=50)
       time()
      
       
       
       #student button
       img4=Image.open("images/face6.jpg")
       img4=img4.resize((220,220),Image.ANTIALIAS)
       self.photoimg4=ImageTk.PhotoImage(img4)

       b1=Button(bg_img, image=self.photoimg4,command=self.student,cursor="hand2")
       b1.place(x=200,y=100,width=220,height=220)

       b1_1=Button(bg_img, text="STUDENT DETAILS",command=self.student, cursor="hand2",font=("times new roman",15,"bold"),bg="yellow",fg="purple")
       b1_1.place(x=200,y=300,width=220,height=40)

       #detect face 
       
       img5=Image.open("images/face7.jpg")
       img5=img5.resize((220,220),Image.ANTIALIAS)
       self.photoimg5=ImageTk.PhotoImage(img5)

       b1=Button(bg_img, image=self.photoimg5,cursor="hand2",command=self.face_data)
       b1.place(x=500,y=100,width=220,height=220)

       b1_1=Button(bg_img, text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=500,y=300,width=220,height=40)
       
       #attendance
       img6=Image.open("images/face9.jpg")
       img6=img6.resize((220,220),Image.ANTIALIAS)
       self.photoimg6=ImageTk.PhotoImage(img6)

       b1=Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.attendance_data)
       b1.place(x=800,y=100,width=220,height=220)

       b1_1=Button(bg_img, text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=800,y=300,width=220,height=40)

       #help
       
       img7=Image.open("images/help.jpg")
       img7=img7.resize((220,220),Image.ANTIALIAS)
       self.photoimg7=ImageTk.PhotoImage(img7)

       b1=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.help_data)
       b1.place(x=1100,y=100,width=220,height=220)

       b1_1=Button(bg_img, text="HELP DESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=1100,y=300,width=220,height=40)

       #train data

       img8=Image.open("images/face10.jpeg")
       img8=img8.resize((220,220),Image.ANTIALIAS)
       self.photoimg8=ImageTk.PhotoImage(img8)

       b1=Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.train_data)
       b1.place(x=200,y=400,width=220,height=220)

       b1_1=Button(bg_img, text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=200,y=600,width=220,height=40)

       #photos

       img9=Image.open("images/fac2.jpeg")
       img9=img9.resize((220,220),Image.ANTIALIAS)
       self.photoimg9=ImageTk.PhotoImage(img9)

       b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
       b1.place(x=500,y=400,width=220,height=220)

       b1_1=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=500,y=600,width=220,height=40)

       #developer

       img10=Image.open("images/developer.jpg")
       img10=img10.resize((220,220),Image.ANTIALIAS)
       self.photoimg10=ImageTk.PhotoImage(img10)

       b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
       b1.place(x=800,y=400,width=220,height=220)

       b1_1=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=800,y=600,width=220,height=40)

       #exit

       img11=Image.open("images/exit.jpg")
       img11=img11.resize((220,220),Image.ANTIALIAS)
       self.photoimg11=ImageTk.PhotoImage(img11)

       b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.iExit)
       b1.place(x=1100,y=400,width=220,height=220)

       b1_1=Button(bg_img, text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="yellow", fg="purple")
       b1_1.place(x=1100,y=600,width=220,height=40)



    def open_img(self):
       
       opener = "open" if sys.platform == "darwin" else "xdg-open"
       subprocess.call([opener,"data"])
       
      #======function buttons======= 
   
    def student(self):
       self.new_window=Toplevel(self.root)
       self.app=Student(self.new_window)
    
    def train_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Train(self.new_window)
    
    def face_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition(self.new_window)

    
    def attendance_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Attendance(self.new_window)
   
    def developer_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Developer(self.new_window)

    def help_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Help(self.new_window)
    


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ?",parent=self.root)
       if self.iExit >0:
          self.root.destroy()
       else:
          return
        


if __name__ == "__main__":
   root=Tk()
   app=Face(root)
   root.mainloop()

      

      
       


         
