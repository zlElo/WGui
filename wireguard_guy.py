import customtkinter
import os
from connection_returns import *
import tkinter as tk
import json
from tkinter import filedialog
import platform



# -------------------- Start -------------------------------------

# A normal done window which can be used for all
def normal_done_window():
	root2 = customtkinter.CTk()
	root2.geometry('165x80')
	root2.title('Done')


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root2, text='The operation is done!').place(x=13, y=10)

	root2.mainloop()

def error_window_windows():
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('213x80')
	root.title('Error')


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='Does not support any Windows!').place(x=13, y=10)

	root.mainloop()




# -------------------- LINUX SETTINGS ------------------------------
def linux_set():
	# Function to change the *.conf file
	def select_btn():
		root.destroy()
		json_c()
	
	# Soure Function to install all important libarys/programs
	def install_sources():

		def btn_pw():
			command = f'echo "{tInput.get()}" | sudo -S apt install wireguard'
			os.system(command)
			root.destroy()
			normal_done_window()


		root = customtkinter.CTk()

		# This is the section of code which creates the main window
		root.geometry('175x88')
		root.title('Auth')


		# This is the section of code which creates a text input box
		tInput=customtkinter.CTkEntry(root)
		tInput.place(x=20, y=10)


		# This is the section of code which creates a button
		customtkinter.CTkButton(root, text='Ok', command=btn_pw).place(x=20, y=45)


		root.mainloop()

	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('172x180')
	root.title('Settings') # Linux settings


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='*.conf File:').place(x=13, y=10)


	# This is the section of code which creates a button
	customtkinter.CTkButton(root, text='Select', command=select_btn).place(x=16, y=38)


	customtkinter.CTkLabel(root, text='-------------------------------').place(x=16, y=68)

	customtkinter.CTkLabel(root, text='Install Sources:').place(x=16, y=88)

	customtkinter.CTkButton(root, text='Install', command=install_sources).place(x=16, y=118)


	root.mainloop()





# ----------------------------------------- Other Configs --------------------------------------

# -- Change Config file --
def json_c():
	dictionary = {
    "path": filedialog.askopenfilename()
	}

	# JSON File for Languages
	f = open('code/config.json') #Open the JSON file
	with open("code/config.json", "w") as outfile: json.dump(dictionary, outfile)
	f.close()
	# End of JSON

	# Show window
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('213x80')
	root.title('Changed')


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='*.conf file changed successfully').place(x=13, y=10)

	root.mainloop()




# ------------------------------- Menu -------------------------------

# -- Settings Menu --
def settings():
	os = platform.system()
	
	if os == 'Linux':
		linux_set()

	elif os == 'Windows':
		error_window_windows()
	




# --------------------------------------------------CONNECT/DISCONNECT------------------------------------------------------

# -- Connect Button --
def connect_btn():
	system = platform.system()
	
	# If Program detect Linux as OS
	if system == 'Linux':
		def btn_pw():
			# json load conf
			f = open('code/config.json') #Open the JSON file
			data = json.load(f) # Load all of the JSON file

			path_to_the_conf = data['path']

			f.close()

			# Start connecting
			command = f'echo "{tInput.get()}" | sudo -S wg-quick up {path_to_the_conf}'
			os.system(command)
			root.destroy()
			con_done()


		root = customtkinter.CTk()

		# This is the section of code which creates the main window
		root.geometry('175x88')
		root.title('Auth')


		# This is the section of code which creates a text input box
		tInput=customtkinter.CTkEntry(root)
		tInput.place(x=20, y=10)


		# This is the section of code which creates a button
		customtkinter.CTkButton(root, text='Ok', command=btn_pw).place(x=20, y=45)


		root.mainloop()

	# If Program detect Windows as OS
	elif system == 'Windows':
		error_window_windows()

	
	

# -- Disconnect Button --
def disconnect_btn():
	system = platform.system()

	# If Program detect Linux as OS
	if system == 'Linux':
		def btn_pw():
			# json load conf
			f = open('code/config.json') #Open the JSON file
			data = json.load(f) # Load all of the JSON file

			path_to_the_conf = data['path']

			f.close()

			# Start connecting
			command = f'echo "{tInput.get()}" | sudo -S wg-quick down {path_to_the_conf}'
			os.system(command)
			root.destroy()
			dis_done()


		root = customtkinter.CTk()

		# This is the section of code which creates the main window
		root.geometry('175x88')
		root.title('Auth')


		# This is the section of code which creates a text input box
		tInput=customtkinter.CTkEntry(root)
		tInput.place(x=20, y=10)


		# This is the section of code which creates a button
		customtkinter.CTkButton(root, text='Ok', command=btn_pw).place(x=20, y=45)


		root.mainloop()

	# If Program detect Windows as OS
	elif system == 'Windows':
		error_window_windows()
		




# ----------------------------------------------------MAIN---------------------------------------------------

# -- Main Window --

root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('439x120')
root.title('Wireguard-Guy')


# This is the section of code which creates the a label
customtkinter.CTkLabel(root, text='Wireguard-Guy').place(x=149, y=20)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Connect', command=connect_btn).place(x=20, y=60)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Disconnect', command=disconnect_btn).place(x=280, y=60)

# This is the section of code which creates a image button


download_icon = tk.PhotoImage(file='code/settings.png')
download_button = customtkinter.CTkButton(root, text='Settings', image=download_icon, width=20, command=settings).place(x=174, y=60)


root.mainloop()
