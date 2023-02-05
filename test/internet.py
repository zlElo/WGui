import socket
import tkinter

top = tkinter.Tk()
top.title("Network Checker")
top.configure(background="#006666")

l=tkinter.Label(top,text='Checking ...')
l.pack()

def is_connected():
    try:
        socket.create_connection(("zlelo.github.io", 80)) # better to set timeout as well
        state = "Online"
    except OSError:
        state = "Offline"
    l.config(text=state)
    top.after(1000, is_connected) # do checking again one second later

is_connected() # start the checking
top.mainloop()