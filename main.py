import pandas as pd
import os
from src.mon_module.core import import_epargnes, import_personnes, suggestion_epargne
from src.mon_module.models.epargne import Epargne
from src.mon_module.models.personne import Personne
from src.mon_module.utils import calcul_interets_composes


def main():
    personne_test = Personne(
        nom="Alice Dupont",
        age=30,
        revenu_annuel=45000.0,
        loyer=1100.0,
        depenses_mensuelles=800.0,
        objectif=50000.0,
        duree_epargne=8
    )

    livret_a = Epargne(
        nom="Livret A",
        taux_interet=0.03,
        fiscalite=0.0,
        duree_min=0,
        versement_max=22950.0
    )

    print(personne_test)
    print(livret_a)
    interet = calcul_interets_composes(1000, 0.10, 3)
    print(f"Montant calculé : {interet:.2f} €")

    fichier_personnes = 'src/mon_module/data/personnes.csv'
    fichier_epargnes = 'src/mon_module/data/epargnes.csv'
    liste_personnes = import_personnes(fichier_personnes)
    liste_epargnes = import_epargnes(fichier_epargnes)
    print("\n Personne importée:")
    for personne in liste_personnes:
        print(personne)
    print("\n Epargne importée:")
    for epargne in liste_epargnes:
        print(epargne)
    suggestions = suggestion_epargne(
        personne=personne_test,
        epargnes=liste_epargnes,
        objectif=personne_test.objectif,
        duree=personne_test.duree_epargne
    )
    for res in suggestions:
        print(res.afficher())

if __name__ == "__main__":
    main()