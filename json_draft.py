#RAFFINAGE 1

import json
import typing as t
import socket
#client + serveur

class requestType(Enum):
    AUTH = 0
    CREATE = 1
    DELETE = 2
    CHANGE = 3
    VIEW = 4

class directory():
    name : str
    phone_number : str
    postal_adress : str
    mail_adress : str

    def _init_(self, name, phone_number, postal_adress, mail_adress):
        self.name = name
        self.phone_number = phone_number
        self.postal_adress = postal_adress
        self.mail_adress = mail_adress

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4) 
