from tkinter import *
from PIL import Image, ImageTk

def mainPage():

	global font

	log = Tk()
	log.geometry("500x600")
	log.title("AGTP")
	log.configure(background="white")
	log.resizable(width=False, height=False)

	#Displaying the main logo on the sign in page
	logo = Image.open("media/logo.png")
	render = ImageTk.PhotoImage(logo)
	lbl_logo = Label(log, image=render, bg="white")
	lbl_logo.image = render
	lbl_logo.pack(fill=X)

	#Creating the frame for the entrys

	frame_entry1= Frame(log,width=500, height=300, bg="white")
	frame_entry1.place(x=60,y=230)



	#Font specifications
	font = ("Helvetica", 20,"bold")
	font_color = "#9acc56"

	#Username entry and password

	#Username label
	enter_username = Label(frame_entry1,text="Username:",bg="white",fg="black",font=font)
	enter_username.pack(anchor=W)

	#Username entry
	entry_username = Entry(frame_entry1,bg="white",width=20,font=("Helvetica", 15),fg="black")
	entry_username.pack()





	frame_entry2= Frame(log,width=500, height=100, bg="white")
	frame_entry2.place(x=60,y=330)


	#Password label
	enter_password = Label(frame_entry2,text="Password:",bg="white",fg="black",font=font)
	enter_password.pack(anchor=W)

	#Password entry
	entry_password = Entry(frame_entry2,bg="white",width=20,font=("Helvetica", 15),fg="black")
	entry_password.pack()

	frame_avail_name= Frame(log,width=500, height=500, bg="white")
	frame_avail_name.place(x=60,y=300)

	avail_response_name = Label(frame_avail_name,text="",bg="white",fg="black",font=("Helvetica", 15))
	avail_response_name.pack()

	frame_avail_pass= Frame(log,width=500, height=500, bg="white")
	frame_avail_pass.place(x=60,y=400)

	avail_response_pass = Label(frame_avail_pass,text="",bg="white",fg="black",font=("Helvetica", 15))
	avail_response_pass.pack()

	log.mainloop()

mainPage()