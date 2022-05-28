from email.errors import MessageDefect
from logging import root
from re import I
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from cv2 import drawFrameAxes
from matplotlib.pyplot import title
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

from images.graph import Graph

mydata=[]
class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Pannel")
        self.root.wm_iconbitmap("icon.ico")

        #=====variables+++++
        self.var_atten_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        

        #first img
        img=Image.open("/Users/anuradhanaidu/Desktop/Face/images/pic1.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #secimg
        img1=Image.open("/Users/anuradhanaidu/Desktop/Face/images/face3.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        #bg img
        img3=Image.open("/Users/anuradhanaidu/Desktop/Face/images/pic3.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1480,height=45)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("times new roman",15,"bold"),width=20,bg="white",fg="green")
        Back_Button.pack(side=RIGHT)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1400,height=600)

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=690,height=580)

        img_left=Image.open("/Users/anuradhanaidu/Desktop/Face/images/face5.jpg")
        img_left=img_left.resize((690,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=690,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=180,width=688,height=370)
        #ATTENDANCE ID
        attendanceId_label=Label(left_inside_frame ,text="ATTENDANCE ID:",bg="white",font="comicsansns 11 bold")
        attendanceId_label.grid(row=0,column=0,padx=10,sticky=W)
  
        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font="comicsansns 11 bold")
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #roll
        roll_label=Label(left_inside_frame,text="Roll No:",bg="white",font="comicsansns 11 bold")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)
  
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)
        #name
        studentName_label=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        studentName_label.grid(row=1,column=0)
  
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8,sticky=W)

        #dept
        dep_label=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        dep_label.grid(row=1,column=2)
  
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        time_label.grid(row=2,column=0)
  
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        date_label.grid(row=2,column=2)
  
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=20,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

        #attend
        attendance_label=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 11 bold")
        attendance_label.grid(row=3,column=0)
  
        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly",width=20)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8,sticky=W)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=690,height=100)
 
        analysis_btn=Button(btn_frame,text="Analysis",command=self.analyse_data,width=20,font=("times new roman",16,"bold"),bg="white",fg="red")
        analysis_btn.grid(row=1,column=2)

        #save button
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",16,"bold"),bg="white",fg="blue")
        save_btn.grid(row=0,column=0)
       
        #update
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",16,"bold"),bg="white",fg="blue")
        update_btn.grid(row=0,column=1)

        #delete
        delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",16,"bold"),bg="white",fg="blue")
        delete_btn.grid(row=0,column=2)

        #reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",16,"bold"),bg="white",fg="blue")
        reset_btn.grid(row=0,column=3)

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=("times new roman",12,"bold"))
        right_frame.place(x=710,y=10,width=690,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=445)

        #======scroll bar===========================


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    
    #update data

    def update_data(self):
        if self.var_atten_id.get()=="" or self.var_attend_roll.get=="" or self.var_atten_name.get()=="" or self.var_attend_dep.get()=="" or self.var_atten_time.get()=="" or self.var_attend_date.get()=="" or self.var_atten_attendance.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(user='root',password='chocobar@6',host='localhost',database='facedb',port=3306)
                    mycursor=conn.cursor()
                    mycursor.execute("update attendance set Attendance ID=%s,Roll=%s,Name=%s,Department=%s,Time=%s,Date=%s,Attendance=%s where Attendance ID=%s",( 
                    self.var_atten_id.get(),
                    self.var_attend_roll.get(),
                    self.var_atten_name.get(),
                    self.var_attend_dep.get(),
                    self.var_atten_time.get(),
                    self.var_attend_date.get(),
                    self.var_atten_attendance.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

#===========fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(user='root',password='chocobar@6',host='localhost',database='facedb',port=3306)
        mycursor=conn.cursor()

        mycursor.execute("select * from attendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

  #====fetch data from import===================  
    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
          self.AttendanceReportTable.insert("",END,values=i)
          print(i)
          
    #import csv 
    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
      with open(fln.name) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
            mydata.append(i)
        self.fetchData(mydata)
    
    #export csv
    def exportCsv(self):
      try:
        if len(mydata)<1:
            messagebox.showerror("No Data","No Data found to export",parent=self.root)
            return False
        fln=filedialog.asksaveasfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln.name,mode="w",newline="") as myfile:
            exp_write=csv.writer(myfile,delimiter=",")
            for i in mydata:
                exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported to" +os.path.basename(fln.name)+"successfully")
      except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content['values']
      
      self.var_atten_id.set(rows[0])
      self.var_attend_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_attend_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_attend_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_attend_roll.set("")
      self.var_atten_name.set("")
      self.var_attend_dep.set("")
      self.var_atten_time.set("")
      self.var_attend_date.set("")
      self.var_atten_attendance.set("Status")

    def analyse_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Graph(self.new_window)

  
      






          
    
          
       
 
















      







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()