import customtkinter

def con_done():
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('360x117')
	root.title('Connection done')

	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='The connection to your target server is done!').place(x=49, y=49)

	root.mainloop()

def dis_done():
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('445x117')
	root.title('Successfully disconnected')

	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='You have been successfully disconnected from the server!').place(x=49, y=49)

	root.mainloop()