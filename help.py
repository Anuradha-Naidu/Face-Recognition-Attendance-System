from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("HELP DESK")
        self.root.wm_iconbitmap("icon.ico")

        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman", 35,"bold"), bg="white", fg="blue")
        title_lbl.place(x=0,y=0,width=1480,height=45)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
        Back_Button.pack(side=RIGHT)

        img_top=Image.open("images/help3.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        help_label=Label(f_lbl,text="Email ID: anuradhaknaidu6@gmail.com",font=("times new roman",30,"bold"),bg="black",fg="white")
        help_label.place(x=500,y=300)

        help_label=Label(f_lbl,text="LinkedIn: www.linkedin.com/in/naidu-anuradha612001",font=("times new roman",30,"bold"),bg="black",fg="white")
        help_label.place(x=500,y=400)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

