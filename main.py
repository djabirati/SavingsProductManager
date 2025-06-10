import pandas as pd
import os
from src.mon_module.core import nettoyer_donnees
def main():
    """
    Fonction principale pour charger, nettoyer et afficher les données.
    """
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


if __name__ == "__main__":
    main()