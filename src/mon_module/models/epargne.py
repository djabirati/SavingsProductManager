from typing import Optional


class Epargne:
    def __init__(self, nom, taux_interet, fiscalite, duree_min, versement_max: Optional[float] = None):
        self.nom = nom
        self.taux_interet = taux_interet
        self.fiscalite = fiscalite
        self.duree_min = duree_min
        self.versement_max = versement_max

    def __repr__(self):
        return (f"Epargne(nom='{self.nom}', taux_interet={self.taux_interet}, "
                f"fiscalite={self.fiscalite}, duree_min={self.duree_min}, "
                f"versement_max={self.versement_max})")

    def __str__(self):
        montant_max = f"{self.versement_max:,.2f}€" if self.versement_max is not None else "Illimité"
        return (f" Produit d'épargne : {self.nom}\n"
                f"  Taux d'intérêt annuel : {self.taux_interet:.2f}%\n"
                f"  Taux de fiscalité : {self.fiscalite:.2f}%\n"
                f"  Durée minimale recommandée : {self.duree_min} ans\n"
                f"  Plafond de versement mensuel : {montant_max}")
