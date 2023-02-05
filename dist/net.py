import psutil
import socket
import customtkinter

def internet():
    UPDATE_DELAY = 1 # in seconds

    def get_size(bytes):
        """
        Returns size of bytes in a nice format
        """
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bytes < 1024:
                return f"{bytes:.2f}{unit}B"
            bytes /= 1024

    # get the network I/O stats from psutil
    io = psutil.net_io_counters()
    # extract the total bytes sent and received
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv
    io_2 = psutil.net_io_counters()
        

    root = customtkinter.CTk()

    # This is the section of code which creates the main window
    root.geometry('307x90')
    root.title('Internet')

    connection = customtkinter.CTkLabel(root,text='Checking ...')
    connection.pack()

    def is_connected():
        try:
            socket.create_connection(("zlelo.github.io", 80))
            state = "Online"
        except OSError:
            state = "Offline"
        connection.configure(text = f'Internet status: {state}')
        root.after(100000, is_connected) # do checking again 10 seconds later

    is_connected() # start the checking
    

    download = customtkinter.CTkLabel(root, text=f'Total Download: {get_size(io_2.bytes_recv)}', anchor="center").pack()
    

    upload = customtkinter.CTkLabel(root, text=f'Total Upload: {get_size(io_2.bytes_sent)}', anchor="center").pack()
    

    root.mainloop()