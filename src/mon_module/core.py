import pandas as pd
import numpy as np

def nettoyer_donnees(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie un DataFrame en traitant les valeurs manquantes et en convertissant
    les types de colonnes spécifiques.
    """
    df_propre = df.copy()
    df_propre.replace("None", np.nan, inplace=True)

    colonnes_float = ['versement_mensuel_utilisateur', 'objectif']
    colonnes_int = ['age', 'revenu_annuel', 'loyer', 'depenses_mensuelles', 'duree']

    try:
        for col in colonnes_float:
            df_propre[col] = pd.to_numeric(df_propre[col], errors='coerce')
        for col in colonnes_int:
            df_propre[col] = pd.to_numeric(df_propre[col], errors='coerce').astype('Int64')
    except KeyError as e:
        raise ValueError(f"Erreur de format : La colonne {e} est introuvable dans le fichier.")

    return df_propre