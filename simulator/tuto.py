import pygame
import sys
from tools import main_path
import launch

BLACK = (0, 0, 0)
GRAY = (75, 75, 75)
WHITE = (255, 255, 255)
SOFT_WHITE = (240, 240, 240)
GREEN = (0, 255, 0)
GREEN_CUSTOM = (25, 200, 25)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLEU_STP = (2, 75, 85)
OR_STP = (251, 175, 0)
BLEU_FC = (0, 0, 25)


width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 600

# Initialisation des éléments pygame
pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior - Tutoriel")
pygame.display.set_icon(pygame.image.load(main_path+'images/logo.png'))

# définition des différentes polices
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 30)
moyfont = pygame.font.Font(None, 45)
grandfont = pygame.font.Font(None, 100)

# Message pour quitter
validquit = False

# Dictionnaires textes et images à afficher
donnees = {1 :  ["Bienvenue sur le tutoriel", "images/backmenu.jpg"],
           2 :  ["Acceder au menu principal", "images/ImagesTuto/menu.jpeg"],
           3 :  ["  Quitter l'application  ", "images/ImagesTuto/quit.jpeg"],
           4 :  ["     Mettre en pause     ", "images/ImagesTuto/pause.jpeg"],
           5 :  ["    Changer la vitesse   ", "images/ImagesTuto/vitesse.jpeg"],
           6 :  ["   Pour entrer une date  ", "images/ImagesTuto/entree.jpeg"],
           7 :  [" Pour suivre une planète ", "images/ImagesTuto/suivi.jpeg"],
           8 :  ["Accès signe astrologiques", "images/ImagesTuto/grego.jpeg"],
           9 :  ["Signe astrologiques Chinois", "images/ImagesTuto/chn.jpeg"],
           10 : ["  Acces phases lunaires  ", "images/ImagesTuto/lune.jpeg"]}


class ecran:

    def __init__(self) -> None:
        pass

    def affichage(self, appel):
        '''affiche les differentes étapes du tuto'''

        # affichage image de fond
        pygame.draw.rect(screen, OR_STP, ((0, 0), (1080, 600)))
        pygame.draw.rect(screen, BLEU_STP, ((5, 5), (1070, 590)))
        pygame.draw.rect(screen, OR_STP, ((25, 75), (1030, 500)))

        # image du tutoriel  --> bientot
        img = pygame.transform.scale(pygame.image.load(main_path + donnees[appel][1]), (1020, 490))
        screen.blit(img, (30, 80))

        # message en haut
        message = moyfont.render(donnees[appel][0] , 1, SOFT_WHITE)
        screen.blit(message, (370, 25))


    def bravo(self):
        '''affiche le message de fin du tuto'''

        # Fond
        pygame.draw.rect(screen, OR_STP, ((0, 0), (1080, 600)))
        pygame.draw.rect(screen, BLEU_STP, ((5, 5), (1070, 590)))

        # Texte
        message = grandfont.render("Merci d'avoir suivi" , 1, OR_STP)
        message2 = grandfont.render(" Merci le tutoriel " , 1, OR_STP)
        screen.blit(message, (240, 150))
        screen.blit(message2, (260, 300))

        # Affichage bouton quitter 
        quitter = moyfont.render("Quitter", 1, WHITE)
        pygame.draw.rect(screen, RED, ((465, 440), (140, 50)), 0, 10)
        screen.blit(quitter, (480, 450))



    def quitter(self):
        '''desine écran validation quitter'''

        # Dessine l'espace d'affichage
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
    appel = 1
   
    while True:

        # recupération coordonnées de la souris
        pos_souris = pygame.mouse.get_pos()  

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit() 

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    appel += 1
                    if appel == 11:
                        # Affichage du message de fin
                        HUD.bravo()
                    if appel == 12:
                        # Lance le menu principal
                        launch.main()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if validquit:
                    # vérifie si la souris est sur le boutton quitter et quitte le tuto si clique dans la zone"""
                    if pos_souris[0] > 465 and pos_souris[0] < 605 and pos_souris[1] > 440 and pos_souris[1] < 490:
                        launch.main()  # Lance le menu principal

                appel += 1

                if appel == 11:
                    # Affichage du message de fin
                    HUD.bravo()
                    validquit = True
                    
        # (Sinon) Affiche la slide suivante
        if appel <= 10:
            HUD.affichage(appel) # Affichage des élément 

        
        pygame.display.flip() # Affichage final
    

if __name__ == '__main__':
    main()