"""
Classes utilisees par le client et serveur pour manipuler les informations plus efficacement
"""
import json
import typing
class Contact():
    nom : str
    prenom : str
    telephone : str
    courriel : str
    adresse : str


    def __init__(self, nom : str, prenom : str, telephone : str, courriel : str, adresse : str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.courriel = courriel
        self.adresse = adresse

    def dump(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def load(self, string):
            self = json.loads(string)
            return self

class Annuaire():
    contacts = []

    def __init__(self, loadFromString = False, string="") -> None:
        if not loadFromString:
            self.contacts = []
        else:
            self = self.load(string)

    def addContact(self, contact : Contact):
        self.contacts.append(contact)
        return self

    def getContacts(self) -> list[Contact]:
        return self.contacts

    def setContacts(self, contacts : list[Contact]):
        self.contacts = contacts
        return self

    def dump(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load(self, savedJson : str):
        self = json.loads(savedJson)
        return self
    
    def __str__(self) -> str:
        return " ".join(self.contacts)
    
    

class Utilisateur():
    identifiant : str
    password : str
    annuaire : Annuaire
    acces = []

    def __init__(self, id : str, pwd : str) -> None:
        self.identifiant = id
        self.password = pwd
        self.annuaire = Annuaire()
        self.acces = []

    def addAcces(self, filename : str):
        self.acces.append(filename)
        return self

    def getAcces(self) -> list[str]:
        return self.acces

    def dump(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load(self, savedJson : str):
        self = json.loads(savedJson)
        return self