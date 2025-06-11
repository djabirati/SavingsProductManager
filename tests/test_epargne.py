import unittest
from src.mon_module.models.epargne import Epargne


class TestEpargne(unittest.TestCase):

    def test_initialisation_complete(self):
        e = Epargne("Livret A", 0.03, 0.0, 0, 22950)

        self.assertEqual(e.nom, "Livret A")
        self.assertEqual(e.taux_interet, 0.03)
        self.assertEqual(e.fiscalite, 0.0)
        self.assertEqual(e.duree_min, 0)
        self.assertEqual(e.versement_max, 22950)