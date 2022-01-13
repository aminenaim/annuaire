# from request import *
from classes import *


def handle_client(conn, addr):
    pass

def creerUtilisateur(utilisateur : Utilisateur):
    """
    Fonction ajoutant les identifiants de connexion de l'utilisateur dans un fichier centralisé
    Fonction créant un fichier annuaire pour l'utilisateur passé en parametre
    """
    nom_fichier = "annuaire_"+utilisateur.identifiant+".json"
    with open("server/annuaire/"+nom_fichier,'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé
        fichier.write(utilisateur.annuaire.dump())
    
    with open("identifiants.txt", "a") as fichier_id:
        # Ouverture du fichier en mode ajout et écriture des identifiants de connexion
        fichier_id.write(utilisateur.identifiant+' '+utilisateur.password+'\n')

def ajouterContact(utilisateur : Utilisateur, contact : Contact):
    """
    Fonction ajoutant un contact dans l'annuaire de l'utilisateur passé en paramètre
    """
    utilisateur.annuaire.contacts.append(contact)

    nom_fichier = "annuaire_"+utilisateur.identifiant+".json"
    
    with open("server/annuaire/"+nom_fichier,'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé mis à jour
        fichier.write(utilisateur.annuaire.dump())

def rechercherContact(utilisateur : Utilisateur, *args, **kwargs):
    """
    Fonction permettant de chercher dans la liste des annuaires accordées le contact demandé
    """
    nom = kwargs.get("nom", None)
    prenom = kwargs.get("prenom", None)
    telephone = kwargs.get("telephone", None)
    courriel = kwargs.get("courriel", None)
    adresse = kwargs.get("adresse", None)

    reference = Contact(nom, prenom, telephone, courriel, adresse)

    
    for annuaire in utilisateur.acces:
        with open("server/annuaire/"+annuaire+".json","r") as fichier_annuaire:
            donnees = fichier_annuaire.read()
            annuaire_lu = Annuaire
            annuaire_lu.load(donnees)
            print(len(annuaire_lu.contacts))

            for contact in annuaire_lu.contacts:
                correspondance = False
                print("iterating over annuaire")
                for attribut_reference, attribut_contact in vars(reference).items(), vars(contact).items:
                    if attribut_reference == None:
                        continue
                    if attribut_reference == attribut_contact:
                        correspondance = True
                    else:
                        correspondance = False
                        break
                
                    print(contact.nom)

print("[STARTING]   server is starting...")
print("[LISTENING]  server is listening")

user1 = Utilisateur("aminenaim", "pwd")
user2 = Utilisateur("axeldelas","pwdaxel")

user1.acces.append("annuaire_axeldelas")

ctc = Contact("André", "Aoun", "0123456789","andre.aoun@mail.fr","1 Impasse Sanzissu 31000 TOULOUSE")

creerUtilisateur(user1)
creerUtilisateur(user2)

ajouterContact(user2, ctc)
rechercherContact(user1, nom="Axel")