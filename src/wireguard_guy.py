import customtkinter
import os
from connection_returns import *
import tkinter as tk
import json
import platform
from net import *
from tkinter import filedialog
from tkinter import *
import public_ip as ip
from os import listdir
from os.path import isfile, join
	

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
# Soure Function to install all important libarys/programs
def install_sources():

	def btn_pw():
		command = f'echo "{tInput.get()}" | sudo -S apt install wireguard'
		os.system(command)
		command2 = f'pip install public-ip'
		os.system(command2)
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

def conf_to_dir():
	conf_file = filedialog.askopenfilename()

	def btn_pw():
			
		destination = '/etc/wireguard'
		command = f'echo "{tInput.get()}" | sudo -S cp {conf_file} {destination}'
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

# Function to change the name of the interface
def select_btn():
	json_c()

def linux_set():

	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('172x240')
	root.title('Settings') # Linux settings


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='Name of Interface:').place(x=13, y=10)


	# This is the section of code which creates a button
	customtkinter.CTkButton(root, text='Change', command=select_btn).place(x=16, y=38)


	customtkinter.CTkLabel(root, text='-----------------------------------').place(x=16, y=68)

	customtkinter.CTkLabel(root, text='Install Sources:').place(x=16, y=88)

	customtkinter.CTkButton(root, text='Install', command=install_sources).place(x=16, y=118)

	customtkinter.CTkLabel(root, text='-----------------------------------').place(x=16, y=148)

	customtkinter.CTkLabel(root, text='Add *.conf to list:').place(x=16, y=168)

	customtkinter.CTkButton(root, text='Select', command=conf_to_dir).place(x=16, y=198)


	root.mainloop()



# ---------------------------------------- other stuff ---------------------------------------
def show_stats():
	root.destroy()

	internet()


# ----------------------------------------- Other Configs --------------------------------------

def json_part(quest):
	dictionary = {"path": quest}

	# JSON File for Languages
	f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
	with open("/opt/zlelo/wireguard-guy/config.json", "w") as outfile: json.dump(dictionary, outfile)
	f.close()
	# End of JSON

def doneWindow4_json():
	# Show window
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('218x80')
	root.title('Changed')


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='Change the Interface successfully').place(x=13, y=10)

	root.mainloop()

def window_(files):

	def btnOkIn():
		get_item = box.get()
		quest = get_item[:-5]
		print(quest)
		json_part(quest)
		root.destroy()
		doneWindow4_json()
		
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('204x99')
	root.configure(background='#F0F8FF')
	root.title('Interface')


	box = customtkinter.CTkComboBox(root, values=files)
	box.place(x=32, y=19)

	# This is the section of code which creates a button
	customtkinter.CTkButton(root, text='Ok', command=btnOkIn).place(x=32, y=52)


	root.mainloop()


# -- Change Config file --
def json_c():
	
	path = '/etc/wireguard/'
	files = [f for f in listdir(path) if isfile(join(path, f))]
	window_(files)




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
			f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
			data = json.load(f) # Load all of the JSON file

			name_of_conf = data['path']

			f.close()

			# Start connecting
			command = f'echo "{tInput.get()}" | sudo -S wg-quick up {name_of_conf}'
			os.system(command)
			win.destroy()
			con_done()


		win = customtkinter.CTk()

		# This is the section of code which creates the main window
		win.geometry('175x88')
		win.title('Auth')


		# This is the section of code which creates a text input box
		tInput=customtkinter.CTkEntry(win)
		tInput.place(x=20, y=10)


		# This is the section of code which creates a button
		customtkinter.CTkButton(win, text='Ok', command=btn_pw).place(x=20, y=45)


		win.mainloop()

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
			f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
			data = json.load(f) # Load all of the JSON file

			name_of_conf = data['path']

			f.close()

			# Start connecting
			command = f'echo "{tInput.get()}" | sudo -S wg-quick down {name_of_conf}'
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
root.geometry('407x135')
root.title('Wireguard-Guy')


# This is the section of code which creates the a label
customtkinter.CTkLabel(root, text='Wireguard-Guy').place(x=163, y=20)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Connect', command=connect_btn).place(x=20, y=60)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Disconnect', command=disconnect_btn).place(x=245, y=60)

# This is the section of code which creates a image button
download_button = customtkinter.CTkButton(root, text='Settings', width=20, command=settings).place(x=173, y=60)

customtkinter.CTkLabel(root, text=f'Your ip is: {ip.get()}').place(x=20, y=100)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Settings", menu=filemenu)
filemenu.add_command(label="Change interface", command=select_btn)
filemenu.add_command(label="Install sources", command=install_sources)
filemenu.add_command(label="Add *.conf to list", command=conf_to_dir)

helpmenu = Menu(menu)
menu.add_cascade(label="Options", menu=helpmenu)
helpmenu.add_command(label="Traffic stats", command=show_stats)



root.mainloop()