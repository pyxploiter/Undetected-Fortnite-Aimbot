import tkinter as tk
from PIL import ImageTk, Image
from model import *

def startAimbot(type, window):
	start_label = tk.Label(window, padx=10, text=type+" mode is running...", font=("Halvetica", 18), bg="red", fg="white")
	start_label.place(x = 250, y = 550)
	play(type)

def init_window(window):
	bg = ImageTk.PhotoImage(Image.open("img/bg.jpg"))
	bg_img_label = tk.Label(window, image = bg)
	bg_img_label.pack(side = "top")

	title_label = tk.Label(window, padx=10, text="Undetectable Fortnite Aimbot", font=("Halvetica", 30), fg="red")
	title_label.place(x = 65, y = 30)

	pic_label = tk.Label(window, padx=10, text="Click on the mode to start it", font=("Halvetica", 18), bg="green", fg="black")
	pic_label.place(x = 200, y = 140)

	novice_button = tk.Button(window, relief="flat", command=lambda: startAimbot('Novice', window))
	novice_img = ImageTk.PhotoImage(file="img/novice.png")
	novice_button.config(image=novice_img)
	novice_button.place(x = 290, y = 200)

	smart_button = tk.Button(window, relief="flat", command=lambda: startAimbot('Smart', window))
	smart_img = ImageTk.PhotoImage(file="img/smart.png")
	smart_button.config(image=smart_img)
	smart_button.place(x = 290, y = 310)

	master_button = tk.Button(window, relief="flat", command=lambda: startAimbot('Master', window))
	master_img = ImageTk.PhotoImage(file="img/master.png")
	master_button.config(image=master_img)
	master_button.place(x = 275, y = 410)

	#Start the GUI
	window.mainloop()

#This creates the main window of an application
window = tk.Tk()
window.title("Fortnite Aimbot")
window.geometry("800x620")

# this removes the maximize button
window.resizable(0,0)
#initiate the first window
init_window(window)
