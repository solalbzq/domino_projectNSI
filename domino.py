class Domino:
    """
    Classe représentant une pièce de domino composée de deux valeurs entières
    """

    def __init__(self, gauche,droite):
        """Initialise un domino avec les valeurs gauche et droite."""
        assert isinstance(gauche, int),'La valeur de gauche doit être un entier'
        assert isinstance(droite, int),'La valeur de droite doit être un entier'
        assert 0 <= gauche <= 6 and 0 <= droite <= 6, 'Les valeurs doivent être entre 0 et 6 inclus'
        self.gauche = gauche
        self.droite = droite

    def retourner(self):
        """
        Inverse les deux côtés du domino
        """
        self.gauche, self.droite = self.droite, self.gauche

    def cote_est_vide(self, cote):
        """
        Vérifie si un côté du domino est vide (0).
        :param cote: (int)
        """
        if cote == 0:
            return " "
        else:
            return cote

    def __str__(self):
        """Retourne une représentation du domino complète comme sur l'affichage."""
        if self.est_double():
            valeur = self.cote_est_vide(self.gauche)
            haut = f"|{valeur}|"
            bas = f"|{valeur}|"
            bordure = "-" * len(haut)
            return f"{bordure}\n{haut}\n{bordure}\n{bas}\n{bordure}"
        else:
            valeur = f"| {self.cote_est_vide(self.gauche)} | {self.cote_est_vide(self.droite)} |"
            bordure = "-" * len(valeur)
            return f"{bordure}\n{valeur}\n{bordure}"
    
    def __repr__(self):
        """Retourne une représentation du domino compacte par soucis d'affichage."""
        return f"[{self.gauche}|{self.droite}]"

    def __eq__(self, autre):
        """
        Vérifie si deux dominos sont équivalents, peu importe l’ordre
        """
        if not isinstance(autre, Domino):
            return NotImplemented
        return ({self.gauche, self.droite} == {autre.gauche, autre.droite})

    def est_double(self):
        """Retourne True si le domino est un double (ex: [3|3])."""
        return self.gauche == self.droite

    def valeur_totale(self):
        """Retourne la somme des deux côtés du domino."""
        return self.gauche + self.droite