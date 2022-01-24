import unittest
from os import path

from serveur import *

"""
Le module 'unittest' est utilisé pour tester unitairement les fonctions python.
Plus d'infos : https://docs.python.org/fr/3.9/library/unittest.html#module-unittest
"""

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


class testServeur(unittest.TestCase):

    def test_constructeurUtilisateur(self):
        """
        Rôle : test du constructeur Utilisateur()
        """
        try:
            identifiant = "Spirou"
            password = "a226176847c3f8f4007cb3b5e98186ae9b949ad4337f6457f966c11ced00f2c0"
            utilisateur = Utilisateur(identifiant, password)
        
            # tests des instances
            self.assertIsInstance(utilisateur,
                                Utilisateur)
                            # objet 'utilisateur' est bien une instance de la classe 'Utilisateur'
            self.assertIsInstance(utilisateur.annuaire, Annuaire)
            self.assertIsInstance(utilisateur.annuaire.contacts, list)
            self.assertIsInstance(utilisateur.annuaire.acces, list)


            # tests des attributs
            self.assertEqual(utilisateur.identifiant, identifiant)  # attribut 'identifiant' est de la bonne valeur
            self.assertEqual(utilisateur.password, password)  # attribut 'password' est de la bonne valeur
            self.assertEqual(len(utilisateur.annuaire.contacts), 0)  # liste de contacts est bien vide
            self.assertEqual(len(utilisateur.annuaire.acces), 0)  # liste des annuaires accessibles vide

            # tests des méthodes
            self.assertEqual(utilisateur.annuaire.addAcces("tintin").acces[0], "annuaire_tintin.json")
            self.assertEqual(utilisateur.annuaire.acces, ["annuaire_tintin.json"])
            self.assertEqual(utilisateur.annuaire.removeAcces("annuaire_tintin.json").acces, [])

            # Gestion des erreurs
            self.assertRaises(ValueError, Utilisateur, "Ibn-Abou-Bekhr","35ed65b1eb2e87086e8d7ea0154e88d77febb8fc53af307f2a543b2d44767df0")

        except Exception:
            print("[TEST] constructeurUtilisateur" + "\t\t\t\t[" + RED + "KO" + RESET + "]")

        else:
            print("[TEST] constructeurUtilisateur" + "\t\t\t\t[" + GREEN + "OK" + RESET + "]")



    def test_creerUtilisateur(self):
        """
        Rôle : test de la fonction creerUtilisateur
        """
        try:
            identifiant = "Spirou"
            password = "a226176847c3f8f4007cb3b5e98186ae9b949ad4337f6457f966c11ced00f2c0"

            # Instanciation et création de l'utilisateur itéré
            utilisateur = Utilisateur(identifiant, password)
            creerUtilisateur(utilisateur)

            # Vérification de l'existance d'un annuaire vierge pour l'utilisateur précédemment créé
            nom_annuaire = "serveur/annuaire/annuaire_" + utilisateur.identifiant + ".json"
            self.assertTrue(path.isfile(nom_annuaire))

            champ_id_utilisateur = utilisateur.identifiant + ' ' + utilisateur.password

            # Vérification que les données de l'utilisateur ont été ajouté dans le fichier identifiants.txt
            with open("serveur/identifiants.txt", 'r') as fichier_id:
                self.assertTrue(champ_id_utilisateur in fichier_id.read())

        except Exception:
            print("[TEST] creerUtilisateur..." + "\t\t\t\t[" + RED + "KO" + RESET + "]")
        
        else:
            print("[TEST] creerUtilisateur..." + "\t\t\t\t[" + GREEN + "OK" + RESET + "]")


    def test_constructeur_contact(self):
        """
        Rôle : test du constructeur Utilisateur()
        """
        try:
            contact = Contact("Tapioca", "General","general@tapioca.fr","0619761954","San Théodoros")
            # tests des instances
            self.assertIsInstance(contact,
                                Contact)
                            # objet 'utilisateur' est bien une instance de la classe 'Utilisateur'
            self.assertIsInstance(contact.nom, str)
            self.assertIsInstance(contact.prenom, str)
            self.assertIsInstance(contact.courriel, str)
            self.assertIsInstance(contact.telephone, str)
            self.assertIsInstance(contact.adresse, str)

            # tests des attributs
            self.assertEqual(contact.nom, "Tapioca")  # attribut 'nom' est de la bonne valeur
            self.assertEqual(contact.prenom, "General")  # attribut 'prenom' est de la bonne valeur
            self.assertEqual(contact.courriel, "general@tapioca.fr")  # attribut 'courriel' est de la bonne valeur
            self.assertEqual(contact.telephone, "0619761954")  # attribut 'telephone' est de la bonne valeur
            self.assertEqual(contact.adresse, "San Théodoros")  # attribut 'adresse' est de la bonne valeur

            # Gestion des erreurs
            self.assertRaises(ValueError, Contact, "R2", "D2", "r2@d2.fr", "073283627SS25","Galaxie lointaine, très lointaine")

        except Exception:
            print("[TEST] constructeurContact" + "\t\t\t\t[" + RED + "KO" + RESET + "]")

        else:
            print("[TEST] constructeurContact" + "\t\t\t\t[" + GREEN + "OK" + RESET + "]")
        


    def test_ajouterContact(self):
        """
        Rôle : tester la fonction d'ajout de contact
        """
        try:
            # Instanciation et création de l'utilisateur test
            utilisateur = Utilisateur("tintin", "e888b69bd484efa688bca24eeeed5ae520f182176f415604bbb83ce9cb360624")
            creerUtilisateur(utilisateur)

            # Récupération du nom de fichier étant l'annuaire de l'utilisateur test
            nom_annuaire_utilisateur = "serveur/annuaire/annuaire_" + utilisateur.identifiant + ".json"

            # Instanciation du contact itéré et ajout dans l'annuaire de l'utilisateur test
            contact = Contact(nom="Zorglub", prenom="Bulgroz", telephone="0719592017",
                                courriel="zor@glub", adresse="Zorgland")
            ajouterContact(utilisateur, contact)

            # Vérification que le contact itéré a bien été ajouté à la suite de l'annuaire de l'utilisateur test
            with open(nom_annuaire_utilisateur, 'r') as fichier_annuaire:
                annuaire = json.load(fichier_annuaire, object_hook=convert_to_obj)

                self.assertEqual(annuaire.contacts[-1].__str__(), contact.__str__())

        except Exception:
            print("[TEST] ajouterContact..." + "\t\t\t\t[" + RED + "KO" + RESET + "]")

        else:
            print("[TEST] ajouterContact..." + "\t\t\t\t[" + GREEN + "OK" + RESET + "]")


    def test_rechercherContact(self):
        """
        Rôle : tester la fonction rechercher contact
        """
        try:
            # Instanciation des utilisateurs de tests
            utilisateurA = Utilisateur("aminenm", "e888b69bd484efa688bca24eeeed5ae520f182176f415604bbb83ce9cb360624")
            utilisateurB = Utilisateur("axeldls", "83701221e23873688094872e3464d6172ae557fb823c84af704f2ff39afa2b17")

            # Ajout des utilisateurs dans les registres
            creerUtilisateur(utilisateurA)
            creerUtilisateur(utilisateurB)

            # Ajout à utilisateurA de l'accès en lecture aux annuaire de l'utilisateur B
            utilisateurA.annuaire.addAcces(utilisateurB.identifiant)

            # Instanciation des contacts de tests
            contact1 = Contact(nom="Tournesol", prenom="Tryphon", courriel="professeur@tournesol.com",
                            telephone="0719431961", adresse="Château de Moulinsart")
            contact2 = Contact(nom="Haddock", prenom="Archibald", courriel="capitaine@haddock.com", telephone="0719412011",
                            adresse="Château de Moulinsart")

            # Ajout des contacts de tests dans l'annuaire de l'utilisateurB
            ajouterContact(utilisateurB, contact1)
            ajouterContact(utilisateurB, contact2)

            # Test de la recherche d'un contact de nom "Tournesol" dans les annuaires accessibles d'utilisateurB
            resultat_rechercherContact = rechercherContact(utilisateurA, nom="Tournesol")
            self.assertEqual(len(resultat_rechercherContact), 1)
            self.assertEqual(resultat_rechercherContact[0].__str__(), contact1.__str__())

            # Test de la recherche d'un contact à l'adresse "Château de Moulinsart" dans les annuaires accessibles d'utilisateurB
            resultat_rechercherContact = rechercherContact(utilisateurA, adresse="Château de Moulinsart")
            self.assertEqual(len(resultat_rechercherContact), 2)
            self.assertEqual(resultat_rechercherContact[0].__str__(), contact1.__str__())
            self.assertEqual(resultat_rechercherContact[1].__str__(), contact2.__str__())

            # Test de la recherche d'un contact non présent dans les annuaires d'utilisateurB
            resultat_rechercherContact = rechercherContact(utilisateurA, prenom="Milou")
            self.assertEqual(len(resultat_rechercherContact), 0)

        except Exception:
            print("[TEST] rechercherContact..." + "\t\t\t\t[" + RED + "KO" + RESET + "]")

        else:
            print("[TEST] rechercherContact..." + "\t\t\t\t[" + GREEN + "OK" + RESET + "]")
            
    @classmethod
    def nettoyer(cls):
        """
        Rôle : nettoyage des fichiers et répertoires modifiés lors de l'exécution des tests
        """

        # Suppression de tous les fichiers annuaires
        for fichier in os.listdir("serveur/annuaire/"):
            os.remove(os.path.join("serveur/annuaire/", fichier))

        # Reset du fichier identifiants.txt
        with open("serveur/identifiants.txt", "w") as fichier_id:
            fichier_id.truncate(0)

        print("[INFO] nettoyage du dossier serveur/annuaire/*" + "\t\t[" + GREEN + "OK" + RESET + "]")
        print("[INFO] nettoyage du fichier serveur/identifiant.txt" + "\t[" + GREEN + "OK" + RESET + "]")


test = testServeur()

test.test_constructeurUtilisateur()
test.test_creerUtilisateur()
test.nettoyer()

test.test_constructeur_contact()
test.test_ajouterContact()
test.nettoyer()

test.test_rechercherContact()
test.nettoyer()