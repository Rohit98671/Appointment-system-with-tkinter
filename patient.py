from tkinter import *
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox

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
			window1.quit()

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


window1.mainloop()