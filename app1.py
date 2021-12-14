from converter import *
from converter import DB
import tkinter as tk
from tkinter import *
from errorwindow import Error
from errorwindow import not_loggged_in
from tkinter import font

class login_form():

    def register_form(self):
        self.form.destroy()
        self.login_opened = False
        self.form.quit()

    def if_registrated(self):
        if not self.card.get() or not self.PIN.get():
            e = Error()
        res = self.db.check_elems(self.card.get(), self.PIN.get())
        if res:
            # TGREEN = '\033[32m'
            # TWHITE = '\033[37m'
            self.data = self.db.get_elems(self.card.get(), self.PIN.get())
            self.form.destroy()
            self.isreg = res
            self.form.quit()
            return res
        elif not res:
            notlogged = not_loggged_in()
            self.isreg = res
            return res
    def edit_form(self):
        self.label = tk.Label(self.form, text="Login", font='Calibri 24 bold')
        self.label.place(x=375, y = 30, anchor='nw')
        ####Card
        self.card_label= tk.Label(self.form, text='Card', font='Calibri 14')
        self.card_label.place(x= 40, y=100)
        self.card = tk.Entry(self.form, font = 'Calibri 16', width=25)
        self.card.place(x = 90, y= 100)
        ### PIN
        self.PIN_label = tk.Label(self.form, text='PIN', font='Calibri 14')
        self.PIN_label.place(x=420, y=100)
        self.PIN = tk.Entry(self.form, font = 'Calibri 16', width=25)
        self.PIN.place(x=460, y=100)
        ## FoundButton
        self.btn = tk.Button(self.form, text='Log in', font='Calibri 16', width= 20, bd=0, activebackground='red', command=self.if_registrated)
        self.btn.place(x=295, y= 250)
        f = font.Font(self.form, family='Calibri', size='11',)
        f.configure(underline=True)
        self.register_label = tk.Label(self.form, text="Haven't registrated yet? Register", font=f, fg='#4240a1')
        self.register_label.place(x=295, y = 305)
        self.register_label.bind('<Button>', lambda e:self.register_form())

    def __init__(self):
        self.form = tk.Tk()
        self.form.geometry('800x400')
        self.form.title('Login')
        self.edit_form()
        self.db = DB()
        self.open = True
        self.isreg = False
        self.login_opened = True
        self.form.iconbitmap('static/icon.ico')
        self.form.mainloop()
