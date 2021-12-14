import tkinter as tk
import winsound
from tkinter import *
class Error():
    def __init__(self):
        self.root = tk.Toplevel()
        duration = 1200  # milliseconds
        winsound.MessageBeep(duration)
        self.root.geometry('400x100')
        tk.Button(self.root, text='Ok', command=self.root.destroy, width=25, font='Calibri 12').place(x= 100, y=45)
        tk.Label(self.root, text='Error! Please fill all the text fields and try again', font= 'Calibri 14 bold').pack()

class not_loggged_in():
    def __init__(self):
        self.root = tk.Toplevel()
        duration = 1200  # milliseconds
        winsound.MessageBeep(duration)
        self.root.geometry('400x100')
        tk.Button(self.root, text='Ok', command=self.root.destroy, width=25, font='Calibri 12').place(x= 100, y=45)
        tk.Label(self.root, text="Can't log in. Check if card or PIN are correct and try again" , font= 'Calibri 14 bold').pack()


class already_registrated_error():

    def __init__(self):
        self.root = tk.Toplevel()
        duration = 1200  # milliseconds
        winsound.MessageBeep(duration)
        self.root.geometry('400x100')
        tk.Button(self.root, text='Ok', command=self.root.destroy, width=25, font='Calibri 12').place(x= 100, y=45)
        tk.Label(self.root, text="That card is already registrated. Please use another card, or log in" , font= 'Calibri 14 bold').pack()

class not_a_mail():
    def __init__(self):
        self.root = tk.Toplevel()
        duration = 1200  # milliseconds
        winsound.MessageBeep(duration)
        self.root.geometry('400x100')
        tk.Button(self.root, text='Ok', command=self.root.destroy, width=25, font='Calibri 12').place(x= 100, y=45)
        tk.Label(self.root, text="This email. Doesn't exist. Please type correct mail." , font= 'Calibri 14 bold').pack()