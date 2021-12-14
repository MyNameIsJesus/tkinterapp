import sqlite3
from functools import partial
from geopy.geocoders import Nominatim
class DB():

    def create_table(self):
        self.mybase.execute('CREATE TABLE Important_Data (ID INT, Name TEXT(100), Country TEXT(100), City TEXT(100), '
                          'Place TEXT(100), Credit TEXT(16), PIN INT(4), CVV2 INT, Email TEXT, PRIMARY KEY (ID))')

    def check_elems(self, card, PIN):
        self.open_base()
        l1 = []
        self.cursor.execute('SELECT * FROM Important_Data WHERE Credit = ? AND PIN = ?', (card, PIN,))
        rows = self.cursor.fetchall()
        for row in rows:
            l1 = list(row)
        print(l1)
        if len(l1) == 0:
            return False
        else:
            return True

    def get_elems(self, card, PIN):
        self.mybase = self.open_base()
        self.cursor = self.mybase.cursor()
        self.cursor.execute('SELECT * FROM Important_Data WHERE Credit = ? AND PIN = ?', (card, PIN,))
        rows = self.cursor.fetchall()
        for row in rows:
            l1 = list(row)
        return l1

    def update_name(self, param, old, id, new):
        self.mybase = self.open_base()
        self.cursor = self.mybase.cursor()
        if param == 'Name':
            command = """UPDATE Important_Data SET Name = ? WHERE Name = ? AND ID = ?"""
        elif param == 'Country':
            command = """UPDATE Important_Data SET Country = ? WHERE Country = ? AND ID = ?"""
        elif param == 'City':
            command = """UPDATE Important_Data SET City = ? WHERE City = ? AND ID = ?"""
        elif param == 'Place':
            command = """UPDATE Important_Data SET Place = ? WHERE Place = ? AND ID = ?"""
        elif param == 'Credit':
            command = """UPDATE Important_Data SET Credit = ? WHERE Credit = ? AND ID = ?"""
        elif param == 'PIN':
            command = """UPDATE Important_Data SET PIN = ? WHERE PIN = ? AND ID = ?"""
        elif param == 'CVV2':
            command = """UPDATE Important_Data SET CVV2 = ? WHERE CVV2 = ? AND ID = ?"""
        elif param == 'Email':
            command = """UPDATE Important_Data SET Email = ? WHERE Email = ? AND ID = ?"""
        self.cursor.execute(str(command), (new, old, int(id),))
        self.mybase.commit()
        self.cursor.close()

    # def update_country(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE Country = ? AND ID = ? SET Country = ? """
    #     self.cursor.execute(command, (old,id,new,))
    #
    # def update_city(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE City = ? AND ID = ? SET City = ?"""
    #     self.cursor.execute(command, (old,id,new,))
    #
    # def update_place(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE Place = ? AND ID = ? SET Place = ?"""
    #     self.cursor.execute(command, (old, id, new,))
    #
    # def update_card(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE Credit = ? AND ID = ? SET Credit = ?"""
    #     self.cursor.execute(command, (old, id, new,))
    #
    # def update_PIN(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE PIN = ? AND ID = ? SET PIN = ?"""
    #     self.cursor.execute(command, (old, id, new,))
    #
    # def update_cvv(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE CVV2 = ? AND ID = ? SET CVV2 = ?"""
    #     self.cursor.execute(command, (old, id, new,))
    #
    # def update_email(self, old, id, new):
    #     self.open_base()
    #     command = """UPDATE Important_Data WHERE Email = ? AND ID = ? SET Email = ?"""
    #     self.cursor.execute(command, (old, id, new,))

    def add_elems(self, id, name, country, city, place, card, pin, cvv, email):
        self.open_base()
        self.cursor = self.mybase.cursor()
        sqlite_insert_with_param = """INSERT INTO Important_Data
                                  (ID, Name,  Country, City, Place, Credit, PIN, CVV2, Email) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (id, name, country, city, place, card, pin, cvv, email)
        self.cursor.execute(sqlite_insert_with_param, data_tuple)
        self.mybase.commit()
        self.cursor.close()

    def open_base(self):
        return sqlite3.connect('myDataBase.db')


    def __init__(self):
        self.mybase = sqlite3.connect('myDataBase.db')
        try:
            self.create_table()
        except:
            pass
        self.cursor = self.mybase.cursor()

class geomatch():

    def sendrequest(self, place):
        return self.geocode(place)

    def __init__(self):
        self.geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
        self.geocode = partial(self.geolocator.geocode, language='en')

