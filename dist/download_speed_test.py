from tkinter import *
from tkinter.ttk import *
import customtkinter
import os
import requests
import time

def download_speed_test_function():
    #Create an instance of tkinter frame
    win= Tk()
    #Set the geometry of frame
    win.title('Downloadspeed-test')
    win.geometry("340x240")


    def download(url, filename):
        start = time.perf_counter()
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')

            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50*downloaded/total)
                    bar.set(done/50) 
                
                    win.update_idletasks()
                    win.update()
        win.update_idletasks()
    
        os.remove('100MB.bin')
        time_ = time.perf_counter() - start
        downspeed_ = 100 / time_

        customtkinter.CTkLabel(win, text='Test is done!').pack(pady=5)

        customtkinter.CTkLabel(win, text=f'Downloaded data: 100 MB').pack()
        customtkinter.CTkLabel(win, text=f'Deleted testfile: True').pack()
        customtkinter.CTkLabel(win, text=f'Time elapsed: {(time.perf_counter() - start):.2f} seconds').pack()
        customtkinter.CTkLabel(win, text=f'Calculated download-speed: {round(downspeed_ , 2)}').pack()

    




    bar= customtkinter.CTkProgressBar(win, orientation=HORIZONTAL, width=300)
    bar.pack(pady=15)

    #Create a button
    customtkinter.CTkButton(master = win, text="Start Downloadtest", command=lambda: [download('https://speed.hetzner.de/100MB.bin', '100MB.bin')]).pack(pady=15)



    win.mainloop()
