from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import filedialog

window = Tk()
window.title("Health Record Management")
window.iconbitmap("icon.png")
window.geometry("1077x800")
window.configure(background='#A9D0F5')

frame1 = LabelFrame(window,background="#A9D0F5")
frame1.grid(row=0,column=0,columnspan=3)

image1 = ImageTk.PhotoImage(Image.open("img1.jpg"))
my_label = Label(frame1,image=image1)
my_label.grid(row=0,column=0,columnspan=3)





#frame2 = LabelFrame(window,background="#A9D0F5")
#frame2.grid(row=2,column=1,rowspan=2)

#image2 = ImageTk.PhotoImage(Image.open("img3.png"))
#my_label1 = Label(frame2,image=image2)
#my_label1.grid(row=0,column=0,rowspan=2)



def patient():

	window1 = Tk()
	window1.title("Registration for patients")
	window1.iconbitmap("icon.png")
	window1.geometry("430x470")
	window1.configure(background="#A9D0F5")

	my_label = Label(window1,text="Welcome to the Registration Department\nPlease fill the following items to register.\n",bg="#A9D0F5")
	my_label.config(font=("Arial Black",13))
	my_label.grid(row=0,column=0,columnspan=2)

	conn = sqlite3.connect("Health Care.db")
	c = conn.cursor()

	'''
	c.execute("""CREATE TABLE Patient(

				first_name text,
				last_name text,
				address text,
				contact_num integer,
				email text,
				problem text
				)""")
	'''

	def register():

		global id_box

		conn = sqlite3.connect("Health Care.db")
		c = conn.cursor()

		c.execute("INSERT INTO Patient VALUES(:f_name,:l_name,:address,:con_num,:email,:problem)",
			{
				"f_name": f_name_box.get(),
				"l_name": l_name_box.get(),
				"address": address_box.get(),
				"con_num": con_num_box.get(),
				"email": email_box.get(),
				"problem": problem_box.get()
			})

		f_name_box.delete(0,END)
		l_name_box.delete(0,END)
		address_box.delete(0,END)
		con_num_box.delete(0,END)
		email_box.delete(0,END)
		problem_box.delete(0,END)

		messagebox.showinfo("Hey There!","Your information was recorded successfully..!\nWe will contact you in the given information.")

		def check():
			conn = sqlite3.connect("Health Care.db")
			c = conn.cursor()

			c.execute("SELECT *,oid FROM Patient")
			records = c.fetchall()
			print_record  = ""

			for record in records:
				print_record = str(record)

			print_label = Label(window1,text=print_record)
			print_label.grid(row=9,column=0,columnspan=2)

			def deloredit():
				my_label2 = Label(window1,text="Type your oid",bg="#A9D0F5")
				my_label2.config(font=("Arial Black",8))
				my_label2.grid(row=11,column=0)

				id_box = Entry(window1)
				id_box.insert(0,"oid is the last num in your record")
				id_box.grid(row=11,column=1,ipadx=30)

				def delete():
					conn  = sqlite3.connect("Health Care.db")
					c = conn.cursor()

					response = messagebox.askyesno("Confirmation box","Are you sure you want to delete the record?")
					if response == 1:
						c.execute("DELETE from Patient WHERE oid=" + id_box.get())
					id_box.delete(0,END)

					conn.commit()
					conn.close()

				def edit():
					
					global window2

					window2 = Tk()
					window2.iconbitmap("icon.png")
					window2.title("Update page")
					window2.geometry("400x400")
					window2.configure(background="#A9D0F5")

					conn = sqlite3.connect("Health Care.db")
					c = conn.cursor()

					c.execute("SELECT * FROM Patient WHERE oid=" + id_box.get())

					global f_name_window2
					global l_name_window2
					global address_window2
					global con_num_window2
					global email_window2
					global problem_window2

					lbl = Label(window2,text="Update page for database",bg="#A9D0F5")
					lbl.config(font=("Arial Black",13))
					lbl.grid(row=0,column=0,columnspan=2)

					f_name_label = Label(window2,text="First Name",bg="#A9D0F5")
					f_name_label.config(font=("Arial Black",8))
					f_name_label.grid(row=1,column=0)

					l_name_label = Label(window2,text="Last Name",bg="#A9D0F5")
					l_name_label.config(font=("Arial Black",8))
					l_name_label.grid(row=2,column=0)

					address_label = Label(window2,text="Address",bg="#A9D0F5")
					address_label.config(font=("Arial Black",8))
					address_label.grid(row=3,column=0)

					con_num_label = Label(window2,text="Contact Number",bg="#A9D0F5")
					con_num_label.config(font=("Arial Black",8))
					con_num_label.grid(row=4,column=0)

					email_label = Label(window2,text="Email",bg="#A9D0F5")
					email_label.config(font=("Arial Black",8))
					email_label.grid(row=5,column=0)

					problem_label = Label(window2,text="Your Problem:",bg="#A9D0F5")
					problem_label.config(font=("Arial Black",8))
					problem_label.grid(row=6,column=0)


					f_name_window2 = Entry(window2)
					f_name_window2.grid(row=1,column=1,ipadx=30)

					l_name_window2 = Entry(window2)
					l_name_window2.grid(row=2,column=1,ipadx=30)

					address_window2 = Entry(window2)
					address_window2.grid(row=3,column=1,ipadx=30)

					con_num_window2 = Entry(window2)
					con_num_window2.grid(row=4,column=1,ipadx=30)

					email_window2 = Entry(window2)
					email_window2.grid(row=5,column=1,ipadx=30)

					problem_window2 = Entry(window2)
					problem_window2.grid(row=6,column=1,ipadx=30)

					records = c.fetchall()

					for record in records:
						f_name_window2.insert(0,record[0])
						l_name_window2.insert(0,record[1])
						address_window2.insert(0,record[2])
						con_num_window2.insert(0,record[3])
						email_window2.insert(0,record[4])
						problem_window2.insert(0,record[5])

					def update():
						
						conn = sqlite3.connect("Health Care.db")
						c = conn.cursor()

						response1 = messagebox.askyesno("Confirmation box","Are you sure you want to update the re-newed data?")

						if response1 == 1:
							record_id = id_box.get()

							c.execute("""UPDATE Patient SET 
								first_name = :first,
								last_name = :last,
								address = :address,
								contact_num = :con_num,
								email = :email,
								problem = :problem

								WHERE oid = :oid""",
								{
									"first": f_name_window2.get(),
									"last": l_name_window2.get(),
									"address": address_window2.get(),
									"con_num": con_num_window2.get(),
									"email": email_window2.get(),
									"problem": problem_window2.get(),
									"oid": record_id
								})

						conn.commit()
						conn.close()

						window2.destroy()

					submit_button = Button(window2,text="Update",bg="#80FF00",command=update)
					submit_button.config(font=("Forte",12))
					submit_button.grid(row=7,column=0,columnspan=2,pady=10)

					def exit():
						response = messagebox.askyesno("Confirmation Box","Are you sure you want to exit the program?")
						if response == 1:
							window2.withdraw()

					exit_button = Button(window2,text="Exit",command=exit,bg="#A9D0F5")
					exit_button.config(font=("Forte",15))
					exit_button.grid(row=8,column=0,columnspan=2,padx=10,pady=5,ipadx=30,ipady=5)


					conn.commit()
					conn.close()







				delete_button = Button(window1,text="Delete Record",bg="#FA5882",command = delete).grid(row=12,column=0,ipadx=20,ipady=5,pady=5)
				update_button = Button(window1,text="Edit Record",bg="#FFFF00",command = edit).grid(row=12,column=1,ipadx=20,ipady=5,pady=5)

			delete_edit_button = Button(window1,text="Delete/Edit the data?",command = deloredit,bg="#FFFF00")
			delete_edit_button.grid(row=10,column=0,columnspan=2,pady=10)

			conn.commit()
			conn.close()

		show_button = Button(window1,text="Check your record",command = check)
		show_button.config(font=("Arial",10))
		show_button.grid(row=8,column=0,columnspan=2)

		def exit():
			response = messagebox.askyesno("Confirmation Box","Are you sure you want to exit the program?")
			if response == 1:
				window1.withdraw()

		exit_button = Button(window1,text="Exit",command=exit,bg="#A9D0F5")
		exit_button.config(font=("Forte",15))
		exit_button.grid(row=13,column=0,columnspan=2,padx=10,pady=5,ipadx=30,ipady=5)

		conn.commit()
		conn.close()


	f_name_label = Label(window1,text="First Name",bg="#A9D0F5")
	f_name_label.config(font=("Arial Black",8))
	f_name_label.grid(row=1,column=0)

	l_name_label = Label(window1,text="Last Name",bg="#A9D0F5")
	l_name_label.config(font=("Arial Black",8))
	l_name_label.grid(row=2,column=0)

	address_label = Label(window1,text="Address",bg="#A9D0F5")
	address_label.config(font=("Arial Black",8))
	address_label.grid(row=3,column=0)

	con_num_label = Label(window1,text="Contact Number",bg="#A9D0F5")
	con_num_label.config(font=("Arial Black",8))
	con_num_label.grid(row=4,column=0)

	email_label = Label(window1,text="Email",bg="#A9D0F5")
	email_label.config(font=("Arial Black",8))
	email_label.grid(row=5,column=0)

	problem_label = Label(window1,text="Your Problem:",bg="#A9D0F5")
	problem_label.config(font=("Arial Black",8))
	problem_label.grid(row=6,column=0)


	f_name_box = Entry(window1)
	f_name_box.grid(row=1,column=1,ipadx=30)

	l_name_box = Entry(window1)
	l_name_box.grid(row=2,column=1,ipadx=30)

	address_box = Entry(window1)
	address_box.grid(row=3,column=1,ipadx=30)

	con_num_box = Entry(window1)
	con_num_box.grid(row=4,column=1,ipadx=30)

	email_box = Entry(window1)
	email_box.grid(row=5,column=1,ipadx=30)

	problem_box = Entry(window1)
	problem_box.grid(row=6,column=1,ipadx=30)


	submit_button = Button(window1,text="Register",bg="#80FF00",command=register)
	submit_button.config(font=("Forte",12))
	submit_button.grid(row=7,column=0,columnspan=2,pady=10)



	conn.commit()
	conn.close()










