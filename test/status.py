from tkinter import *

root = Tk()
root.title('test')
root.geometry('150x150')

# Statusleuchte erstellen
led = Canvas(root, width=15, height=15)
led.pack()
condition = True
# Funktion, die die Statusleuchte ändert
def change_light():
    if condition == True:
        led.create_oval(0, 0, 15, 15, fill="green")
    else:
        led.create_oval(0, 0, 15, 15, fill="red")

# Aufruf der Funktion beim Start
change_light()

root.mainloop()