from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from criminal import Criminal
import os
from train import Train
from facerecognition import Face_Recognition
from records import Records


class Criminal_Face_Recogniation:
	def __init__(self,root):
		self.root=root
		self.root.geometry('1530x70+0+0')	
		self.root.title("Criminal Face Recognition")

		#img1
		img=Image.open("images/p1.jpg")
		img=img.resize((500,130),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		f_lbl=Label(self.root,image=self.photoimg)
		f_lbl.place(x=0,y=0,width=500,height=130)

		#img2
		img1=Image.open("images/criminal1.jpg")
		img1=img1.resize((500,130),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		f_lbl=Label(self.root,image=self.photoimg1)
		f_lbl.place(x=450,y=0,width=450,height=130)


		#img3
		img3=Image.open("images/face.jpg")
		img3=img3.resize((500,130),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		f_lbl=Label(self.root,image=self.photoimg3)
		f_lbl.place(x=1000,y=0,width=500,height=130)

		#background img
		img2=Image.open("images/bg.jpg")
		img2=img2.resize((1530,710),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		bg_img=Label(self.root,image=self.photoimg2)
		bg_img.place(x=0,y=130,width=1530,height=710)


		title_lbl=Label(bg_img,text="Criminal Face Recognition System",font=("times new roman",35,"bold"),bg="black",fg="white")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		#criminal details
		img4=Image.open("images/c2.jpg")
		img4=img4.resize((220,220),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		b1=Button(bg_img,image=self.photoimg4,command=self.criminal_details,cursor="hand2")
		b1.place(x=300,y=100,width=220,height=220)

		b1_1=Button(bg_img,text="Criminal Details",command=self.criminal_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
		b1_1.place(x=300,y=300,width=220,height=40)

		#detect face 
		img5=Image.open("images/d1.jpg")
		img5=img5.resize((220,220),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
		b2.place(x=600,y=100,width=220,height=220)

		b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
		b2_1.place(x=600,y=300,width=220,height=40)

		#photo 
		img6=Image.open("images/p2.jpg")
		img6=img6.resize((220,220),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
		b3.place(x=900,y=100,width=220,height=220)

		b3_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
		b3_1.place(x=900,y=300,width=220,height=40)


		#train data 
		img8=Image.open("images/t1.jpg")
		img8=img8.resize((220,220),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		b6=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
		b6.place(x=300,y=400,width=220,height=220)

		b6_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
		b6_1.place(x=300,y=600,width=220,height=40)
  
  
		#All data 
		img9=Image.open("images/r1.png")
		img9=img9.resize((220,220),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.criminal_data)
		b5.place(x=600,y=400,width=220,height=220)

		b5_1=Button(bg_img,text="All Records",cursor="hand2",command=self.criminal_data,font=("times new roman",15,"bold"),bg="white",fg="black")
		b5_1.place(x=600,y=600,width=220,height=40)


		#Exit 
		img7=Image.open("images/e1.jpg")
		img7=img7.resize((220,220),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.exit)
		b4.place(x=900,y=400,width=220,height=220)

		b4_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="white",fg="black")
		b4_1.place(x=900,y=600,width=220,height=40)

	def open_img(self):
		os.startfile("data")
  
	def exit(self):
		self.exit=tkinter.messagebox.askyesno("Criminal Management","Are you sure exit this System",parent=self.root)
		if 	self.exit>0:
			self.root.destroy()
		else:
			return
		

	#function button

	def criminal_details(self):
		self.new_window=Toplevel(self.root)
		self.app=Criminal(self.new_window)

	def train_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Train(self.new_window)

	def face_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Face_Recognition(self.new_window)
  
	def criminal_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Records(self.new_window)






if __name__=="__main__":
	root=Tk()
	obj=Criminal_Face_Recogniation(root)
	root.mainloop()