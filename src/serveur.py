from classes import *

def creerUtilisateur(utilisateur : Utilisateur):
    """
    Fonction ajoutant les identifiants de connexion de l'utilisateur dans un fichier centralisé
    Fonction créant un fichier annuaire pour l'utilisateur passé en parametre

    src/
    ├─ __pycache__/
    ├─ serveur/
    │  ├─ annuaire/
    │  │  └─ annuaire_{utilisateur.identifiant}.json  <-- Création du fichier annuaire de l'utilisateur
    │  └─ identifiants.txt                            <-- Ajout des identifiants de connexion de l'utilisateur
    ├─ test/
    ├─ classes.py
    └─ serveur.py

    """
    
            
    nom_fichier = "annuaire_"+utilisateur.identifiant+".json"

    with open("serveur/identifiants.txt", "a") as fichier_id:
        # Ouverture du fichier en mode ajout et écriture des identifiants de connexion
        fichier_id.write(utilisateur.identifiant+' '+utilisateur.password)

    with open("serveur/annuaire/"+nom_fichier,'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé
        utilisateur.annuaire.dump(fichier)
    



def ajouterContact(utilisateur : Utilisateur, contact : Contact):
    """
    Fonction ajoutant un contact dans l'annuaire de l'utilisateur passé en paramètre

    src/
    ├─ __pycache__/
    ├─ serveur/
    │  ├─ annuaire/
    │  │  └─ annuaire_{utilisateur.identifiant}.json  <-- Mise à jour du fichier annuaire
    │  └─ identifiants.txt                            
    ├─ test/
    ├─ classes.py
    └─ serveur.py
    """
    utilisateur.annuaire.addContact(contact)

    nom_fichier = f"annuaire_{utilisateur.identifiant}.json"
    
    with open("serveur/annuaire/"+nom_fichier,'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé mis à jour
        utilisateur.annuaire.dump(fichier)




def rechercherContact(utilisateur : Utilisateur, *args, **kwargs):
    """
    Fonction permettant de chercher dans la liste des annuaires accordées le contact demandé
    """
    nom = kwargs.get("nom", '')
    prenom = kwargs.get("prenom", '')
    telephone = kwargs.get("telephone", '')
    courriel = kwargs.get("courriel", '')
    adresse = kwargs.get("adresse", '')

    reference = Contact(nom, prenom, telephone, courriel, adresse)
    
    liste_correspondance = []
    
    for annuaire in utilisateur.acces:
        with open(f"serveur/annuaire/{annuaire}","r") as fichier_annuaire:
            annuaire_lu = json.load(fichier_annuaire, object_hook=convert_to_obj)
        
        for contact in annuaire_lu.contacts:
            correspondance = False

            liste_attribut_reference = [tuple[1] for tuple in list(vars(reference).items())]
            liste_attribut_contact = [tuple[1] for tuple in list(vars(contact).items())]

            for attribut_reference, attribut_contact in zip(liste_attribut_reference, liste_attribut_contact):
                
                if attribut_reference == '' or attribut_contact == '':
                    continue
                elif attribut_reference == attribut_contact:
                    correspondance = True
                else:
                    correspondance = False
                    break

            if correspondance == True:

                liste_correspondance.append(contact)
                # contact.afficherContact()
    
    set(liste_correspondance)
    return liste_correspondance