from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import cv2


class Criminal:
	def __init__(self,root):
		self.root=root
		self.root.geometry('1300x700+0+0')
		self.root.title('CRIMINAL MANAGEMENT SYSTEM')
  
		#variables
		self.var_case_id=StringVar()
		self.var_criminal_no=StringVar()
		self.var_name=StringVar()
		self.var_middle_name=StringVar()
		self.var_arrest_date=StringVar()
		self.var_date_of_crime=StringVar()
		self.var_address=StringVar()
		self.var_age=StringVar()
		self.var_occupation=StringVar()
		self.var_birthMark=StringVar()
		self.var_crime_type=StringVar()
		self.var_last_name=StringVar()
		self.var_gender=StringVar()
		self.var_wanted=StringVar()

		lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM',font=('times new roman',40,'bold'),bg='black',fg='white')
		lbl_title.place(x=0,y=0,width=1530,height=70)

  
		

        #Logo
		img_logo=Image.open('images/Logo.png')
		img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
		self.photo_logo=ImageTk.PhotoImage(img_logo)

		self.logo=Label(self.root,image=self.photo_logo)
		self.logo.place(x=220,y=5,width=60,height=60)
  
		
		
  
		  
		#image_frame1
		img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
		img_frame.place(x=0,y=70,width=1530,height=130)

		img1=Image.open('images/poloce.webp')
		img1=img1.resize((540,160),Image.ANTIALIAS)
		self.photo1=ImageTk.PhotoImage(img1)

		self.img_1=Label(img_frame,image=self.photo1)
		self.img_1.place(x=0,y=0,width=540,height=160)


		#image_frame2
		img_2=Image.open('images/car.jpg')
		img_2=img_2.resize((540,160),Image.ANTIALIAS)
		self.photo2=ImageTk.PhotoImage(img_2)

		self.img_2=Label(img_frame,image=self.photo2)
		self.img_2.place(x=540,y=0,width=540,height=160)


		#image_frame3
		img_3=Image.open('images/police-2.webp')
		img_3=img_3.resize((540,160),Image.ANTIALIAS)
		self.photo3=ImageTk.PhotoImage(img_3)

		self.img_3=Label(img_frame,image=self.photo3)
		self.img_3.place(x=1080,y=0,width=540,height=160)

        #main Frame
		Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
		Main_frame.place(x=10,y=200,width=1500,height=560)

        #upper frame
		upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
		upper_frame.place(x=10,y=10,width=1480,height=270)

