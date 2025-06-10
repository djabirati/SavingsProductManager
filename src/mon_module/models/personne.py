class Personne:
    def __init__(self, nom, age, revenu_annuel, loyer, depenses_mensuelles, objectif, duree_epargne, versements_mensuel):
        self.nom = nom
        self.age = age
        self.revenu_annuel = revenu_annuel
        self.loyer = loyer
        self.depenses_mensuelles = depenses_mensuelles
        self.objectif = objectif
        self.duree_epargne = duree_epargne
        self.versements_mensuel = versements_mensuel

    def __calcul_capacite_epargne(self) -> float:
        return (self.revenu_annuel / 12) - self.loyer - self.depenses_mensuelles

    def __str__(self):
        capacite = self.__calcul_capacite_epargne()
        return (f"Client: {self.nom}, {self.age} ans\n"
                f"Revenu annuel : {self.revenu_annuel:,.2f}€\n"
                f"Loyer mensuel : {self.loyer:,.2f}€\n"
                f"Dépenses mensuelles : {self.depenses_mensuelles:,.2f}€\n"
                f"Capacité d'épargne mensuelle : {capacite:,.2f}€\n"
                f"Objectif d'épargne : {self.objectif}€ sur {self.duree_epargne} mois\n"
                f"Versement mensuel prévu : {self.versements_mensuel or 'Non précisé'}")
