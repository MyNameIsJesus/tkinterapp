from converter import *
from converter import DB
import tkinter as tk
from tkinter import *
from tkinter import font
from app1 import login_form
from errorwindow import *
import re


class register_form():

    def open_login(self):
        self.login_opened = True
        self.root.withdraw()
        self.log_form = login_form()
        if self.log_form.login_opened == False:
            print('F')
            self.root.deiconify()
        elif self.log_form.login_opened == True:
            self.root.destroy()

    def action(self):
        if self.entry_name.get() =='' or self.entry_pin.get()=='' or self.entry_card.get()=='' or self.entry_cvv.get()=='' or self.entry_city.get() =='' or self.entry_mail.get() =='' or self.entry_place.get()=='':
            return Error()
        if not len(self.entry_card.get()) == 16:
            return Error()
        if not len(self.entry_pin.get()) == 4:
            return Error()
        if not re.match(r'\w+@\w+', self.entry_mail.get()):
            return not_a_mail()
        try:
            s = len(self.db.get_elems(self.entry_card.get(), self.entry_pin.get()))
            if s != 0:
                return already_registrated_error()
        except:
            pass
        geoloc = {}
        geo = [self.entry_country.get(), self.entry_city.get(), self.entry_place.get()]
        gm = geomatch()
        try:
            geoloc['country'] = str(gm.sendrequest(geo[0] + ', ' + geo[1])).split(',')[-1]
            geoloc['city']= str(gm.sendrequest(geo[0] + ', ' + geo[1])).split(',')[0]
            geoloc['place']=str(gm.sendrequest(geo[0] + ', ' + geo[1]+ ', '+ geo[-1])).split(',')[0]
            self.db.add_elems(3,self.entry_name.get(), geoloc['country'], geoloc['city'], geoloc['place'], self.entry_card.get(), self.entry_pin.get(), self.entry_cvv.get(), self.entry_mail.get() )
            del geoloc, geo
        except:
            return Error()

        self.data = self.db.get_elems(self.entry_card.get(), self.entry_pin.get())
        self.registered = True
        self.root.destroy()
    def edit_page(self):
        ## Limit func cvv

        def limitSizeDay(*args):
            value = dayValue.get()
            if len(value) > 3 and value.isdigit(): dayValue.set(value[:3])
            elif not value.isdigit(): dayValue.set((''))
        dayValue = StringVar()
        dayValue.trace('w', limitSizeDay)

        def limitSizeCard(*args):
            value = cardValue.get()
            if len(value) > 16 and value.isdigit(): cardValue.set(value[:16])
            elif not value.isdigit(): cardValue.set((''))
        cardValue = StringVar()
        cardValue.trace('w', limitSizeCard)

        def limitSizeDay1(*args):
            value = dayValue1.get()
            if len(value) > 4 and value.isdigit(): dayValue1.set(value[:4])
            elif not value.isdigit(): dayValue1.set((''))
        dayValue1 = StringVar()
        dayValue1.trace('w', limitSizeDay1)

        # def cardWriting(*args):
        #     value = card_var.get()
        #     if len(value) % 4 == 0 and value.isdigit() and len(value) < 19: card_var.set(value[:len(value)] + ' ')
        #     elif not value.isdigit(): card_var.set((''))
        # card_var = StringVar()
        # card_var.trace('w', cardWriting)
        ##left

        ### name field
        self.label=tk.Label(text='Name', font='Calibri 16')
        self.label.place(x=25, y=97)
        self.entry_name=tk.Entry(width=25, font='Calibri 14')
        self.entry_name.place(x=100, y = 100)

        ### country field
        self.label = tk.Label(text='Country', font='Calibri 16')
        self.label.place(x=25, y=147)
        self.entry_country=tk.Entry(width=25, font='Calibri 14')
        self.entry_country.place(x=100, y=150)

        ##city field
        self.label = tk.Label(text='City', font='Calibri 16')
        self.label.place(x=25, y=197)
        self.entry_city=tk.Entry(width=25, font='Calibri 14')
        self.entry_city.place(x=100, y=200)

        ## place
        self.label = tk.Label(text='Place', font='Calibri 16')
        self.label.place(x=25, y=247)
        self.entry_place=tk.Entry(width=25, font='Calibri 14')
        self.entry_place.place(x=100, y=250)

        ### right

        ## Card
        self.label=tk.Label(text='Card', font='Calibri 16')
        self.label.place(x=380, y=97)
        self.entry_card=tk.Entry(width=25, font='Calibri 14',textvariable=cardValue)
        self.entry_card.place(x=440, y = 100)

        ## PIN
        self.label = tk.Label(text='PIN', font='Calibri 16')
        self.label.place(x=380, y=147)
        self.entry_pin=tk.Entry(width=25, font='Calibri 14', textvariable=dayValue1, show="*")
        self.entry_pin.place(x=440, y=150)

        ## CVV
        self.label = tk.Label(text='CVV', font='Calibri 16')
        self.label.place(x=380, y=197)
        self.entry_cvv=tk.Entry(width=25, font='Calibri 14', textvariable=dayValue)
        self.entry_cvv.place(x=440, y=200)

        ## e-mail
        self.label = tk.Label(text='E-mail', font='Calibri 16')
        self.label.place(x=380, y=247)
        self.entry_mail=tk.Entry(width=25, font='Calibri 14')
        self.entry_mail.place(x=440, y=250)

        ## Button
        self.btn=tk.Button(self.root, text='Register',  width=10, height = 1, activebackground='#84c3d1', activeforeground='black', bd=0, font= 'Times 14', command=self.action)
        self.btn.place(x=355, y=500)


        ## Log In
        f = font.Font(family='Calibri', size='11',)
        f.configure(underline=True)
        self.login = tk.Label(text='Already registrated? Log in', font=f, fg='#4240a1')
        self.login.place(x=320, y = 540)
        self.login.bind('<Button>', lambda e:self.open_login())

    def run(self):
        self.root.mainloop()

    def __init__(self):
        self.root = tk.Tk()
        self.login_opened = False
        self.root.geometry('800x600')
        self.root.title('Register')
        self.edit_page()
        self.root.resizable(False, False)
        self.db = DB()
        self.registered = False
        self.root.iconbitmap('static/icon.ico')
        self.root.mainloop()

