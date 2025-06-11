from datetime import datetime


def decorateur_suggestion(fonction):
    def wrapper(personne, epargnes, objectif, duree):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"\n[{date}] Nous allons faire une comparaison de {len(epargnes)} placements selon la situation de {personne.nom}.\n")
        return fonction(personne, epargnes, objectif, duree)
    return wrapper