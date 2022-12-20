from tkinter import filedialog
import os

file = filedialog.askopenfilename()
print(file)
file = file.split('/')[len(file.split('/'))-1]
print(file)