import unittest
from src.mon_module.models.resultat import ResultatEpargne


class TestResultatEpargne(unittest.TestCase):

    def test_initialisation_et_affichage(self):
        r = ResultatEpargne(
            nom_produit="PEL",
            effort_mensuel=100.0,
            montant_brut_final=11000.0,
            total_verse=9600.0,
            total_interets_bruts=1400.0,
            imposition_totale=420.0,
            montant_net_final=10980.0,
            atteinte_objectif=False
        )

        self.assertEqual(r.nom_produit, "PEL")
        self.assertEqual(r.effort_mensuel, 100.0)
        self.assertEqual(r.montant_brut_final, 11000.0)
        self.assertEqual(r.total_verse, 9600.0)
        self.assertEqual(r.total_interets_bruts, 1400.0)
        self.assertEqual(r.imposition_totale, 420.0)
        self.assertEqual(r.montant_net_final, 10980.0)
        self.assertFalse(r.atteinte_objectif)

        texte = r.afficher()
        self.assertIn("PEL", texte)
        self.assertIn("100.00 €", texte)

    def test_conversion_dataframe(self):
        r = ResultatEpargne("Test", 50, 5000, 4800, 200, 60, 4940, True)
        df = r.to_dataframe()
        self.assertEqual(df.shape, (1, 8))
        self.assertEqual(df["nom_produit"][0], "Test")
