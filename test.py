import unittest

from combat import COMBAT_RESULTS_TABLE, KILL, table_coups


class TestTableCoups(unittest.TestCase):
    def test_exemple_du_livre(self):
        # « Règles de combat » : quotient -3, chiffre 6 -> le LS perd 3, le Diable Volant perd 6
        self.assertEqual(table_coups(-3, 6), (6, 3))

    def test_colonnes_limites(self):
        self.assertEqual(table_coups(0, 1), (3, 5))
        self.assertEqual(table_coups(-1, 1), (2, 5))
        self.assertEqual(table_coups(-2, 1), (2, 5))
        self.assertEqual(table_coups(1, 1), (4, 5))
        self.assertEqual(table_coups(10, 1), (8, 3))
        self.assertEqual(table_coups(11, 1), (9, 3))
        self.assertEqual(table_coups(-11, 3), (0, 8))
        self.assertEqual(table_coups(40, 3), table_coups(11, 3))
        self.assertEqual(table_coups(-40, 3), table_coups(-11, 3))

    def test_tue_sur_le_coup(self):
        self.assertEqual(table_coups(-11, 1), (0, KILL))
        self.assertEqual(table_coups(-9, 2), (0, 8))
        self.assertEqual(table_coups(11, 9), (KILL, 0))
        self.assertEqual(table_coups(7, 0), (KILL, 0))

    def test_le_10_de_la_table_de_hasard_vaut_0(self):
        for quotient in range(-12, 13):
            self.assertEqual(table_coups(quotient, 10), table_coups(quotient, 0))

    def test_plus_le_quotient_est_haut_mieux_c_est(self):
        order = lambda loss: float("inf") if loss is KILL else loss
        for dice, row in COMBAT_RESULTS_TABLE.items():
            enemy = [order(e) for e, _ in row]
            ls = [order(l) for _, l in row]
            self.assertEqual(enemy, sorted(enemy), f"ligne {dice}")
            self.assertEqual(ls, sorted(ls, reverse=True), f"ligne {dice}")


if __name__ == "__main__":
    unittest.main()
