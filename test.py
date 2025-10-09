import unittest
from utils import table_coups


class TestTableCoups(unittest.TestCase):

    def test_dommages_pour_quotient_attaque_eleve(self):
        # Test avec un quotient d'attaque élevé et un dé de valeur élevée
        dommage_LS, dommage_ennemi = table_coups(20, 10)
        self.assertEqual(dommage_LS, 0)
        self.assertEqual(dommage_ennemi, T)

    def test_dommages_pour_quotient_attaque_faible(self):
        # Test avec un quotient d'attaque faible et un dé de valeur faible
        dommage_LS, dommage_ennemi = table_coups(-10, 2)
        self.assertEqual(dommage_LS, T)
        self.assertEqual(dommage_ennemi, 0)

    def test_dommages_pour_quotient_attaque_moyen(self):
        # Test avec un quotient d'attaque moyen et un dé de valeur moyenne
        dommage_LS, dommage_ennemi = table_coups(5, 5)
        self.assertEqual(dommage_LS, 2)
        self.assertEqual(dommage_ennemi, 8)

    def test_dommages_pour_quotient_attaque_limite(self):
        # Test avec le quotient d'attaque aux limites (-49, 49) et divers dés
        dommage_LS, dommage_ennemi = table_coups(49, 10)
        self.assertEqual(dommage_LS, 0)
        self.assertEqual(dommage_ennemi, T)

        dommage_LS, dommage_ennemi = table_coups(-49, 10)
        self.assertEqual(dommage_LS, T)
        self.assertEqual(dommage_ennemi, 0)

    def test_dommages_pour_combinaisons_particulieres(self):
        # Tests pour des combinaisons particulières de quotient d'attaque et de valeur de dé
        dommage_LS, dommage_ennemi = table_coups(0, 7)
        self.assertEqual(dommage_LS, 1)
        self.assertEqual(dommage_ennemi, 10)

        dommage_LS, dommage_ennemi = table_coups(9, 8)
        self.assertEqual(dommage_LS, 3)
        self.assertEqual(dommage_ennemi, 9)
