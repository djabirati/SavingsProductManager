import unittest
from src.mon_module.utils import calcul_interets_composes


class TestCalculInteretsComposes(unittest.TestCase):
    def test_cas_simple_et_positif(self):
        """
        Teste un scénario de base sur 2 ans pour vérifier le calcul.
        - Année 1: (0 + 1000) * 1.10 = 1100
        - Année 2: (1100 + 1000) * 1.10 = 2310
        """
        self.assertAlmostEqual(calcul_interets_composes(versement_annuel=1000, taux_annuel=0.10, duree_annees=2),
                               2310.0)

    def test_avec_versement_nul(self):
        """
        Teste que si le versement est de zéro, le capital reste à zéro.
        """
        self.assertEqual(calcul_interets_composes(versement_annuel=0, taux_annuel=0.10, duree_annees=10), 0.0)

    def test_avec_duree_nulle(self):
        """
        Teste que si la durée est de zéro an, aucun calcul n'est fait.
        """
        self.assertEqual(calcul_interets_composes(versement_annuel=1000, taux_annuel=0.10, duree_annees=0), 0.0)


if __name__ == '__main__':
    unittest.main()