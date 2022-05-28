from tkinter import RIGHT, Button, Label, Tk
import matplotlib.pyplot as plt
import pandas as pd


from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Graph:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Analysis")
        self.root.wm_iconbitmap("icon.ico")

        img3=Image.open("/Users/anuradhanaidu/Desktop/Face/images/pic3.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(self.root,text="Student Analysis",font=("times new roman", 35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1480,height=45)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
        Back_Button.pack(side=RIGHT)

        plt.style.use('bmh')
        df = pd.read_csv('anuradha.csv')

        x = df['Attendance']
        y = df['Teacher']

        plt.xlabel('Attendance',fontsize=18)
        plt.ylabel('Teacher',fontsize=16)
        plt.bar(x,y)



        plt.show()


if __name__ == "__main__":
    root=Tk()
    obj=Graph(root)
    root.mainloop()