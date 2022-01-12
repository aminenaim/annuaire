"""
Classes utilisees par le client et serveur pour manipuler les informations plus efficacement
"""
from typing import *


class contact():
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

class typeAnnuaire():
    contacts : contact

    def __init__(self):
        self.contacts = contact
    

class utilisateur():
    identifiant : str
    password : str
    annuaire : typeAnnuaire

    def __init__(self, id : str, pwd : str):
        self.identifiant = id
        self.password = pwd
        self.annuaire = typeAnnuaire