from tkinter import *
from PIL import Image, ImageTk

def mainPage():

	bgcolor = "#FAF9F5"

	global font

	root = Tk()
	root.geometry("500x600")
	root.title("AGTP")
	root.configure(background="#FAF9F5")
	root.resizable(width=False, height=False)

	#Displaying the main logo on the sign in page
	logo = Image.open("media/logo.png")
	render = ImageTk.PhotoImage(logo)
	lbl_logo = Label(root, image=render, bg="#FAF9F5")
	lbl_logo.image = render
	lbl_logo.pack(fill=X)

	#Creating the frame for the entrys

	frame_entry1= Frame(root,width=500, height=300, bg=bgcolor)
	frame_entry1.place(x=20,y=230)



	#Font specifications
	font = ("Helvetica", 18,"bold")
	font_color = "#9acc56"

	#Username entry and password

	#Username label
	enter_username = Label(frame_entry1,text="How many sides does the shape have:",fg="black",font=font,bg=bgcolor)
	enter_username.pack(side=LEFT)

	frame_entry2= Frame(root,width=500, height=300, bg=bgcolor)
	frame_entry2.place(x=40,y=430)

	numF = StringVar(frame_entry1)
	numF.set(3) # default value

	def createOptions(numF):
		optionFunc = int(numF.get())
		if 


	numFunctions = OptionMenu(frame_entry1, numF, 3, 4, 5)
	numFunctions.pack(side=LEFT)


	numButton = Button(frame_entry1, text ="Input", command = lambda: createOptions(numF))
	numButton.pack(side=LEFT)


	root.mainloop()

mainPage()