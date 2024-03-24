import psutil
import socket
import customtkinter

def internet():
    UPDATE_DELAY = 1  # in seconds

    def get_size(bytes):
        """Return size of bytes in a nice format"""
        units = ['B', 'K', 'M', 'G', 'T', 'P']
        for i, unit in enumerate(units):
            if bytes < 1024 or i == len(units) - 1:
                return f"{bytes:.2f}{unit}"
            bytes /= 1024

    # Get network I/O stats from psutil
    io = psutil.net_io_counters()
    # Extract total bytes sent and received
    sent, recv = io.bytes_sent, io.bytes_recv

    root = customtkinter.CTk()

    # This is the section of code which creates the main window
    root.geometry('307x90')
    root.title('Internet')

    label = customtkinter.CTkLabel(root, text='Checking...')
    label.pack()

    def is_connected():
        try:
            socket.create_connection(("google.com", 80))
            state = "Connected"
        except OSError:
            state = "Disconnected"
        label.configure(text=f'Internet status: {state}')
        root.after(1000 * UPDATE_DELAY, is_connected)

    is_connected()  # start the checking

    down_label = customtkinter.CTkLabel(root, text=f'Total download: {get_size(recv)}', anchor="center")
    down_label.pack()

    up_label = customtkinter.CTkLabel(root, text=f'Total upload: {get_size(sent)}', anchor="center")
    up_label.pack()

    root.mainloop()
