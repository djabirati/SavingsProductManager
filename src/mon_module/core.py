import pandas as pd
from typing import List
from .models.personne import Personne
from .models.epargne import Epargne
from .models.resultat import ResultatEpargne
from .utils import calcul_interets_composes


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

def suggestion_epargne(personne: Personne,
                       epargnes: List[Epargne],
                       objectif: float,
                       duree: int) -> List['ResultatEpargne']:

    """

    Pour chaque produit :
    Si durée OK :
        Pour chaque effort :
            Si plafond OK :
                Calculs :
                    - capital_brut
                    - intérêts
                    - fiscalité
                    - capital_net
                Résultat → ajouté à la liste

    """
    scenarios = []
    efforts = []
    if personne.versement_mensuel_utilisateur is not None:
        efforts.append(personne.versement_mensuel_utilisateur)

    capacite = personne.capacite_epargne_mensuelle
    efforts += [round(capacite * ratio, 2) for ratio in [0.25, 0.50, 0.75, 1.0]]

    for epargne in epargnes:
        if duree < epargne.duree_min:
            continue

        for effort_mensuel in efforts:
            montant_total = effort_mensuel * 12 * duree

            if epargne.versement_max is not None and montant_total > epargne.versement_max:
                continue

            versement_annuel = effort_mensuel * 12
            capital_brut = calcul_interets_composes(versement_annuel, epargne.taux_interet, duree)

            interets = capital_brut - montant_total
            interets_net = interets * (1 - epargne.fiscalite)
            capital_net = montant_total + interets_net

            scenarios.append(ResultatEpargne(
                nom_produit=epargne.nom,
                effort_mensuel=effort_mensuel,
                montant_brut_final=capital_brut,
                total_verse=montant_total,
                total_interets_bruts=interets,
                imposition_totale=interets - interets_net,
                montant_net_final=capital_net,
                atteinte_objectif=capital_net >= objectif
            ))
    print(f"\n[DEBUG] Efforts testés : {efforts}")
    return scenarios