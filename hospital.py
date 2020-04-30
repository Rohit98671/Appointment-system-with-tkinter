from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

window3 = Tk()
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

	global usrnm
	global psswd

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

		def ext():
			window4.withdraw()

		exit_button = Button(window4,text="Exit",command= ext,bg="#A9D0F5")
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
		window3.quit()

login_button = Button(login_frame,text="Log In",command=login,bg="#80FF00",font=("Forte",20)).grid(row=3,column=0,pady=10,padx=5)
forget_button = Button(login_frame,text="Forget Password",command=forget,bg="#FFFF00",font=("Arial Black",10)).grid(row=3,column=1,padx=10)

exit_button = Button(window3,text="Exit",command= exit,bg="#A9D0F5")
exit_button.config(font=("Forte",15))
exit_button.grid(row=2,column=1,padx=10,pady=5,ipadx=30,ipady=5)



window3.mainloop()