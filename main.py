import pandas as pd
import os
from src.mon_module.core import nettoyer_donnees
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
        df_nettoye.to_csv("data/cleaned_personne.csv", index=False)
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


if __name__ == "__main__":
    main()