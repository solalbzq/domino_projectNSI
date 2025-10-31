from domino import Domino
from functions import generateur_jeu
import random

class Jeu():
    def __init__(self):
        """
        Initialise un jeu de dominos avec deux joueurs, une pioche et un plateau de jeu.
        """
        self.dominos = self.generer_jeu()
        random.shuffle(self.dominos)
        self.pioche = []
        self.joueurs = [[], []] 
        self.plateau = []

    def generer_jeu(self):
        """
        Génère un jeu complet de dominos grâce à la fonction récursive.
        :return: (list), une liste de dominos représentant le jeu complet.
        """
        return generateur_jeu()
    
    def distribuer(self):
        """
        distribue 7 dominos à chaque joueur et place le reste dans la pioche. 
        (pas besoin de boucle ici car le nombre de joueurs est fixe à 2 et le paquet est dêja melangé)
        """
        self.joueurs[0] = self.dominos[:7]
        self.joueurs[1] = self.dominos[7:14]
        self.pioche = self.dominos[14:]
        
    def afficher_plateau(self):
        """
        Affiche le plateau de jeu de manière lisible.
        """
        print("Plateau :", end=" ")

        if not self.plateau:
            print("(vide)")
            return

        indice = 0
        while indice < len(self.plateau):
            domino_courant = self.plateau[indice]
            print(repr(domino_courant), end="")
            indice += 1
        
    def afficher_main(self, joueur):
        """
        Affiche la main du joueur spécifié.
        :param joueur: (int) le numéro du joueur dont on veut afficher la main
        :cu: joueur doit être 0 ou 1
        """
        assert joueur in (0, 1), "Le joueur doit être 0 ou 1"

        print(f"\n\n====== Main du Joueur {joueur + 1} ======\n")

        main_du_joueur = self.joueurs[joueur]
        if not main_du_joueur:
            print("(Aucun domino dans la main)\n")
            return

        dominos_affiches = []
        indice = 0
        while indice < len(main_du_joueur):
            domino_courant = main_du_joueur[indice]
            texte_domino = f"[{indice}] {repr(domino_courant)}"
            dominos_affiches.append(texte_domino)
            indice += 1

        print(" | ".join(dominos_affiches))
        print("\n")
        
    def verifier_victoire(self):
        """
        Vérifie si un joueur a gagné la partie.
        :return: (int or None), le numéro du joueur gagnant (0 ou 1) ou None si personne n'a gagné.
        """
        if len(self.joueurs[joueur_actuel]) == 0:
            print(f"\nJoueur {joueur_actuel + 1} a gagné !")
        else:
            joueur_actuel = 1 - joueur_actuel
        print("\n" + "#" * 50 + "\n")
        
    def jouer(self):
        """
        Lance une partie de domino entre deux joueurs humains.
        """
        self.distribuer()
        joueur_actuel = 0

        premier_domino = self.pioche.pop()
        self.plateau.append(premier_domino)
        print(f"Le jeu commence avec le domino suivant : {repr(premier_domino)}\n")

        while True:
            self.afficher_plateau()
            self.afficher_main(joueur_actuel)
            self.tour_joueur(joueur_actuel)

            # On vérifie si le joueur actuel a gagné après son tour
            if self.verifier_victoire(joueur_actuel):
                print(f"\n🎉 Joueur {joueur_actuel + 1} a gagné la partie ! 🎉")
                break

            # Changement de joueur
            joueur_actuel = 1 - joueur_actuel
            print("\n" + "#" * 50 + "\n")


    def verifier_victoire(self, numero_joueur):
        """
        Vérifie si le joueur spécifié a gagné la partie.

        :param numero_joueur: (int) Numéro du joueur (0 ou 1)
        :return: (bool) True si le joueur n’a plus de dominos, sinon False
        """
        main_joueur = self.joueurs[numero_joueur]
        return len(main_joueur) == 0
                
                
    def peut_poser(self, domino):
        """
        Vérifie si un domino peut être posé sur le plateau actuel.
        :param domino: (Domino), le domino à vérifier
        :return: (bool), True si le domino peut être posé, False sinon.
        """
        assert isinstance(domino, Domino), "L'objet doit être un domino"
        
        if not self.plateau:
            return True
        
        gauche_plateau = self.plateau[0].gauche
        droite_plateau = self.plateau[-1].droite
        
        return domino.gauche == gauche_plateau or domino.droite == gauche_plateau or domino.gauche == droite_plateau or domino.droite == droite_plateau


    def poser_domino(self, joueur, domino_index):
        """
        Permet au joueur de poser un domino sur le plateau en vérifiant où il peut le poser.
        """
        assert joueur in (0, 1), "Le joueur doit être 0 ou 1"
        assert isinstance(domino_index, int), "L'indice du domino doit être un entier"

        if domino_index < 0 or domino_index >= len(self.joueurs[joueur]):
            print("Indice invalide.")
            return

        domino_choisi = self.joueurs[joueur][domino_index]

        if not self.plateau:
            self.plateau.append(domino_choisi)
            self.joueurs[joueur].pop(domino_index)
            print(f"Domino {domino_choisi} posé sur le plateau.")
            return

        gauche_plateau = self.plateau[0].gauche
        droite_plateau = self.plateau[-1].droite

        peut_gauche = domino_choisi.gauche == gauche_plateau or domino_choisi.droite == gauche_plateau
        peut_droite = domino_choisi.gauche == droite_plateau or domino_choisi.droite == droite_plateau

        if peut_gauche and not peut_droite:
            print("Ce domino ne peut être joué qu’à gauche")
            if domino_choisi.droite != gauche_plateau:
                domino_choisi.retourner()
            self.plateau.insert(0, domino_choisi)

        elif peut_droite and not peut_gauche:
            print("Ce domino ne peut être joué qu’à droite")
            if domino_choisi.gauche != droite_plateau:
                domino_choisi.retourner()
            self.plateau.append(domino_choisi)

        elif peut_gauche and peut_droite:
            print("Ce domino peut être joué des deux côtés, on le place à droite par défaut.")
            if domino_choisi.gauche != droite_plateau:
                domino_choisi.retourner()
            self.plateau.append(domino_choisi)

        else:
            print("Impossible de poser ce domino sur le plateau.")
            return

        self.joueurs[joueur].pop(domino_index)

    def piocher(self, joueur):
        """
        Permet au joueur de piocher un domino dans la pioche.
        :param joueur: (int), le joueur qui pioche
        :cu: joueur doit être 0 ou 1
        """
        assert joueur in (0, 1), "Le joueur doit être 0 ou 1"
        for d in self.pioche:
            assert isinstance(d, Domino), "La pioche doit contenir des dominos"
            
        if self.pioche:
            domino_pioche = self.pioche.pop()
            self.joueurs[joueur].append(domino_pioche)
            print(f"Vous avez pioché le domino : {repr(domino_pioche)}")
        else:
            print("La pioche est vide, vous ne pouvez plus piocher.")


    def tour_joueur(self, joueur):
        """
        Gère le déroulement complet du tour d’un joueur.
        :param joueur: (int), le joueur dont c'est le tour
        :cu: joueur doit être 0 ou 1
        """
        assert joueur in (0, 1), "Le joueur doit être 0 ou 1"
        for d in self.joueurs[joueur]:
            assert isinstance(d, Domino), "La main du joueur doit contenir des dominos"
            
        while True:
            action = input("Que voulez-vous faire ? (poser un domino: entrer l'indice, piocher: 'p') : ")
            
            if action.lower() == 'p':
                self.piocher(joueur)
                break
            else:
                if self.peut_poser(self.joueurs[joueur][int(action)]):
                    self.poser_domino(joueur, int(action))
                    break
                else:
                    print("Vous ne pouvez pas poser ce domino. Choisissez une autre action.")