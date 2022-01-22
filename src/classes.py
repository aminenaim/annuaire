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

    def __init__(self, nom='', prenom='', courriel='', telephone='', adresse='') -> None:
        self.nom = nom
        self.prenom = prenom
        self.courriel = courriel
        # les champs 'telephone' et 'adresse' sont facultatifs donc vide si pas renseignés par l'utilisateur
        self.telephone = telephone
        self.adresse = adresse

    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    def afficherContact(self):
        print(f"         ╮ Nom : {self.nom} \n",
              f"        │ Prénom : {self.prenom} \n",
              f"Contact │ Téléphone : {self.telephone} \n",
              f"        │ Courriel : {self.courriel} \n",
              f"        ╯ Adresse : {self.adresse} \n")

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} {self.telephone} {self.courriel} {self.adresse}"


class Annuaire:
    contacts = []

    def __init__(self, contacts=None) -> None:
        if contacts is None:
            contacts = []
        self.contacts = contacts

    def addContact(self, contact: Contact):
        self.contacts.append(contact)
        return self

    def getContacts(self) -> 'list[Contact]':
        return self.contacts

    def setContacts(self, contacts: 'list[Contact]'):
        self.contacts = contacts
        return self

    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    def __str__(self) -> str:
        return "\n".join([contact.__str__() for contact in self.contacts])


class Utilisateur:
    identifiant: str
    password: str
    annuaire: Annuaire
    acces = []

    def __init__(self, identifiant: str, pwd: str) -> None:
        self.identifiant = identifiant
        self.password = pwd
        self.annuaire = Annuaire()
        self.acces = []

    def addAcces(self, identifiant: str):
        filename = "annuaire_" + identifiant + ".json"
        self.acces.append(filename)
        return self

    def getAcces(self) -> 'list[str]':
        return self.acces

    def removeAcces(self, nom_fichier: str):
        self.acces.remove(nom_fichier)
        return self

    def dump(self, jsonFile):
        return json.dump(self, jsonFile, default=convert_to_dict, sort_keys=True, indent=4, )

    def __str__(self) -> str:
        return f"{self.identifiant} {self.password} {self.annuaire}\n" + '\n'.join(self.acces)


def convert_to_dict(obj):
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__
    }

    obj_dict.update(obj.__dict__)
    return obj_dict


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