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

	filedialog.askopenfilename()



def doctor():
	return




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
l1=Label(window,text="\nThis is for doctors",background="#A9D0F5")
l1.config(font=("GOBOLD ITALIC",20))
l1.grid(row=2,column=2)

btn_patient = Button(window,text="Click Me!",command=patient,bg="#FFFF00")
btn_patient.config(font=("Forte",20))
btn_patient.grid(row=3,column=0)

btn_doctor = Button (window,text="Click Me!",command = doctor,bg="#80FF00")
btn_doctor.config(font=("Forte",20))
btn_doctor.grid(row=3,column=2)

exit_button = Button(window,text="Exit",command=exit,bg="#A9D0F5")
exit_button.config(font=("Forte",15))
exit_button.grid(row=4,column=1,padx=10,pady=5,ipadx=30,ipady=5)



window.mainloop()