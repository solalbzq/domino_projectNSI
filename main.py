from domino import Domino
from jeu import Jeu
import pyfiglet

while True:
    titre = pyfiglet.figlet_format("DOMINO", font="banner3-D")
    print(titre)
    print("By Solal, Jeremi et Quentin".center(60, " "))
    print("\nBienvenue dans le jeu de Domino !\n")
    jeu = Jeu()
    jeu.distribuer()
    jeu.jouer()
    
    rejouer = input("Voulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() != 'o':
        print("Merci d'avoir joué ! Au revoir.")
        break