from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
class finish():
    def __init__(self):
        self.root = tk.Tk()
        # image1 = Image.open("static/finish.png")
        img = ImageTk.PhotoImage(file ="static/finish.png")
        self.label = tk.Label(self.root, image=img)
        self.label.place( x=0, y=0, relwidth=1, relheight=1)
        self.label.configure(background='white')
        self.root.iconbitmap('static/icon.ico')
        self.root.mainloop()