#  ======================Entries================
		#Case Id
		caseid=Label(upper_frame, text="Case ID:", font=("arial",11,"bold"),bg="White")
		caseid.grid(row=0,column=0,padx=2,sticky=W)
		caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=("arial",11,"bold"))
		caseentry.grid(row=0,column=1, padx=2,sticky=W)
  
		#Criminal No
		lbl_criminal_no=Label(upper_frame, text="Criminal NO:", font=("arial",11,"bold"),bg="White")
		lbl_criminal_no.grid(row=0,column=2,padx=2,sticky=W,pady=7)
		txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=("arial",11,"bold"))
		txt_criminal_no.grid(row=0,column=3, padx=2,pady=7)

		#Criminal name
		name=Label(upper_frame, text="Criminal Name:", font=("arial",11,"bold"),bg="White")
		name.grid(row=1,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=1,column=1, padx=2,sticky=W,pady=7)
       
       #Middle name
		name=Label(upper_frame, text="Middle Name:", font=("arial",11,"bold"),bg="White")
		name.grid(row=1,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_middle_name,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=1,column=3, padx=2,sticky=W,pady=7)
  
		#Arrest Date
		arrest_date=Label(upper_frame, text="Arrest Date:", font=("arial",11,"bold"),bg="White")
		arrest_date.grid(row=2,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=2,column=1, padx=2,sticky=W,pady=7)
  
		#Date of Crime
		name=Label(upper_frame, text="Date of Crime:", font=("arial",11,"bold"),bg="White")
		name.grid(row=2,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=2,column=3, padx=2,sticky=W,pady=7)
  
		#Address
		address=Label(upper_frame, text="Address:", font=("arial",11,"bold"),bg="White")
		address.grid(row=3,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=3,column=1, padx=2,sticky=W,pady=7)
  
		#Age
		age=Label(upper_frame, text="Age:", font=("arial",11,"bold"),bg="White")
		age.grid(row=3,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=3,column=3, padx=2,sticky=W,pady=7)
  
		#Occupution
		occupution=Label(upper_frame, text="Occupution:", font=("arial",11,"bold"),bg="White")
		occupution.grid(row=4,column=0,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=4,column=1, padx=2,sticky=W,pady=7)
  
		#Birth Mark
		birth_mark=Label(upper_frame, text="Birth Mark:", font=("arial",11,"bold"),bg="White")
		birth_mark.grid(row=4,column=2,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=4,column=3, padx=2,sticky=W,pady=7)
  
		#Crime Type
		crime_type=Label(upper_frame, text="Crime Type:", font=("arial",11,"bold"),bg="White")
		crime_type.grid(row=0,column=4,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=0,column=5, padx=2,sticky=W,pady=7)
  
		#Last Name
		last_name=Label(upper_frame, text="Last Name:", font=("arial",11,"bold"),bg="White")
		last_name.grid(row=1,column=4,padx=2,sticky=W,pady=7)
		txt_name=ttk.Entry(upper_frame,textvariable=self.var_last_name,width=22,font=("arial",11,"bold"))
		txt_name.grid(row=1,column=5, padx=2,sticky=W,pady=7)
  
		#gender
		gender=Label(upper_frame,font=("arial",11,"bold"),text="Gender:",bg="white")
		gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)
  
		#Wanted
		wanted=Label(upper_frame,font=("arial",11,"bold"),text="Most Wanted:",bg="white")
		wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)
  
		#Radio Button gender
		radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
		radio_frame_gender.place(x=730,y=90,width=190,height=30)
		male=Radiobutton(radio_frame_gender,variable=self.var_gender,text="Male",value="male",font=("arial",9,"bold"),bg="white")
		male.grid(row=0,column=0,padx=5,pady=2,sticky=W)
		female=Radiobutton(radio_frame_gender,variable=self.var_gender,text="FeMale",value="female",font=("arial",9,"bold"),bg="white")
		female.grid(row=0,column=1,padx=5,pady=2,sticky=W)
  
		#Radio Button wanted
		radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
		radio_frame_wanted.place(x=730,y=130,width=190,height=30)
		yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="Yes",value="yes",font=("arial",9,"bold"),bg="white")
		yes.grid(row=0,column=0,padx=5,pady=2,sticky=W)
		no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text="No",value="no",font=("arial",9,"bold"),bg="white")
		no.grid(row=0,column=1,padx=5,pady=2,sticky=W)
  		
		#Button	
		button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
		button_frame.place(x=5,y=200,width=830,height=45)
  

  
		#Add Button
		add=Button(button_frame,command=self.add_data,text="Record Save",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		add.grid(row=0,column=0,padx=3,pady=5)
	
		#Update Button
		update=Button(button_frame,command=self.update_data,text="Update",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		update.grid(row=0,column=1,padx=3,pady=5)
  
		#Delete Button
		delete=Button(button_frame,command=self.delete_data,text="Delete",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		delete.grid(row=0,column=2,padx=3,pady=5)
  
		#Clear Button
		clear=Button(button_frame,command=self.clear_data,text="Clear",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		clear.grid(row=0,column=3,padx=3,pady=5)
	
		#photo sample
		take_photo_btn=Button(button_frame, text="Take Photo sample", command=self.generate_dataset, width=20,font=("times new roman",12, "bold"),bg="blue", fg="white")
		take_photo_btn.grid(row=0, column=4,padx=3,pady=5)
        
  
		
  
		#right side image
		img_crime=Image.open('images/criminal.jpg')
		img_crime=img_crime.resize((470,245),Image.ANTIALIAS)
		self.photocrime=ImageTk.PhotoImage(img_crime)

		self.img_crime=Label(upper_frame,image=self.photocrime)
		self.img_crime.place(x=1000,y=0,width=470,height=245)
        
        #down frame
		down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Tabel',font=('times new roman',11,'bold'),fg='red',bg='white')
		down_frame.place(x=10,y=280,width=1480,height=270)

		 #search frame
		search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text=' Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
		search_frame.place(x=0,y=0,width=1470,height=60)
  
		search_by=Label(search_frame, text="Search By:", font=("arial",11,"bold"),bg="red",fg="white")
		search_by.grid(row=0,column=0,padx=2,sticky=W)
  

		self.var_com_search=StringVar()
		combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",11,"bold"),width=18,state="readonly")
		combo_search_box["value"]=("Select Option","Case_id","Criminal_no")
		combo_search_box.current(0)
		combo_search_box.grid(row=0,column=1,padx=2,sticky=W)

		self.var_search=StringVar()
		search=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("arial",11,"bold"))
		search.grid(row=0,column=2,padx=2,sticky=W)
  
		#search Button
		search=Button(search_frame,command=self.search_data,text="Search",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		search.grid(row=0,column=3,padx=2,sticky=W)
  
		#all Button
		all=Button(search_frame,command=self.fetch_data,text="Show All",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
		all.grid(row=0,column=4,padx=2,sticky=W)
  
		crime_agency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg="white",fg="crimson")
		crime_agency.grid(row=0,column=5,sticky=W,padx=50,pady=0)
  
		#table
  
		table_frame=Frame(down_frame,bd=2,relief=RIDGE)
		table_frame.place(x=0,y=60,width=1470,height=170)
  
		#Scroll Bar
		scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
		self.criminal_table=ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
  
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
  
		scroll_x.config(command=self.criminal_table.xview)
		scroll_y.config(command=self.criminal_table.yview)
  
		self.criminal_table.heading("1",text="CaseID")
		self.criminal_table.heading("2",text="CrimeNo")
		self.criminal_table.heading("3",text="Criminal Name")
		self.criminal_table.heading("4",text="Middle Name")
		self.criminal_table.heading("5",text="ArrestDate")
		self.criminal_table.heading("6",text="CrimeofDate")
		self.criminal_table.heading("7",text="Address")
		self.criminal_table.heading("8",text="Age")
		self.criminal_table.heading("9",text="Occupation")
		self.criminal_table.heading("10",text="Birth Mark")
		self.criminal_table.heading("11",text="Crime Type")
		self.criminal_table.heading("12",text="Last Name")
		self.criminal_table.heading("13",text="Gender")
		self.criminal_table.heading("14",text="Wanted")
  
		self.criminal_table["show"]="headings"
		self.criminal_table.column("1",width=100)
		self.criminal_table.column("2",width=100)
		self.criminal_table.column("3",width=100)
		self.criminal_table.column("4",width=100)
		self.criminal_table.column("5",width=100)
		self.criminal_table.column("6",width=100)
		self.criminal_table.column("7",width=100)
		self.criminal_table.column("8",width=100)
		self.criminal_table.column("9",width=100)
		self.criminal_table.column("10",width=100)
		self.criminal_table.column("11",width=100)
		self.criminal_table.column("12",width=100)
		self.criminal_table.column("13",width=100)
		self.criminal_table.column("14",width=100)
		

  
		self.criminal_table.pack(fill=BOTH,expand=1)

		self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

		self.fetch_data()

  
	#Add function
 
	def add_data(self):
		if self.var_case_id.get()=="":
			messagebox.showerror("Error","All Fields are required")
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
																											self.var_case_id.get(),
																											self.var_criminal_no.get(),
																											self.var_name.get(),
																											self.var_middle_name.get(),
																											self.var_arrest_date.get(),
																											self.var_date_of_crime.get(),
																											self.var_address.get(),
																											self.var_age.get(),
																											self.var_occupation.get(),
																											self.var_birthMark.get(),
																											self.var_crime_type.get(),
																											self.var_last_name.get(),
																											self.var_gender.get(),
																											self.var_wanted.get()
                 
																		
					
     
     
																										))
				conn.commit()
				self.fetch_data()
				self.clear_data()
				conn.close()
				messagebox.showinfo("Success","Criminal record has been added")
			except Exception as es:
				messagebox.showerror("Error",f"Due To{str(es)}")

	

	#fetch Data
	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from criminal")
		data=my_cursor.fetchall()
		if len(data)!=0:
			self.criminal_table.delete(*self.criminal_table.get_children())
			for i in data:
				self.criminal_table.insert("",END,values=i)
			conn.commit()
		conn.close()

	#get cursor
	def get_cursor(self,event=""):
		cursor_row=self.criminal_table.focus()
		content=self.criminal_table.item(cursor_row)
		data=content["values"]

		self.var_case_id.set(data[0])
		self.var_criminal_no.set(data[1])
		self.var_name.set(data[2])
		self.var_middle_name.set(data[3])
		self.var_arrest_date.set(data[4])
		self.var_date_of_crime.set(data[5])
		self.var_address.set(data[6])
		self.var_age.set(data[7])
		self.var_occupation.set(data[8])
		self.var_birthMark.set(data[9])
		self.var_crime_type.set(data[10])
		self.var_last_name.set(data[11])
		self.var_gender.set(data[12])
		self.var_wanted.set(data[13])


	#update
	def update_data(self):
		if self.var_case_id.get()=="":
			messagebox.showerror("Error","All Fields are required")
		else:
			try:
				update=messagebox.askyesno("Update","Are you sure update this criminal record")
				if update>0:
					conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
					my_cursor=conn.cursor()
					my_cursor.execute("update criminal set criminal_no=%s,name=%s,address=%s, middle_name=%s,arrest_date=%s,date_of_crime=%s,age=%s,occupation=%s,birthMark=%s,crime_type=%s,last_name=%s,gender=%s,wanted=%s where case_id=%s",(
																																																									
																																																									self.var_criminal_no.get(),
																																																									self.var_name.get(),
                                                                           																																							self.var_address.get(),
																																																									self.var_middle_name.get(),
																																																									self.var_arrest_date.get(),
																																																									self.var_date_of_crime.get(),
																																																									self.var_age.get(),
																																																									self.var_occupation.get(),
																																																									self.var_birthMark.get(),
																																																									self.var_crime_type.get(),
																																																									self.var_last_name.get(),
																																																									self.var_gender.get(),
																																																									self.var_wanted.get(),
																																																									self.var_case_id.get()



																																																								))
				else:
					if not update:
						return
				conn.commit()
				self.fetch_data()
				self.clear_data()
				conn.close()
				messagebox.showinfo("Success","Criminal record has been successfully updated")
			except Exception as es:
				messagebox.showerror("Error",f"Due To{str(es)}")


	#delete
	def delete_data(self):
		if self.var_case_id.get()=="":
			messagebox.showerror("Error","All Fields are required")
		else:
			try:
				delete=messagebox.askyesno("Delete","Are you sure delete this criminal record")
				if delete>0:

					conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
					my_cursor=conn.cursor()
					sql="delete from criminal where case_id=%s"
					value=(self.var_case_id.get(),)
					my_cursor.execute(sql,value)
				else:
					if not delete:
						return
				conn.commit()
				self.fetch_data()
				self.clear_data()
				conn.close()
				messagebox.showinfo("Success","Criminal record has been successfully deleted")
			except Exception as es:
				messagebox.showerror("Error",f"Due To{str(es)}")


	#clear
	def clear_data(self):
		self.var_case_id.set("")
		self.var_criminal_no.set("")
		self.var_name.set("")
		self.var_middle_name.set("")
		self.var_arrest_date.set("")
		self.var_date_of_crime.set("")
		self.var_address.set("")
		self.var_age.set("")
		self.var_occupation.set("")
		self.var_birthMark.set("")
		self.var_crime_type.set("")
		self.var_last_name.set("")
		self.var_gender.set("")
		self.var_wanted.set("")
  
	    # ============================Generate dataset or take a photo sample=====================              
        
	def generate_dataset(self):
		if self.var_case_id.get()=="" or self.var_name.get()=="" :
			messagebox.showerror("Error", "All Fields are Required",parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
				mycursor=conn.cursor()
				mycursor.execute("select * from criminal")
				myresult=mycursor.fetchall()
				id=0
				for x in myresult:
					id+=1
				mycursor.execute("update criminal set criminal_no=%s,name=%s,address=%s, middle_name=%s,arrest_date=%s,date_of_crime=%s,age=%s,occupation=%s,birthMark=%s,crime_type=%s,last_name=%s,gender=%s,wanted=%s where case_id=%s",(
																																																									
																																																									self.var_criminal_no.get(),
																																																									self.var_name.get(),
                                                                           																																							self.var_address.get(),
																																																									self.var_middle_name.get(),
																																																									self.var_arrest_date.get(),
																																																									self.var_date_of_crime.get(),
																																																									self.var_age.get(),
																																																									self.var_occupation.get(),
																																																									self.var_birthMark.get(),
																																																									self.var_crime_type.get(),
																																																									self.var_last_name.get(),
																																																									self.var_gender.get(),
																																																									self.var_wanted.get(),
																																																									self.var_case_id.get()



								                                                 
				  							)
                                     )   
				conn.commit()
				self.fetch_data()
				self.clear_data()
				conn.close()
        
 
                # =====================load predefined data of face from opencv=============
            
				face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

				def facecropped(img):
					gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
					faces=face_classifier.detectMultiScale(gray,1.3,3)

					for(x,y,w,h) in faces:
						facecropped=img[y:y+h, x:x+w]
						return facecropped
				capture=cv2.VideoCapture(0)
				img_id=0
				while True:
					ret,my_frame=capture.read()
					if facecropped(my_frame) is not None:
						img_id+=1
						face=cv2.resize(facecropped(my_frame),(350,350)) 
						face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
						file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
						cv2.imwrite(file_path,face)
						cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
						cv2.imshow("Cropped face",face)
					if cv2.waitKey(1)==13 or int(img_id)==100:
						break
				capture.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Result","Generating dataset completed successfully!!!!!")

			except Exception as es:
				messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

	#search
	def search_data(self):
		if self.var_com_search.get()=="":
			messagebox.showerror("Error","All Fields are required")

		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="Rutuj@0207",database="criminal")
				my_cursor=conn.cursor()
				my_cursor.execute("select * from criminal where " +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
				rows=my_cursor.fetchall()
				if len(rows)!=0:
					self.criminal_table.delete(*self.criminal_table.get_children())
					for i in rows:
						self.criminal_table.insert("",END,values=i)
				conn.commit()
				conn.close()
			except Exception as es:
				messagebox.showerror("Error",f"Due To{str(es)}")
    
 

if __name__=="__main__":
	root=Tk()
	obj=Criminal(root)
	root.mainloop()
	