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


# The error message when you run the program under windows
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

	
	command = f'sudo apt install wireguard'
	os.system(command) # run the command to install wireguard
	command2 = f'pip install public-ip' # command to install the libary to show the public ip of the user
	os.system(command2)
	root.destroy()
	normal_done_window()

# function to copy the config file to the wireguard directory
def conf_to_dir():
	conf_file = filedialog.askopenfilename()

	
			
	destination = '/etc/wireguard' # set the standart directory
	command = f'sudo cp {conf_file} {destination}' # standart linux command to copy files
	os.system(command) # run the command with the os libary
	root.destroy()
	normal_done_window() # show the standart done window


# function to call the json_c function
def select_btn():
	json_c()


# ---------------------------------------- other stuff ---------------------------------------

# function to call the internet statistics function from the net.py script

def show_stats():
	internet()

# ----------------------------------------- Other Configs --------------------------------------

# function to write the path for the config file in the config.json file
def json_part(quest):
	dictionary = {"path": quest} # get the var quest from window_ (exactly from the combobox)

	# JSON File for Languages
	f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
	with open("/opt/zlelo/wireguard-guy/config.json", "w") as outfile: json.dump(dictionary, outfile) # write in the JSON
	f.close()
	# End of JSON


# The done window for the json operation
def doneWindow4_json():
	# Show window
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('218x80')
	root.title('Changed')


	# This is the section of code which creates the a label
	customtkinter.CTkLabel(root, text='Change the Interface successfully').place(x=13, y=10)

	root.mainloop()


# The window to choose the tunnel
def window_(files):

	# create function for the button
	def btnOkIn():
		get_item = box.get() # get the item from the combobox
		quest = get_item[:-5] # remove the last 5 characters from the get_item variable (it remove the .conf)
		print(quest)
		json_part(quest) # call the json function and give the function the variable quest
		root.destroy() # destroy the window
		doneWindow4_json() # show the done window
	
	# Create the window with the selection combobox
	root = customtkinter.CTk()

	# This is the section of code which creates the main window
	root.geometry('204x99')
	root.configure(background='#F0F8FF')
	root.title('Interface')


	box = customtkinter.CTkComboBox(root, values=files)
	box.place(x=32, y=19) # place the combobox, box = customtkinter.CTkComboBox(root, values=files).place(x=32, y=19) is not possible!

	# This is the section of code which creates a button
	customtkinter.CTkButton(root, text='Ok', command=btnOkIn).place(x=32, y=52)


	root.mainloop()


# -- Change Config file --
def json_c():
	
	path = '/etc/wireguard/' # set the standart wireguard path
	files = [f for f in listdir(path) if isfile(join(path, f))] # read all files from the dir
	window_(files)



# --------------------------------------------------CONNECT/DISCONNECT------------------------------------------------------

# -- Connect Button --
def connect_btn():
	
	system = platform.system()
	
	# If Program detect Linux as OS
	if system == 'Linux':
		
		# --- connection ---
		# json load conf
		f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
		data = json.load(f) # Load all of the JSON file

		name_of_conf = data['path']

		f.close()

		# Start connecting
		command = f'sudo wg-quick up {name_of_conf}'
		os.system(command)
			

		# --- LED ---
		dictionary = {"light": True} # Set True to activate the green LED

		# JSON File for the status light
		f = open('/opt/zlelo/wireguard-guy/light_config.json') #Open the JSON file
		with open("/opt/zlelo/wireguard-guy/light_config.json", "w") as outfile: json.dump(dictionary, outfile) # write in the JSON
		f.close()


		f = open('/opt/zlelo/wireguard-guy/light_config.json') #Open the JSON file
		data = json.load(f) # Load all of the JSON file

		condition = data['light']

		f.close()

		change_light(condition)


		# Show connect done Window
		con_done()


	# If Program detect Windows as OS
	elif system == 'Windows':
		error_window_windows()

	
	

# -- Disconnect Button --
def disconnect_btn():
	
	system = platform.system()

	# If Program detect Linux as OS
	if system == 'Linux':
		
		# json load conf
		f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
		data = json.load(f) # Load all of the JSON file

		name_of_conf = data['path']

		f.close()

		# Start connecting
		command = f'sudo wg-quick down {name_of_conf}'
		os.system(command)


		# --- LED ---
		dictionary = {"light": False} # set False

		# JSON file for the light controle
		f = open('/opt/zlelo/wireguard-guy/light_config.json') #Open the JSON file
		with open("/opt/zlelo/wireguard-guy/light_config.json", "w") as outfile: json.dump(dictionary, outfile) # write in the JSON
		f.close()


		f = open('/opt/zlelo/wireguard-guy/light_config.json') #Open the JSON file
		data = json.load(f) # Load all of the JSON file

		condition = data['light'] # set the condition

		f.close()

		change_light(condition)


		# Show disconnect window
		dis_done()


	# If Program detect Windows as OS
	elif system == 'Windows':
		error_window_windows()
		

	
# Function to change the light color
def change_light(condition):

    if condition == True:
        led.create_oval(0, 0, 15, 15, fill="green")
    else:
        led.create_oval(0, 0, 15, 15, fill="red")


# Function for status led to check the connection and set the right color
def status_now_for_led():

	f = open('/opt/zlelo/wireguard-guy/light_config.json') #Open the JSON file
	data = json.load(f) # Load all of the JSON file

	condition = data['light']

	f.close()

	change_light(condition)


    

	

# ----------------------------------------------------MAIN---------------------------------------------------

# -- Main Window --

root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('407x115')
root.title('Wireguard-Guy')

def check_selected_server():

	f = open('/opt/zlelo/wireguard-guy/config.json') #Open the JSON file
	data = json.load(f) # Load all of the JSON file

	data_set = data['path']
	f.close()

	label_ = customtkinter.CTkLabel(root, text=f'Server: {data_set}', anchor="center")
	label_.pack()
	

# Aufrufen der Funktion, um den Textwert zuzuweisen
check_selected_server()


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Connect', command=connect_btn, width=175).place(x=20, y=40)


# This is the section of code which creates a button
customtkinter.CTkButton(root, text='Disconnect', command=disconnect_btn, width=175).place(x=212, y=40)


customtkinter.CTkLabel(root, text=f'Your ip is: {ip.get()}').place(x=20, y=80)

customtkinter.CTkLabel(root, text='Your VPN connection is:').place(x=230, y=80)

dictionary = {"light": True} # get the var quest from window_ (exactly from the combobox)

	
led = Canvas(root, width=15, height=15, bg='#ebebeb')
led.place(x=370, y=85)
status_now_for_led()

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