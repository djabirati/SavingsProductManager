from typing import Optional


class Personne:
    def __init__(self,
                 nom: str,
                 age: int,
                 revenu_annuel: float,
                 loyer: float,
                 depenses_mensuelles: float,
                 objectif: float,
                 duree_epargne: int,
                 versement_mensuel_utilisateur: Optional[float] = None):
        self.nom = nom
        self.age = age
        self.revenu_annuel = revenu_annuel
        self.loyer = loyer
        self.depenses_mensuelles = depenses_mensuelles
        self.objectif = objectif
        self.duree_epargne = duree_epargne
        self.versement_mensuel_utilisateur = versement_mensuel_utilisateur
        self.capacite_epargne_mensuelle = self._calcul_capacite_epargne()
    def _calcul_capacite_epargne(self) -> float:
        return (self.revenu_annuel / 12) - self.loyer - self.depenses_mensuelles

    def __str__(self) -> str:

        info_versement = (f"Versement utilisateur : {self.versement_mensuel_utilisateur:.2f} €/mois"
                          if self.versement_mensuel_utilisateur is not None
                          else "Versement utilisateur : non défini")
        return (
            f"--- Profil de {self.nom} ---\n"
            f"Âge : {self.age} ans\n"
            f"Revenu annuel net : {self.revenu_annuel:.2f} €\n"
            f"Objectif d'épargne : {self.objectif:.2f} € sur {self.duree_epargne} ans\n"
            f"---------------------------------\n"
            f"Capacité d'épargne calculée : {self.capacite_epargne_mensuelle:.2f} €/mois\n"
            f"{info_versement}"
        )
    def __repr__(self):
        capacite = self._calcul_capacite_epargne()
        return (f"Client: {self.nom}, {self.age} ans\n"
                f"Revenu annuel : {self.revenu_annuel:,.2f}€\n"
                f"Loyer mensuel : {self.loyer:,.2f}€\n"
                f"Dépenses mensuelles : {self.depenses_mensuelles:,.2f}€\n"
                f"Capacité d'épargne mensuelle : {capacite:,.2f}€\n"
                f"Objectif d'épargne : {self.objectif}€ sur {self.duree_epargne} mois\n"
                f"Versement mensuel prévu : {self.versement_mensuel_utilisateur or 'Non précisé'}")