def department():

	global usrnm
	global psswd

	window3 = Toplevel()
	window3.title("Department Page")
	#window3.iconbitmap("icon.png")
	window3.geometry("400x400")
	window3.configure(background="#A9D0F5")


	login_label = Label(window3,text="Please login first..",bg="#A9D0F5")
	login_label.config(font=("Arial Black",20),fg="#AEB404")
	login_label.grid(row=0,column=0,columnspan=2,ipady=10)

	rndm = Label(window3,text="                    ",bg="#A9D0F5").grid(row=1,column=0)

	login_frame = LabelFrame(window3,bg="#FFFFFF")
	login_frame.grid(row=1,column=1,columnspan=2)

	my_login_image = ImageTk.PhotoImage(Image.open("img2.png"))
	my_user_image = ImageTk.PhotoImage(Image.open("user.png"))
	my_pass_image = ImageTk.PhotoImage(Image.open("pass.png"))

	img_label = Label(login_frame,image=my_login_image,borderwidth=0)
	img_label.grid(row=0,column=0,columnspan=2)

	usrnm = StringVar()
	psswd = StringVar()

	user_label = Label(login_frame,text="Username",image=my_user_image,compound=LEFT,font=("Arial Black",10),bg="#FFFFFF").grid(row=1,column=0)
	user_box = Entry(login_frame,textvariable=usrnm,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=(10,5))

	pass_label = Label(login_frame,text="Password",image=my_pass_image,compound=LEFT,font=("Arial Black",10),bg="#FFFFFF").grid(row=2,column=0)
	pass_box = Entry(login_frame,textvariable=psswd,relief=SUNKEN).grid(row=2,column=1,pady=(10,20),padx=(10,5))

	def login():

		username = "Project"
		password = "12345678"


		global id_box

		#usrnm = user_box.get()
		#psswd = pass_box.get()

		if usrnm.get() == "" or psswd.get() == "":
			messagebox.showwarning("Sorry!","You must fill the username and password in order to login")

		elif usrnm.get() == username and psswd.get() == password:
			
			window4 = Tk()
			window4.title("Check Appointments")
			window4.geometry=("470x500")
			window4.configure(background="#A9D0F5")

			conn = sqlite3.connect("Health Care.db")
			c = conn.cursor()

			Label(window4,text="Here are the all appointment records of patients\n",font=("Arial Black",15),fg="#000000",bg="#A9D0F5").grid(row=0,column=0,pady=(10,20),columnspan=2)

			c.execute("SELECT *,oid FROM Patient")

			records = c.fetchall()
			print_record = ""

			for record in records:
				print_record += str(record) + "\n"

			print_label = Label(window4,text=print_record).grid(row=1,column=0,columnspan=2)

			id_box = Entry(window4,relief=SUNKEN)
			id_box.grid(row=2,column=1,pady=10,padx=(10,100))

			def dlt():
				conn  = sqlite3.connect("Health Care.db")
				c = conn.cursor()

				response = messagebox.askyesno("Confirmation box","Are you sure you want to remove this record from the records?")
				if response ==1:
					c.execute("DELETE FROM Patient WHERE oid=" + id_box.get())
				
				id_box.delete(0,END)

				conn.commit()
				conn.close()



			oid_label = Label(window4,text="Enter the oid",bg="#A9D0F5",font=("Arial Black",8)).grid(row=2,column=0,pady=10,padx=(100,10))


			#id_box = Entry(window4,relief=SUNKEN)
			#id_box.grid(row=2,column=1,pady=10,padx=(10,100))
			oid_button = Button(window4,text="Done Treatment",command=dlt,bg="#80FF00",font=("Forte",15)).grid(row=3,column=0,padx=15)

			exit_button = Button(window4,text="Exit",command= window4.quit,bg="#A9D0F5")
			exit_button.config(font=("Forte",15))
			exit_button.grid(row=4,column=1,padx=10,pady=5,ipadx=30,ipady=5)


			window3.withdraw()


			conn.commit()
			conn.close()

		else:
			messagebox.showerror("Sorry!","Invalid username or password")


	def forget():
		messagebox.showinfo("Sorry!","You need to contact to the service provider:)")

	def exit():
		response = messagebox.askyesno("Confirmation Box","Are you sure you want to exit the program?")
		if response == 1:
			window3.withdraw()

	login_button = Button(login_frame,text="Log In",command=login,bg="#80FF00",font=("Forte",20)).grid(row=3,column=0,pady=10,padx=5)
	forget_button = Button(login_frame,text="Forget Password",command=forget,bg="#FFFF00",font=("Arial Black",10)).grid(row=3,column=1,padx=10)

	exit_button = Button(window3,text="Exit",command= exit,bg="#A9D0F5")
	exit_button.config(font=("Forte",15))
	exit_button.grid(row=2,column=1,padx=10,pady=5,ipadx=30,ipady=5)
	




