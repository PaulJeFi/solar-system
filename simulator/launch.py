import pygame
import sys
import interface
from tools import main_path
import tuto
import webbrowser
import os

BLACK = (0, 0, 0)
GRAY = (75, 75, 75)
WHITE = (255, 255, 255)
SOFT_WHITE = (240, 240, 240)
GREEN = (0, 255, 0)
GREEN_CUSTOM = (25, 200, 25)
GREEN_CUSTOM2 = (25, 150, 25)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLEU_STP = (2, 75, 85)
OR_STP = (251, 175, 0)
BLEU_FC = (0, 0, 25)


width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720

# Initialisation de pygame
pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior - Menu")
pygame.display.set_icon(pygame.image.load(main_path+'images/logo.png'))

# Initialisation des différentes polices 
font = pygame.font.Font(None, 40)
moyfont = pygame.font.Font(None, 50)
grandfont = pygame.font.Font(None, 75)

# Message pour quitter
validquit = False


class ecran:

    def __init__(self) -> None:
        pass

    def affichage(self):
        '''Affiche les éléments de l'interface'''

        # Affichage image de fond
        background = pygame.image.load(main_path+"images/backmenu.jpg")
        background = pygame.transform.scale(background, (1080, 640))
        screen.blit(background, (0, -20))

        # Message bienvenue en haut
        welcome = grandfont.render("Bienvenue sur Spacior", 1, WHITE)
        screen.blit(welcome, (250, 100))

        # Bouton lancement tutoriel
        pygame.draw.rect(screen, OR_STP, ((210, 450),(150, 50)), 0, 10)
        tuto = font.render("Tutoriel", 1, BLEU_STP)
        screen.blit(tuto, (230, 462))
        
        # Bouton de la base de donnée externe
        pygame.draw.rect(screen, OR_STP, ((720, 450),(150, 50)), 0, 10)
        ext = font.render("Galaxies", 1, BLEU_STP)
        screen.blit(ext, (733, 462))

        # Bouton lancement système
        pygame.draw.rect(screen, GREEN_CUSTOM2, ((460, 440),(170, 70)), 0, 10)
        start = moyfont.render("START", 1, SOFT_WHITE)
        screen.blit(start, (490, 460))

        # Bouton quitter
        pygame.draw.rect(screen, RED, ((470, 530),(150, 50)), 0, 10)
        quitter = font.render("QUITTER", 1, WHITE)
        screen.blit(quitter, (483, 542))
        


    def quitter(self):
        '''desine écran validation quitter'''

        # Dessine la zone
        pygame.draw.rect(screen, GRAY, ((340, 200),(400, 200)), 0, 5)
        pygame.draw.rect(screen, GREEN_CUSTOM, ((400, 300),(100, 50)), 0, 10)
        pygame.draw.rect(screen, RED, ((590, 300),(100, 50)), 0, 10)

        # Affichage du texte 
        sur = font.render("Sûr de vouloir quitter ?", 1, OR_STP)
        screen.blit(sur, (385, 220))
        quitter = font.render("Oui", 1, WHITE)
        screen.blit(quitter, (425, 312))
        non = font.render("Non", 1, WHITE)
        screen.blit(non, (615, 312))


def main():

    HUD = ecran()
    validquit = False
   
    while True:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit() 

            HUD.affichage() # Affichage des élément 

            # Recupération coordonnées souris
            pos_souris = pygame.mouse.get_pos()

            # Vérifie si souris sur le bouton et lance l'appli si clique dans la zone
            if pos_souris[0] > 210 and pos_souris[0] < 360 and pos_souris[1] > 445 and pos_souris[1] < 502:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.time.wait(100)
                    tuto.main()
                    
            
            # Vérifie si souris sur le bouton et affiche message pour quitte l'appli si clique dans la zone
            if pos_souris[0] > 470 and pos_souris[0] < 620 and pos_souris[1] > 530 and pos_souris[1] < 580:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    validquit = True

            # Vérifie souris pour le bouton de lancement
            if pos_souris[0] > 460 and pos_souris[0] < 630 and pos_souris[1] > 440 and pos_souris[1] < 510:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    interface.main()

            # Paul's Satan's tricks
            if pos_souris[0] > 720 and pos_souris[0] < 870 and pos_souris[1] > 445 and pos_souris[1] < 502:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    webbrowser.open('file://' + os.path.realpath('./simulator/templates/index.html'))
                    

            if validquit == True:
                # Permet d'afficher le message de confirmation pour quitter
                HUD.quitter()
                pos_souris = pygame.mouse.get_pos()

                # Pour quitter le programme ou revenir en arrière
                if pos_souris[0] > 400 and pos_souris[0] < 500 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit() # Quitte le programme
                        sys.exit()
                
                # Pour rester sur le programme et enlever le message à l'écran
                elif pos_souris[0] > 600 and pos_souris[0] < 700 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        validquit = not validquit # Enlève le message de confirmation 

        
        pygame.display.flip() # Affichage final
    

if __name__ == '__main__':
    main()