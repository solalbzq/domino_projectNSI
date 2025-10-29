from domino import Domino
import random

class Jeu():
    def __init__(self):
        self.dominos = self.generer_jeu()
        random.shuffle(self.dominos)
        self.pioche = []
        self.joueurs = [[], []] 
        self.plateau = []

    def generer_jeu(self):
        """Génère un jeu complet de dominos (28 pièces) de façon récursive."""
        def rec(i, j):
            if i > 6:
                return []
            if j > 6:
                return rec(i + 1, i + 1)
            return [Domino(i, j)] + rec(i, j + 1)
        return rec(0, 0)
    
    def distribuer(self):
        """distribue 7 dominos à chaque joueur et place le reste dans la pioche. (pas besoin de. boucle ici car le nombre de joueurs est fixe à 2 et le paquet est melangé)"""
        self.joueurs[0] = self.dominos[:7]
        self.joueurs[1] = self.dominos[7:14]
        self.pioche = self.dominos[14:]
        
    def afficher_plateau(self):
        """Affiche le plateau de jeu."""
        s = ""
        for i in range(len(self.plateau)):
            if i:
                s += " "
            s += str(self.plateau[i])
        print(s)
        
    def afficher_main(self, joueur):
        print("Main du joueur :", end=" ")
        for i, d in enumerate(self.joueurs[joueur]):
            print(f"{i}: {d}", end="  ")
        print("\n")
        
    def jouer(self):
        """lance une partie de domino entre deux joueurs humains."""
        self.distribuer()
        joueur_actuel = 0
        
        premier_domino = self.pioche.pop()
        self.plateau.append(premier_domino)
        print(f"Le jeu commence avec {premier_domino}\n")
        
        while True:
            print(f"--- Tour du joueur {joueur_actuel + 1} ---")
            self.afficher_plateau()
            self.afficher_main(joueur_actuel)
            
            self.tour_joueur(joueur_actuel)

            # Vérifier victoire (peut etre a optimser on verra plus tard)
            if len(self.joueurs[joueur_actuel]) == 0:
                print(f"\nJoueur {joueur_actuel + 1} a gagné !")
            else:
                joueur_actuel = 1 - joueur_actuel
                
    def peut_poser(self, domino):
        """
        Vérifie si un domino peut être posé sur le plateau actuel.
        
        Étapes à réaliser :
        1. Si le plateau est vide → retourner True directement (tout domino est jouable).
        2. Sinon :
        - Récupérer la valeur gauche du premier domino du plateau (extrémité gauche).
        - Récupérer la valeur droite du dernier domino du plateau (extrémité droite).
        3. Vérifier si une des deux valeurs du domino correspond à l'une des extrémités :
        - Si oui → retourner True (le domino peut être joué).
        - Sinon → retourner False.
        """


    def poser_domino(self, joueur):
        """
        Permet au joueur de poser un domino sur le plateau.
        
        Étapes à réaliser :
        1. Demander au joueur l’indice du domino qu’il souhaite poser.
        - Vérifier que cet indice est valide (existe dans sa main).
        2. Récupérer le domino choisi.
        3. Si le plateau est vide :
        - Poser le domino directement (self.plateau.append(domino)).
        4. Sinon :
        - Vérifier si le domino peut être placé à gauche ou à droite :
            * Si domino.gauche correspond à la valeur droite du plateau → placer à droite.
            * Si domino.droite correspond à la valeur gauche du plateau → placer à gauche.
            * Si aucune correspondance → le domino ne peut pas être posé.
        - Si nécessaire, inverser le domino avant de le poser (domino.inverser()).
        5. Si le domino est posé :
        - Retirer ce domino de la main du joueur.
        - Afficher un message confirmant le coup.
        6. Sinon :
        - Afficher un message "Impossible de poser ce domino".
        - Le joueur devra piocher ou passer son tour.
        """


    def piocher(self, joueur):
        """
        Permet au joueur de piocher un domino dans la pioche.
        
        Étapes à réaliser :
        1. Vérifier si la pioche contient encore des dominos :
        - Si oui, retirer un domino (self.pioche.pop()).
        - L’ajouter à la main du joueur (self.joueurs[joueur].append(...)).
        - Afficher le domino pioché.
        2. Si la pioche est vide :
        - Afficher un message "La pioche est vide, vous ne pouvez plus piocher".
        """


    def tour_joueur(self, joueur):
        """
        Gère le déroulement complet du tour d’un joueur.
        
        Étapes à réaliser :
        1. Demander au joueur ce qu’il veut faire :
        - Poser un domino (entrer un indice)
        - Piocher (entrer 'p')
        2. Si le joueur choisit de poser :
        - Appeler poser_domino(joueur)
        3. Si le joueur choisit de piocher :
        - Appeler piocher(joueur)
        4. Si le joueur ne peut plus jouer et la pioche est vide :
        - Le tour passe automatiquement au joueur suivant.
        """