def exit():
	response = messagebox.askyesno("Confirmation Box","Are you sure you want to exit the program?")
	if response == 1:
		window.quit()

welcome_label = Label(window,text="Welcome to the Health Record Management System",background="#A9D0F5",relief=SUNKEN)
welcome_label.config(font=("Arial Black",20))
welcome_label.grid(row=1,column=0,columnspan=3)

l=Label(window,text="\nEvery Patient click here",background="#A9D0F5")
l.config(font=("GOBOLD ITALIC",20))
l.grid(row=2,column=0)
l1=Label(window,text="\nFor Hospital Use",background="#A9D0F5")
l1.config(font=("GOBOLD ITALIC",20))
l1.grid(row=2,column=2)

btn_patient = Button(window,text="Click Me!",command=patient,bg="#FFFF00")
btn_patient.config(font=("Forte",20))
btn_patient.grid(row=3,column=0)

btn_doctor = Button (window,text="Click Me!",command = department,bg="#80FF00")
btn_doctor.config(font=("Forte",20))
btn_doctor.grid(row=3,column=2)

exit_button = Button(window,text="Exit",command=exit,bg="#A9D0F5")
exit_button.config(font=("Forte",15))
exit_button.grid(row=4,column=1,padx=10,pady=5,ipadx=30,ipady=5)



window.mainloop()