def calcul_interets_composes(versement_annuel: float, taux_annuel: float, duree_annees: int) -> float:
    capital_total = 0.0
    for _ in range(duree_annees):
        capital_total += versement_annuel
        capital_total *= (1 + taux_annuel)
    return capital_total