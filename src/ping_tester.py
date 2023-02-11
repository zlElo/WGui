import os
import customtkinter
from tkinter import *
from tkinter.ttk import *

# The script to test the ping statistics in different countrys on the world
def pinger():
    def ping_test_locations():
        count = 0
        print(
    """
Ping test starts now!

//Informations
Test locations: USA, USA-2, Germany, Finland, Sweden
Pings per location: 3
Total pings: 15

-------------------------

    """
        )

        # testing USA
        print('testing USA')

        hostname = "ash-speed.hetzner.com"
        response = os.system("ping -c 3 " + hostname)

        #and then check the response...
        if response == 0:
            print(f'[✓] USA')
            usa = 'Successfully'
            count = count + 1 
        else:
            print(f'[✕] USA')
            usa = 'Unsuccessfully'
        progress['value'] = 20
        customtkinter.CTkLabel(root, text=f'USA: {usa}').place(x=20, y=80)
        root.update_idletasks()
    
        # testing Germany
        print('')
        print('testing Germany')

        hostname = "speed.hetzner.de"
        response = os.system("ping -c 3 " + hostname)

        #and then check the response...
        if response == 0:
            print(f'[✓] Germany')
            germany = 'Successfully'
            count = count + 1 
        else:
            print(f'[✕] Germany')
            germany = 'Unsuccessfully'
        progress['value'] = 40
        customtkinter.CTkLabel(root, text=f'Germany: {germany}').place(x=20, y=100)
        root.update_idletasks()
    

        # testing Finland
        print('')
        print('testing Finland')

        hostname = "hel.icmp.hetzner.com"
        response = os.system("ping -c 3 " + hostname)

        #and then check the response...
        if response == 0:
            print(f'[✓] Finland')
            finland = 'Successfully'
            count = count + 1 
        else:
            print(f'[✕] Findland')
            finland = 'Unsuccessfully'
        progress['value'] = 60
        customtkinter.CTkLabel(root, text=f'Finland: {finland}').place(x=20, y=120)
        root.update_idletasks()

    
        # testing USA2
        print('')
        print('testing USA-2')

        hostname = "hil-speed.hetzner.com"
        response = os.system("ping -c 3 " + hostname)

        #and then check the response...
        if response == 0:
            print(f'[✓] USA-2')
            usa_2 = 'Successfully'
            count = count + 1 
        else:
            print(f'[✕] USA-2')
            usa_2 = 'Unsuccessfully'
        progress['value'] = 80
        customtkinter.CTkLabel(root, text=f'USA-2: {usa_2}').place(x=20, y=140)
        root.update_idletasks()


        # testing Sweden
        print('')
        print('testing Sweden')

        hostname = "www.junet.se"
        response = os.system("ping -c 3 " + hostname)

        #and then check the response...
        if response == 0:
            print(f'[✓] Sweden')
            sweden = 'Successfully'
            count = count + 1 
        else:
            print(f'[✕] Sweden')
            sweden = 'Unsuccessfully'
        progress['value'] = 100
        customtkinter.CTkLabel(root, text=f'Sweden: {sweden}').place(x=20, y=160)
        root.update_idletasks()

        if count == 5:
            customtkinter.CTkLabel(root, text=f'Test done!', text_color=('green')).place(x=20, y=185)
        if count == 4:
            customtkinter.CTkLabel(root, text=f'Test done!', text_color=('orange')).place(x=20, y=185)
        if count < 4:
            customtkinter.CTkLabel(root, text=f'Test done!', text_color=('red')).place(x=20, y=185)


    root = customtkinter.CTk()


    # This is the section of code which creates the main window
    root.geometry('332x215')
    root.title('Connection pingtest')



    # This is the section of code which creates a button
    customtkinter.CTkButton(root, text='Start test', command=ping_test_locations, width=175).place(x=20, y=40)


    progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    progress.place(x=212, y=44)


    root.mainloop()