import pandas as pd
import os
from src.mon_module.core import import_epargnes, import_personnes
from src.mon_module.models.epargne import Epargne
from src.mon_module.models.personne import Personne
from src.mon_module.utils import calcul_interets_composes


def main():
    """
    Fonction principale pour charger, nettoyer et afficher les données.

    chemin_fichier = os.path.join("data", "personnes.csv")

    try:
        df_original = pd.read_csv(chemin_fichier)
    except FileNotFoundError:
        print(f"ERREUR : Le fichier {chemin_fichier} n'a pas été trouvé. Vérifiez le chemin.")
        return

    print("---  DataFrame AVANT nettoyage ---")
    print(df_original.head())
    print("\n--- Types de données avant ---")
    print(df_original.dtypes)

    try:
        df_nettoye = nettoyer_donnees(df_original)

        print("\n\n---  DataFrame APRÈS nettoyage ---")
        print(df_nettoye.head())
        print("\n--- Types de données après ---")
        print(df_nettoye.dtypes)
    except ValueError as e:
        print(f"\nERREUR lors du nettoyage : {e}")
    """
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


if __name__ == "__main__":
    main()