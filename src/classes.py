"""
Classes utilisees par le client et serveur pour manipuler les informations plus efficacement
"""
import json

class Contact():
    nom : str
    prenom : str
    telephone : str
    courriel : str
    adresse : str


    def __init__(self, nom : str, prenom : str, telephone : str, courriel : str, adresse : str):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.courriel = courriel
        self.adresse = adresse

    def dump(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def load(string):
            self = json.loads(string)

class Annuaire():
    contacts = []

    def __init__(self):
        self.contacts = []

    def dump(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load(string):
            self = json.loads(string)
    

class Utilisateur():
    identifiant : str
    password : str
    annuaire : Annuaire
    acces = []

    def __init__(self, id : str, pwd : str):
        self.identifiant = id
        self.password = pwd
        self.annuaire = Annuaire()
        self.acces = []

    def dump(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load(string):
            self = json.loads(string)