class Domino:

    def __init__(self, gauche, droite):
        """
        Initialise un domino avec les valeurs gauche et droite.
        :param gauche: (int), valeur du coté gauche du domino
        :param droite: (int), valeur du coté droite du domino
        :cu: les valeurs doivent être des entiers de 0 à 6
        """
        assert isinstance(gauche, int),'La valeur de gauche doit être un entier'
        assert isinstance(droite, int),'La valeur de droite doit être un entier'
        assert 0 <= gauche <= 6 and 0 <= droite <= 6, 'Les valeurs doivent être entre 0 et 6 inclus'
        self.gauche = gauche
        self.droite = droite

    def retourner(self):
        """
        Inverse les deux côtés du domino
        """
        tmp = self.gauche
        self.gauche = self.droite
        self.droite = tmp

    def cote_est_vide(self, cote):
        """
        Vérifie si un côté du domino est vide (0).
        :param cote: (int) valeur d'un coté du dommino
        :cu: le côté doit être un entier entre 0 et 6
        :return:(int) renvoie soit une string vide pour l'affichage soit la valeur du coté du domino
        """
        assert isinstance(cote, int), "Le côté doit être un entier"
        assert 0 <= cote <= 6, "Le côté doit être entre 0 et 6"
        
        if cote == 0:
            res = " "
        else:
            res = cote    
        return res

    def valeur_totale(self):
        """
        Retourne la somme des deux côtés du domino.
        :return: (int), La somme des deux coté du domino.
        """
        return self.gauche + self.droite
    
    def est_double(self):
        """
        Retourne True si le domino est un double.
        :return: (bool), Le domino est un double ou non.
        """
        return self.gauche == self.droite

    def __str__(self):
        """
        Retourne une représentation du domino comme demandander dans le cahier des charges.
        :return: représentation graphique textuelle du domino.
        """
        
        if self.est_double():
            valeur = self.cote_est_vide(self.gauche)
            haut = f"|{valeur}|"
            bas = f"|{valeur}|"
            bordure = "-" * len(haut)
            res = f"{bordure}\n{haut}\n{bordure}\n{bas}\n{bordure}"
        else:
            valeur = f"| {self.cote_est_vide(self.gauche)} | {self.cote_est_vide(self.droite)} |"
            bordure = "-" * len(valeur)
            res = f"{bordure}\n{valeur}\n{bordure}"
        
        return res
    
    def __repr__(self):
        """
        Retourne une représentation du domino compacte par soucis d'affichage.
        :return: (str), représentation textuelle compacte du domino.
        """
        return f"[{self.gauche}|{self.droite}]"

    def __eq__(self, autre):
        """
        Vérifie si deux dominos sont équivalents, peu importe l’ordre
        :param autre: (Domino), autre domino à comparer
        :return: (bool), compare les deux dominos différents.
        """
        assert isinstance(autre, Domino), "La comparaison doit se faire avec un autre domino"
        return self.valeur_totale() == autre.valeur_totale()