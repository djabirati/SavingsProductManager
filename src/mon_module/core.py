import pandas as pd
from typing import List
from .models.personne import Personne
from .models.epargne import Epargne


def import_personnes(fichier: str) -> List[Personne]:

    try:
        if fichier.endswith('.csv'):
            df = pd.read_csv(fichier)
        elif fichier.endswith('.xlsx'):
            df = pd.read_excel(fichier)
        else:
            df = pd.read_csv(fichier, sep='\t')

        personnes = []
        for _, row in df.iterrows():
            personnes.append(Personne(**row.to_dict()))

        print(f" {len(personnes)} personnes importées avec succès depuis '{fichier}'.")
        return personnes

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Une erreur est survenue lors de l'import des personnes : {e}")
        return []


def import_epargnes(fichier: str) -> List[Epargne]:

    try:
        na_vals = ["None", "null", ""]
        if fichier.endswith('.csv'):
            df = pd.read_csv(fichier, na_values=na_vals)
        elif fichier.endswith('.xlsx'):
            df = pd.read_excel(fichier, na_values=na_vals)
        else:
            df = pd.read_csv(fichier, sep='\t', na_values=na_vals)

        epargnes = []
        for _, row in df.iterrows():
            data = row.to_dict()
            if pd.isna(data.get('versement_max')):
                data['versement_max'] = None
            epargnes.append(Epargne(**data))

        print(f"{len(epargnes)} produits d'épargne importés avec succès depuis '{fichier}'.")
        return epargnes

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Une erreur est survenue lors de l'import des épargnes : {e}")
        return []