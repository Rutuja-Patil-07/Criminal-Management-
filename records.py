from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Records:
	def __init__(self,root):
		self.root=root
		self.root.geometry('1300x700+0+0')
		self.root.title('CRIMINAL MANAGEMENT SYSTEM')
  
		self.var_id=StringVar()
		self.var_criminalno=StringVar()
		self.var_name=StringVar()
		self.var_age=StringVar()
		self.var_arrestdate=StringVar()
		self.var_crimedate=StringVar()
		self.var_address=StringVar()
		self.var_occupation=StringVar()
  
        #image1
		img1=Image.open('images/c3.jpg')
		img1=img1.resize((800,200),Image.ANTIALIAS)
		self.photo1=ImageTk.PhotoImage(img1)

		f_lbl=Label(self.root,image=self.photo1)
		f_lbl.place(x=0,y=0,width=800,height=200)


		#image2
		img_2=Image.open('images/c4.jpg')
		img_2=img_2.resize((800,200),Image.ANTIALIAS)
		self.photo2=ImageTk.PhotoImage(img_2)

		f_lbl=Label(self.root,image=self.photo2)
		f_lbl.place(x=800,y=0,width=800,height=200)
  
        #background img
		img3=Image.open("images/bg.jpg")
		img3=img3.resize((1530,710),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=200,width=1530,height=710)

		lbl_title=Label(bg_img,text='CRIMINAL RECORDS',font=('times new roman',40,'bold'),bg='black',fg='white')
		lbl_title.place(x=0,y=0,width=1530,height=45)
  
        #main Frame
		Main_frame=Frame(bg_img,bd=2,relief=RIDGE,bg='white')
		Main_frame.place(x=20,y=55,width=1530,height=710)
        #left frame
		left_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Records',font=('times new roman',11,'bold'),fg='black',bg='white')
		left_frame.place(x=10,y=10,width=730,height=580)

		left_inside=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
		left_inside.place(x=0,y=135,width=720,height=370)
  
        
  
  
  
        #  ======================Entries================
		#Case Id
		caseid=Label(left_inside, text="Case ID:", font=("arial",11,"bold"),bg="White")
		caseid.grid(row=0,column=0,padx=2,sticky=W)
		caseentry=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		caseentry.grid(row=0,column=1, padx=2,sticky=W)
  
		#Criminal No
		lbl_criminal_no=Label(left_inside, text="Criminal NO:", font=("arial",11,"bold"),bg="White")
		lbl_criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)
		txt_criminal_no=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_criminal_no.grid(row=0,column=3, padx=2,pady=7)

		#Criminal name
		name=Label(left_inside, text="Criminal Name:", font=("arial",11,"bold"),bg="White")
		name.grid(row=1,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=1,column=1, padx=3,sticky=W,pady=8)
       
       
  
		#Arrest Date
		arrest_date=Label(left_inside, text="Arrest Date:", font=("arial",11,"bold"),bg="White")
		arrest_date.grid(row=2,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=2,column=1, padx=2,sticky=W,pady=7)
  
		#Date of Crime
		name=Label(left_inside, text="Date of Crime:", font=("arial",11,"bold"),bg="White")
		name.grid(row=2,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=2,column=3, padx=2,sticky=W,pady=7)
  
		#Address
		address=Label(left_inside, text="Address:", font=("arial",11,"bold"),bg="White")
		address.grid(row=3,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=3,column=1, padx=2,sticky=W,pady=7)
  
		#Age
		age=Label(left_inside, text="Age:", font=("arial",11,"bold"),bg="White")
		age.grid(row=1,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=1,column=3, padx=2,sticky=W,pady=7)
  
		#Occupution
		occupution=Label(left_inside, text="Occupution:", font=("arial",11,"bold"),bg="White")
		occupution.grid(row=3,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(left_inside,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=3,column=3, padx=2,sticky=W,pady=7)
  
        #Button	
		button_frame=Frame(left_inside,bd=2,relief=RIDGE,bg="white")
		button_frame.place(x=5,y=300,width=620,height=45)
  

  
		#import Button
		add=Button(button_frame,text="Import csv",command=self.importCsv, font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		add.grid(row=0,column=0,padx=3,pady=5)
	
		#export Button
		update=Button(button_frame,text="Export csv", command=self.ExportCsv,font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		update.grid(row=0,column=1,padx=3,pady=5)
  
		#update Button
		delete=Button(button_frame,text="Update",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		delete.grid(row=0,column=2,padx=3,pady=5)
  
		#reset Button
		clear=Button(button_frame,text="Reset", command=self.resetdata, font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		clear.grid(row=0,column=3,padx=3,pady=5)

  
  
        #right frame
		right_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Record Details',font=('times new roman',11,'bold'),fg='black',bg='white')
		right_frame.place(x=750,y=10,width=720,height=580)
	
		table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
		table_frame.place(x=5,y=5,width=700,height=455)
  
		# =======scroll bar table=========
		scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
  
		self.CriminalReportTable=ttk.Treeview(table_frame,column=("id","criminal_no","criminal_name","age","arrest_date","date_of_crime","address","occupation"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
  
		scroll_x.config(command=self.CriminalReportTable.xview)
		scroll_y.config(command=self.CriminalReportTable.yview)
  
		self.CriminalReportTable.heading("id",text="Criminal ID")
		self.CriminalReportTable.heading("criminal_no",text="Criminal No")
		self.CriminalReportTable.heading("criminal_name",text="Criminal Name")
		self.CriminalReportTable.heading("age",text="Age")
		self.CriminalReportTable.heading("arrest_date",text="Arrest Date")
		self.CriminalReportTable.heading("date_of_crime",text="Date of Crime")
		self.CriminalReportTable.heading("address",text="Address")
		self.CriminalReportTable.heading("occupation",text="Occupation")
  
		self.CriminalReportTable["show"]="headings"
		self.CriminalReportTable.column("id",width=100)
		self.CriminalReportTable.column("criminal_no",width=100)
		self.CriminalReportTable.column("criminal_name",width=100)
		self.CriminalReportTable.column("age",width=100)
		self.CriminalReportTable.column("arrest_date",width=100)
		self.CriminalReportTable.column("date_of_crime",width=100)
		self.CriminalReportTable.column("address",width=100)
		self.CriminalReportTable.column("occupation",width=100)

  
		self.CriminalReportTable.pack(fill=BOTH,expand=1)

		#====fetch data========
	def fetchdata(self,rows):
		self.CriminalReportTable.delete(*self.CriminalReportTable.get_children())
		for i in rows:
			self.CriminalReportTable.insert("",END,values=i)


        # ==================import data===============

	def importCsv(self):
		global mydata
		mydata.clear()
		fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
		with open(fln) as myfile:
			csvread=csv.reader(myfile, delimiter=",")
			for i in csvread:
				mydata.append(i)
			self.fetchdata(mydata)
   
   
#    ================export data================
	def ExportCsv(self):
		try:
			if len(mydata)<1:
				messagebox.showerror("Nodata","No Data Found to Export",parent=self.root)
				return False
			fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="OPEN CSV", filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
			with open(fln,mode="w",newline="") as myfile:
				csvwrite=csv.writer(myfile,delimiter=",")
				for i in mydata:
					csvwrite.writerow(i)
				messagebox.showinfo("data"," Your Data Exported to "+os.path.basename(fln)+"SuccesFully....")
		except Exception as es:
				messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
	
	def getcursor(self, event=""):
		cursor_row=self.CriminalReportTable.focus()
		content=self.CriminalReportTable.item(cursor_row)
		rows=content['values']
		self.var_id.set(rows[0])
		self.var_criminalno.set(rows[1])
		self.var_name.set(rows[2])
		self.var_age.set(rows[3])
		self.var_arrestdate.set(rows[4])
		self.var_crimedate.set(rows[5])
		self.var_address.set(rows[6])
		self.var_occupation.set(rows[7])
  
	# =================reset data=====================
	def resetdata(self):
		self.var_id.set("")
		self.var_criminalno.set("")
		self.var_name.set("")
		self.var_age.set("")
		self.var_arrestdate.set("")
		self.var_crimedate.set("")
		self.var_address.set("")
		self.var_occupation.set("")
    	
     
  
if __name__=="__main__":
	root=Tk()
	obj=Records(root)
	root.mainloop()
	