from classes import *
import os


def creerUtilisateur(utilisateur: Utilisateur):
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
    ├─ serveur.py
    └─ test_serveur.py
    """

    nom_fichier = "annuaire_" + utilisateur.identifiant + ".json"

    if not os.path.exists(f"serveur/annuaire/"):
        # Création du répertoire annuaire si inexistant
        os.mkdir("serveur/annuaire/")

    with open("serveur/identifiants.txt", "a") as fichier_id:
        # Ouverture du fichier en mode ajout et écriture des identifiants de connexion
        fichier_id.write(utilisateur.identifiant + ' ' + utilisateur.password)

    with open("serveur/annuaire/" + nom_fichier, 'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé
        utilisateur.annuaire.dump(fichier)


def ajouterContact(utilisateur: Utilisateur, contact: Contact):
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
    ├─ serveur.py
    └─ test_serveur.py
    """

    utilisateur.annuaire.addContact(contact)

    nom_fichier = f"annuaire_{utilisateur.identifiant}.json"

    with open("serveur/annuaire/" + nom_fichier, 'w') as fichier:
        # Ouverture du fichier en mode écriture et écriture de l'annuaire sérialisé mis à jour
        utilisateur.annuaire.dump(fichier)


def rechercherContact(utilisateur: Utilisateur, *args, **kwargs):
    """
    Fonction permettant de chercher dans la liste des annuaires accordées le contact demandé
    """
    nom = kwargs.get("nom", '')
    prenom = kwargs.get("prenom", '')
    telephone = kwargs.get("telephone", '')
    courriel = kwargs.get("courriel", '')
    adresse = kwargs.get("adresse", '')

    reference = Contact(nom, prenom, telephone, courriel, adresse)
    # Récupération des valeurs des attributs du contact de reference
    liste_attribut_reference = [t[1] for t in list(vars(reference).items())]

    liste_correspondance = []

    for annuaire in utilisateur.acces:
        # Parcours des annuaires accessibles en lecture

        with open(f"serveur/annuaire/{annuaire}", "r") as fichier_annuaire:
            # Ouverture de l'annuaire en mode lecture et désérialisation de l'annuaire
            annuaire_lu = json.load(fichier_annuaire, object_hook=convert_to_obj)

        for contact in annuaire_lu.contacts:
            # Parcours des contacts de l'annuaire
            correspondance = False

            # Récupération des valeurs des attributs du contact à l'itération actuelle
            liste_attribut_contact = [t[1] for t in list(vars(contact).items())]

            for attribut_reference, attribut_contact in zip(liste_attribut_reference, liste_attribut_contact):
                # Comparaison des valeurs de chaque attribut des deux contacts

                if attribut_reference == '' or attribut_contact == '':
                    # Passage à l'itération suivante si les champs d'au moins un des deux contacts est vide
                    continue
                elif attribut_reference == attribut_contact:
                    # Passage du flag correspondance à True quand les valeurs sont égales
                    correspondance = True
                else:
                    # Passage du flag correspondance à False quand les valeurs sont différentes
                    correspondance = False
                    # Arrêt de la boucle en cours car le contact ne correspond pas
                    break

            if correspondance:
                # Ajout du contact à notre liste de correspondance si le flag correspondance est à True
                liste_correspondance.append(contact)
                # contact.afficherContact()

    set(liste_correspondance) # Suppression des doublons dans le cas où deux annuaires ont un contact en commun
    return liste_correspondance
