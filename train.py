from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import Directory
from PIL import UnidentifiedImageError
import mysql.connector
import cv2
import os
from sys import path
import numpy as np
from PIL import Image,ImageTk

class Train:
    def __init__(self,root):
    
       self.root=root
       self.root.geometry("1530x710+0+0")
       self.root.title("TRAIN")
       self.root.wm_iconbitmap("icon.ico")

       title_lbl=Label(self.root,text="TRAIN DATA SET", font=("times new roman", 35,"bold"), bg="white", fg="purple")
       title_lbl.place(x=0,y=0,width=1480,height=45)

       Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
       Back_Button.pack(side=RIGHT)

       img_top=Image.open("images/collage.png")
       img_top=img_top.resize((1530,325),Image.ANTIALIAS)
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl=Label(self.root,image=self.photoimg_top)
       f_lbl.place(x=0,y=55,width=1530,height=325)

       #button
       b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",50,"bold"),bg="white",fg="red")
       b1_1.place(x=0,y=380,width=1530,height=60)

       img_bottom=Image.open("images/train1.jpg")
       img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
       self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

       f_lbl=Label(self.root,image=self.photoimg_bottom)
       f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        if '.DS_Store' in path:
            path.remove('.DS_Store')

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayscale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split(".")[2])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
         
         #=========Train the classifier and save==============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")
        
 

if __name__ == "__main__":
   root=Tk()
   obj=Train(root)
   root.mainloop()
