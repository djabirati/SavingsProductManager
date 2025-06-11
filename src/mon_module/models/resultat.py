import pandas as pd

class ResultatEpargne:

    def __init__(self,
                 nom_produit: str,
                 effort_mensuel: float,
                 montant_brut_final: float,
                 total_verse: float,
                 total_interets_bruts: float,
                 imposition_totale: float,
                 montant_net_final: float,
                 atteinte_objectif: bool):

        self.nom_produit = nom_produit
        self.effort_mensuel = effort_mensuel
        self.montant_brut_final = montant_brut_final
        self.total_verse = total_verse
        self.total_interets_bruts = total_interets_bruts
        self.imposition_totale = imposition_totale
        self.montant_net_final = montant_net_final
        self.atteinte_objectif = atteinte_objectif

    def afficher(self):

        statut_objectif = "✅ Atteint" if self.atteinte_objectif else "❌ Manqué"

        return(
            f"--- Simulation pour le produit : {self.nom_produit} ---\n"
            f"| Effort d'épargne mensuel : {self.effort_mensuel:,.2f} €\n"
            f"| Montant total versé      : {self.total_verse:,.2f} €\n"
            f"| Intérêts bruts générés   : {self.total_interets_bruts:,.2f} €\n"
            f"| Imposition sur les gains : {self.imposition_totale:,.2f} €\n"
            f"| Montant final NET        : {self.montant_net_final:,.2f} €\n"
            f"| Statut de l'objectif     : {statut_objectif}\n"
            f"--------------------------------------------------"
        )

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convertit l'objet en DataFrame pandas d'une seule ligne.
        """
        return pd.DataFrame([vars(self)])