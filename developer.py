from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("DEVELOPER")
        self.root.wm_iconbitmap("icon.ico")

        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman", 35,"bold"), bg="white", fg="blue")
        title_lbl.place(x=0,y=0,width=1480,height=45)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
        Back_Button.pack(side=RIGHT)

        img_top=Image.open("images/dev3.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=800,y=50,width=500,height=300)

        img_top1=Image.open("images/anu.png")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        dev_label=Label(main_frame,text="Hello, Anuradha Naidu here !",font=("times new roman",24,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="A sophomore pursuing Comp Engg.",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="I am an alpha MLSA'22,MS ENGAGE'22 mentee",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=70)

        dev_label=Label(main_frame,text="and an incoming GDSC lead'22",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=100)

        dev_label=Label(main_frame,text="I love CP,blockchain tech,AI,Web development",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=130)

        dev_label=Label(main_frame,text="Thank you for using my application!",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_label.place(x=0,y=160)







        


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
