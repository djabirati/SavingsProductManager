import unittest
from src.mon_module.core import calcul_interets_composes, suggestion_epargne
from src.mon_module.models.personne import Personne
from src.mon_module.models.epargne import Epargne


class TestFonctionsCore(unittest.TestCase):

    def test_calcul_interets_composes(self):
        montant = calcul_interets_composes(1200, 0.05, 3)
        self.assertAlmostEqual(montant, 3972.15, places=2)

    def test_suggestion_epargne_basique(self):
        personne = Personne("Test", 30, 36000, 1000, 500, 10000, 5)
        produit = Epargne("Livret", 0.02, 0.0, 0, None)

        resultats = suggestion_epargne(personne, [produit], 10000, 5)
        self.assertTrue(len(resultats) >= 1)
        self.assertTrue(any(isinstance(r.montant_net_final, float) for r in resultats))

    def test_suggestion_epargne_inadmissible(self):
        personne = Personne("Test", 30, 36000, 1000, 500, 10000, 1)
        produit = Epargne("Produit bloqué", 0.03, 0.0, 5, None)

        resultats = suggestion_epargne(personne, [produit], 10000, 1)
        self.assertEqual(resultats, [])
