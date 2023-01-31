import customtkinter

def window_(files):

	def btnOkIn():
		quest = box.get()
		print(quest)
		
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('204x99')
	root.configure(background='#F0F8FF')
	root.title('Interface')


	box = customtkinter.CTkComboBox(root, values=files).place(x=32, y=19)

	# This is the section of code which creates a button
	customtkinter.CTkButton(root, text='Ok', command=btnOkIn).place(x=32, y=52)


	root.mainloop()

files = ['1', '2']
window_(files)