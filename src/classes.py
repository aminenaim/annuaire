"""
Classes utilisees par le client et serveur pour manipuler les informations plus efficacement
"""
import json


class Contact:
    nom: str
    prenom: str
    telephone: str
    courriel: str
    adresse: str

    # Constructeur afin d'instancier un objet de type Contact
    def __init__(self, nom='', prenom='', courriel='', telephone='', adresse='') -> None:
        self.nom = nom
        self.prenom = prenom
        self.courriel = courriel
        # les champs 'telephone' et 'adresse' sont facultatifs donc vide si pas renseignés par l'utilisateur
        self.telephone = telephone
        self.adresse = adresse

    # Méthode 'dump' afin de sérialiser et stocker l'instance en json
    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    # Méthode 'afficherContact' afin d'afficher graphiquement les informations du contact
    def afficherContact(self):
        print(f"         ╮ Nom : {self.nom} \n",
              f"        │ Prénom : {self.prenom} \n",
              f"Contact │ Téléphone : {self.telephone} \n",
              f"        │ Courriel : {self.courriel} \n",
              f"        ╯ Adresse : {self.adresse} \n")

    # Redéfinition de la méthode '__str__' afin d'afficher les informations du contact sur une ligne
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} {self.telephone} {self.courriel} {self.adresse}"


class Annuaire:
    contacts = []
    acces = []

    # Constructeur afin d'instancier un objet de type Annuaire
    def __init__(self, contacts=None, acces=None) -> None:
        if contacts is None:
            contacts = []
        self.contacts = contacts
        self.acces = []
    
    # Méthode 'addContact' afin d'ajouter un contact dans l'annuaire d'un utilisateur donné en paramètre
    def addContact(self, contact: Contact):
        self.contacts.append(contact)
        return self

    # Méthode 'addAcces' afin de donner le droit à un utilisateur distinct de lire l'annuaire
    def addAcces(self, identifiant: str):
        filename = "annuaire_" + identifiant + ".json"
        self.acces.append(filename) 
        return self

    # Méthode 'removeAcces' afin de retirer le droit à un utilisateur distinct de lire l'annuaire
    def removeAcces(self, nom_fichier: str):
        self.acces.remove(nom_fichier)
        return self

    # Méthode 'dump' afin de sérialiser et stocker l'instance en json
    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    # Redéfinition de la méthode '__str__' afin d'afficher les informations sur une ligne de chaque contact contenu dans l'annuaire
    def __str__(self) -> str:
        return "\n".join([contact.__str__() for contact in self.contacts]) + '\n'.join(self.acces)


class Utilisateur:
    identifiant: str
    password: str
    annuaire: Annuaire

    # Constructeur afin d'instancier un objet de type Utilisateur
    def __init__(self, identifiant: str, pwd: str) -> None:
        self.identifiant = identifiant
        self.password = pwd
        self.annuaire = Annuaire()

    # Méthode 'dump' afin de sérialiser et stocker l'instance en json
    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    # Redéfinition de la méthode '__str__' afin d'afficher les informations de l'utilisateur sur une ligne
    def __str__(self) -> str:
        return f"{self.identifiant} {self.password} {self.annuaire}\n"

# Fonction pour faciliter l'étape de sérialisation
def convert_to_dict(obj):
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    obj_dict.update(obj.__dict__)
    return obj_dict

# Fonction pour faciliter l'étape de désérialisation
def convert_to_obj(temp_dict):
    if "__class__" in temp_dict:

        class_name = temp_dict.pop("__class__")

        module_name = temp_dict.pop("__module__")

        module = __import__(module_name)

        class_ = getattr(module, class_name)

        obj = class_(**temp_dict)
    else:
        obj = temp_dict
    return obj