from domino import Domino

def generateur_jeu(valeur_gauche=0, valeur_droite=0):
    """
    Génère un jeu complet de dominos (28 pièces) de façon récursive.
    :param valeur_gauche: (int), la valeur gauche actuelle à traiter
    :param valeur_droite: (int), la valeur droite actuelle à traiter
    :return: (list), une liste de dominos représentant le jeu complet.
    """
    
    if valeur_gauche > 6:
        return []
    if valeur_droite > 6:
        return generateur_jeu(valeur_gauche + 1, valeur_gauche + 1)

    return [Domino(valeur_gauche, valeur_droite)] + generateur_jeu(valeur_gauche, valeur_droite + 1)