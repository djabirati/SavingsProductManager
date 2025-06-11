import unittest
from src.mon_module.models.personne import Personne


class TestPersonne(unittest.TestCase):

    def test_initialisation_valide(self):
        p = Personne("Alice", 30, 45000, 1000, 500, 50000, 10, 200)

        self.assertEqual(p.nom, "Alice")
        self.assertEqual(p.age, 30)
        self.assertEqual(p.revenu_annuel, 45000)
        self.assertEqual(p.loyer, 1000)
        self.assertEqual(p.depenses_mensuelles, 500)
        self.assertEqual(p.objectif, 50000)
        self.assertEqual(p.duree_epargne, 10)
        self.assertEqual(p.versement_mensuel_utilisateur, 200)
        self.assertEqual(p.capacite_epargne_mensuelle, 2250.0)

    def test_initialisation_sans_versement_utilisateur(self):
        p = Personne("Bob", 40, 60000, 1500, 1000, 70000, 5)
        self.assertIsNone(p.versement_mensuel_utilisateur)
        self.assertAlmostEqual(p.capacite_epargne_mensuelle, 2500.0)

    def test_calcul_capacite_epargne(self):
        p = Personne("Claire", 25, 36000, 800, 600, 20000, 3)
        self.assertAlmostEqual(p._calcul_capacite_epargne(), 1600.0)