from genericpath import isfile
import os
from serveur import *
from os import path, remove
import unittest

"""
Le module 'unittest' est utilisé pour tester unitairement les fonctions python.
Plus d'infos : https://docs.python.org/fr/3.9/library/unittest.html#module-unittest
"""

# user1.addAcces("annuaire_axeldelas")

# ctc = Contact("Aoun", "Andre", "0123456789","andre.aoun@mail.fr","1 Impasse Sanzissu 31000 TOULOUSE")

# creerUtilisateur(user1)
# creerUtilisateur(user2)

# ajouterContact(user2, ctc)

# rechercherContact(user1, prenom="Andre", telephone="0123456789")

class testServeur(unittest.TestCase):

    def test_constructeurUtilisateur(self):
        """
        Rôle : test du constructeur Utilisateur()
        """
        print("[TEST] constructeurUtilisateur")

        with open("test/jeu_id.txt", 'r') as fichier_test_id:
            for ligne in fichier_test_id:
                
                ligne = ligne.split(";")
                utilisateur = Utilisateur(ligne[0], ligne[1])

                # tests des instances
                self.assertIsInstance(utilisateur, Utilisateur)         # objet 'utilisateur' est bien une instance de la classe 'Utilisateur'
                self.assertIsInstance(utilisateur.annuaire, Annuaire)
                self.assertIsInstance(utilisateur.annuaire.contacts, list)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:",utilisateur.annuaire.contacts[0])
                # tests des attributs
                self.assertEqual(utilisateur.identifiant, ligne[0])     # attribut 'identifiant' est de la bonne valeur
                self.assertEqual(utilisateur.password, ligne[1])        # attribut 'password' est de la bonne valeur
                self.assertEqual(len(utilisateur.annuaire.contacts), 0) # liste de contacts est bien vide
                self.assertEqual(len(utilisateur.acces), 0)             # liste des annuaires accessibles vide
                
                # tests des méthodes
                self.assertEqual(utilisateur.addAcces("annuaire_aminenm.json").acces[0], "annuaire_aminenm.json")
                self.assertEqual(utilisateur.getAcces(), ["annuaire_aminenm.json"])
                self.assertEqual(utilisateur.removeAcces("annuaire_aminenm.json").acces, [] )

    
    def test_creerUtilisateur(self):
        """
        Rôle : test de la fonction creerUtilisateur
        """
        print("[TEST] creerUtilisateur")
        
        nom_fichier_test_id = "test/jeu_id.txt"
        
        with open(nom_fichier_test_id, 'r') as fichier_test_id:
            for ligne in fichier_test_id:
                
                ligne = ligne.split(";")
                utilisateur = Utilisateur(ligne[0], ligne[1])

                creerUtilisateur(utilisateur)

                nom_annuaire = "serveur/annuaire/annuaire_"+utilisateur.identifiant+".json"
                self.assertTrue(path.isfile(nom_annuaire))
                
                champ_id_utilisateur = utilisateur.identifiant+" "+utilisateur.password

                with open("serveur/identifiants.txt", 'r') as fichier_id:
                    self.assertTrue(champ_id_utilisateur in fichier_id.read())
                    

    def test_ajouterContact(self):
        """
        Rôle : tester la fonction d'ajout de contact
        """

        nom_fichier_test_contact = "test/jeu_contact.txt"
        
        utilisateur = Utilisateur("aminenm","e888b69bd484efa688bca24eeeed5ae520f182176f415604bbb83ce9cb360624")
        creerUtilisateur(utilisateur)

        nom_annuaire_utilisateur = "serveur/annuaire/annuaire_"+utilisateur.identifiant+".json"
        
        with open(nom_fichier_test_contact, 'r') as fichier_test_contact:

            for ligne in fichier_test_contact:
                ligne = ligne.split(";")

                contact = Contact(nom=ligne[0], prenom=ligne[1], telephone=ligne[2], courriel=ligne[3], adresse=ligne[4])
                ajouterContact(utilisateur, contact)

                with open(nom_annuaire_utilisateur, 'r') as fichier_annuaire:

                    annuaire = json.load(fichier_annuaire, object_hook=convert_to_obj)

                    self.assertEqual(annuaire.contacts[-1], contact)



                

    def test_rechercherContact(self):
        pass

    @classmethod
    def tearDownClass(cls):
        """
        Rôle : nettoyage des fichiers et répertoires modifiés lors de l'exécution des tests
        """
        print("[INFO] nettoyage du dossier serveur/annuaire/*")
        for fichier in os.listdir("serveur/annuaire/"):
            os.remove(os.path.join("serveur/annuaire/", fichier))

        with open("serveur/identifiants.txt", "w") as fichier_id:
            print("[INFO] nettoyage du fichier serveur/identifiant.txt")
            fichier_id.truncate(0)
            
if __name__ == "__main__":
    unittest.main(verbosity=1)