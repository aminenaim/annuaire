from serveur import *
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
        with open("test/jeu_id.txt", 'r') as fichier_test:
            for ligne in fichier_test:
                
                ligne = ligne.split(";")
                utilisateur = Utilisateur(ligne[0], ligne[1])
                self.assertIsInstance(utilisateur, Utilisateur)
                self.assertEqual(utilisateur.identifiant, ligne[0])
                self.assertEqual(utilisateur.password, ligne[1])
                self.assertEqual(len(utilisateur.annuaire.contacts), 0)
            
                
    def test_creerUtilisateur(self):
        """
        Rôle : test de la fonction creerUtilisateur
        """
        with open("test/jeu_id.txt", 'r') as fichier_test:
            for ligne in fichier_test:
                
                ligne = ligne.split(";")
                utilisateur = Utilisateur(ligne[0], ligne[1])
                creerUtilisateur(utilisateur)
                
        

    def test_ajouterContact(self):
        pass

    def test_rechercherContact(self):
        pass

if __name__ == '__main__':
    unittest.main()