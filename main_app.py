from tkinter import *
import tkinter as tk
from app import *
from converter import DB
from errorwindow import Error
from finish_window import *


class main_app():

    def call_finish(self):
        self.root.destroy()
        self.finish = finish()
        self.finish.root.quit()
        self.root.quit()
    def entry_get(self, entry):
        return entry.get()
    def setEdit(self, param,  old_value):
        ## TODO Edit args
        # print(self.edit_entry_var.get())
        if len(self.edit_entry_var.get()) == 0:
            return Error()
        self.db.update_name(param, old_value,  self.data[0], self.edit_entry_var.get())
        if param == 'PIN':
            self.data = self.db.get_elems(self.data[5], self.edit_entry_var.get())
        if param == 'Credit':
            self.data = self.db.get_elems(self.edit_entry_var.get(), self.data[6])
        self.data = self.db.get_elems(self.data[5], self.data[6])
        self.edit_button.grid_forget()
        self.edit_entry.grid_forget()
        print(self.data)
        if param == "Name":
            self.name.destroy()
            self.name_variable = self.data[1]
            self.name = tk.Label(self.frame, text=self.data[1],textvariable=self.name_variable, font='Times 14')
            self.name.grid(row=0, column=1, padx=0, pady=3)
            print(self.name_variable)
        elif param == "Country":
            self.country.destroy()
            self.country_variable = self.data[2]
            self.country = tk.Label(self.frame, text=self.data[2], textvariable=self.country_variable, font='Times 14')
            self.country.grid(row=1, column=1, padx=0, pady=3)
        elif param == "City":
            self.city.destroy()
            self.city_variable = self.data[3]
            self.city = tk.Label(self.frame, font='Times 14', text=self.data[3], textvariable=self.city_variable)
            self.city.grid(row=2, column=1, padx=0, pady=3)
        elif param == "Place":
            self.place.destroy()
            self.place_variable = self.data[4]
            self.place = tk.Label(self.frame, text=self.data[4], textvariable=self.place_variable, font='Times 14')
            self.place.grid(row=3, column=1, padx=0, pady=3)
        elif param == "Credit":
            self.card.destroy()
            self.card_variable = self.data[5]
            self.card = tk.Label(self.frame, text=self.data[5], textvariable=self.card_variable, font='Times 14')
            self.card.grid(row=0, column=5, padx=0, pady=3)
        elif param == "PIN":
            self.PIN.destroy()
            self.PIN_variable = self.data[6]
            self.PIN = tk.Label(self.frame, text=self.data[6], textvariable=self.PIN_variable, font='Times 14')
            self.PIN.grid(row=1, column=5, padx=0, pady=3)
        elif param == "CVV2":
            self.CVV.destroy()
            self.cvv_variable = self.data[7]
            self.CVV = tk.Label(self.frame, text=self.data[7], textvariable=self.cvv_variable, font='Times 14')
            self.CVV.grid(row=2, column=5, padx=0, pady=3)
        elif param == "Email":
            self.email.destroy()
            self.email_variable = self.data[8]
            self.email = tk.Label(self.frame, text=self.data[8], textvariable=self.email_variable, font='Times 14')
            self.email.grid(row=3, column=5, padx=0, pady=3)



    def edit_label(self, param, row, column, old_value):

        self.edit_button = tk.Button(self.frame, text='set', bd=0, background="#039c06", command=lambda:self.setEdit(param, old_value))
        self.edit_button.grid(row=row, column=column+1, padx=3, pady=3)
        self.edit_entry_var = tk.StringVar()
        self.edit_entry = tk.Entry(self.frame, font='Calibri 14', textvariable=self.edit_entry_var)
        self.edit_entry.grid(row=row, column=column, padx=3, pady=3)

    def edit_form(self):

        self.frame = tk.Frame(self.root)
        # self.frame.resizable = True

        ## name
        self.label_name = tk.Label(self.frame, text='Your name:', font='Times 14').grid(row=0, column=0, padx=0, pady=10)
        self.name_variable = tk.StringVar()
        self.name_variable = self.data[1]
        self.name = tk.Label(self.frame, text=self.data[1],textvariable=self.name_variable, font='Times 14')
        self.name.grid(row=0, column=1, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text ='edit', bd=0, activebackground='#8fc5cf',
                                       font = 'Calibri 12', command=lambda :self.edit_label('Name',0,1,self.data[1])).grid(row=0, column = 2,padx=3, pady=3)
        self.spacing = tk.Label(self.frame, text='      ', font='Times 14').grid(row=0, column=3, padx=0,
                                                                                 pady=10)
        ### country
        self.label_country = tk.Label(self.frame, text='Your country:', font='Times 14').grid(row=1, column=0, padx=0, pady=10)
        self.country_variable = tk.StringVar()
        self.country_variable = self.data[2]
        self.country = tk.Label(self.frame, text=self.data[2], textvariable=self.country_variable, font='Times 14')
        self.country.grid(row=1, column=1, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('Country',1,1, self.data[2])).grid(row=1, column=2, padx=3, pady=3)
        self.spacing = tk.Label(self.frame, text='      ', font='Times 14').grid(row=1, column=3, padx=0,
                                                                                 pady=10)

        #### City
        self.label_city = tk.Label(self.frame, text='Your city:', font='Times 14').grid(row=2, column=0, padx=0, pady=10)
        self.city_variable = tk.StringVar()
        self.city_variable = self.data[3]
        self.city = tk.Label(self.frame, font='Times 14',text=self.data[3], textvariable=self.city_variable)
        self.city.grid(row=2, column=1, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda:self.edit_label('City',2,1, self.data[3]))
        self.change_button.grid(row=2, column=2, padx=3, pady=3)
        self.spacing = tk.Label(self.frame, text='      ', font='Times 14').grid(row=2, column=3, padx=0,
                                                                                 pady=10)
        #### Place
        self.label_place = tk.Label(self.frame, text='Your place:', font='Times 14').grid(row=3, column=0, padx=0, pady=10)
        self.place_variable = tk.StringVar()
        self.place_variable = self.data[4]
        self.place = tk.Label(self.frame, text= self.data[4], textvariable=self.place_variable, font='Times 14')
        self.place.grid(row=3, column=1, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('Place',3,1, self.data[4])).grid(row=3, column=2, padx=3, pady=3)
        self.spacing = tk.Label(self.frame, text='      ', font='Times 14').grid(row=3, column=3, padx=0,
                                                                                 pady=10)
        ### Card
        self.label_card = tk.Label(self.frame, text='Your card:', font='Times 14').grid(row=0, column=4, padx=0, pady=10)
        self.card_variable = tk.StringVar()
        self.card_variable = self.data[5]
        self.card = tk.Label(self.frame, text = self.data[5], textvariable=self.card_variable, font='Times 14')
        self.card.grid(row=0, column=5, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('Credit',0,5, self.data[5])).grid(row=0, column=6, padx=3, pady=3)
        ### PIN
        self.label_PIN = tk.Label(self.frame, text='Your PIN:', font='Times 14').grid(row=1, column=4, padx=0, pady=10)
        self.PIN_variable = tk.StringVar()
        self.PIN_variable = self.data[6]
        self.PIN = tk.Label(self.frame, text= self.data[6], textvariable=self.PIN_variable, font='Times 14')
        self.PIN.grid(row=1, column=5, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('PIN',1,5, self.data[6])).grid(row=1, column=6, padx=3, pady=3)
        ### CVV
        self.label_cvv = tk.Label(self.frame, text='Your cvv:', font='Times 14').grid(row=2, column=4, padx=0, pady=10)
        self.cvv_variable = tk.StringVar()
        self.cvv_variable = self.data[7]
        self.CVV = tk.Label(self.frame, text = self.data[7], textvariable=self.cvv_variable, font='Times 14')
        self.CVV.grid(row=2, column=5, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('CVV2',2,5, self.data[7])).grid(row=2, column=6, padx=3, pady=3)
        ## email
        self.label_email = tk.Label(self.frame, text='Your email:', font='Times 14').grid(row=3, column=4, padx=0, pady=10)
        self.email_variable = tk.StringVar()
        self.email_variable = self.data[8]
        self.email = tk.Label(self.frame, text = self.data[8],textvariable=self.email_variable, font='Times 14')
        self.email.grid(row=3, column=5, padx=0, pady=3)
        self.change_button = tk.Button(self.frame, text='edit', bd=0, activebackground='#8fc5cf',
                                       font='Calibri 12', command=lambda :self.edit_label('Email',3,5, self.data[8])).grid(row=3, column=6, padx=3, pady=3)
        ## Finish button
        self.finish_button = tk.Button(self.frame, text = 'Finish', bd=0, activebackground='#44db6f', font='Calibri 16',
                                       command=self.call_finish)
        self.finish_button.grid(row=5, column=3)
        ## Frame config
        self.frame.columnconfigure(tuple(range(5)), weight=1)
        self.frame.rowconfigure(tuple(range(3)), weight=1)
        self.frame.place(x=100, y=50, relwidth=0.5, relheight=0.5)
    def __init__(self):
        self.reg = register_form()
        if self.reg.login_opened:
            if self.reg.log_form.isreg:
                self.data = self.reg.log_form.data
                print(self.data)
                try:
                    self.reg.log_form.form.destroy()
                    self.reg.root.destroy()
                except:
                    pass
                self.root = tk.Tk()
                self.edit_form()
                self.db = DB()
                self.root.iconbitmap('static/icon.ico')
                self.root.mainloop()
        elif not self.reg.login_opened:
            if self.reg.registered:
                self.data = self.reg.data
                print(self.data)
                self.root = tk.Tk()
                self.edit_form()
                self.db = DB()
                self.root.iconbitmap('static/icon.ico')
                self.root.mainloop()
        else:
            return Error()


m = main_app()