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
        utilisateur.annuaire.dump(fichier)
    
    #with open("identifiants.txt", "a") as fichier_id:
    #  # Ouverture du fichier en mode ajout et écriture des identifiants de connexion
    #    fichier_id.write(utilisateur.identifiant+' '+utilisateur.password+'\n')

def ajouterContact(utilisateur : Utilisateur, contact : Contact):
    """
    Fonction ajoutant un contact dans l'annuaire de l'utilisateur passé en paramètre
    """
    utilisateur.annuaire.contacts.append(contact)

    nom_fichier = f"annuaire_{utilisateur.identifiant}.json"
    
    with open("server/annuaire/"+nom_fichier,'w') as fichier:
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
        with open(f"server/annuaire/{annuaire}.json","r") as fichier_annuaire:
            annuaire_lu = json.load(fichier_annuaire, object_hook=convert_to_obj)

        for contact in annuaire_lu.contacts:
            correspondance = False

            for attribut_reference, attribut_contact in zip(vars(reference).items(), vars(contact).items()):
                print("ref(",attribut_reference,") et comp(",attribut_contact,"")
                if attribut_reference == None or attribut_contact == None:
                    continue
                if attribut_reference == attribut_contact:
                    correspondance = True
                else:
                    correspondance = False
                    break
            liste_correspondance.append(contact)
        set(liste_correspondance)
        
        print(liste_correspondance)
def main():
    print("[STARTING]   server is starting...")
    print("[LISTENING]  server is listening")
    
    user1 = Utilisateur("aminenaim", "pwd")
    user2 = Utilisateur("axeldelas","pwdaxel")
    
    user1.addAcces("annuaire_axeldelas")
    
    ctc = Contact("Andre", "Aoun", "0123456789","andre.aoun@mail.fr","1 Impasse Sanzissu 31000 TOULOUSE")
    
    creerUtilisateur(user1)
    creerUtilisateur(user2)
    
    ajouterContact(user2, ctc)
    
    rechercherContact(user1, nom="Andre")

if __name__ == "__main__":
    main()