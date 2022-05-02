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


width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720
pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior - Tutoriel")
pygame.display.set_icon(pygame.image.load(main_path+'images/logo.png'))
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 30)
moyfont = pygame.font.Font(None, 45)
grandfont = pygame.font.Font(None, 100)
validquit = False

donnees = {1 :  ["Bienvenue sur le tutoriel", "images/backmenu.jpg"],
           2 :  ["Acceder au menu principal", "images/ImageTuto/menu.JPEG"],
           3 :  ["  Quitter l'application  ", "images/ImageTuto/quit.jpeg"],
           4 :  ["     Mettre en pause     ", "images/TmageTuto/pause.jpeg"],
           5 :  ["    Changer la vitesse   ", "images/TmageTuto/pause.jpeg"],
           6 :  ["   Pour entrer une date  ", "images/ImageTuto/entree.jpeg"],
           7 :  [" Pour suivre une planète ", "images/TmageTuto/suivi.jpeg"],
           8 :  ["Accès signe astrologiques", "images/ImageTuto/grego.jpeg"],
           9 :  ["Signe astrologiques Chinois", "images/ImageTuto/chn.jpeg"],
           10 : ["  Acces phases lunaires  ", "images/ImageTuto/lune.jpeg"]}


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

        # # bouton quitter
        # pygame.draw.rect(screen, OR_STP, ((720, 450),(150, 50)), 0, 10)
        # quitter = font.render("QUITTER", 1, BLEU_STP)
        # screen.blit(quitter, (733, 462))

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

        """desine écran validation quitter"""
        pygame.draw.rect(screen, GRAY, ((340, 200),(400, 200)), 0, 5)
        pygame.draw.rect(screen, GREEN_CUSTOM, ((400, 300),(100, 50)), 0, 10)
        pygame.draw.rect(screen, RED, ((590, 300),(100, 50)), 0, 10)
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

        """recupération coordonnées souris"""
        pos_souris = pygame.mouse.get_pos()  

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit() 

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    appel += 1
                    if appel == 11:
                        HUD.bravo()
                    if appel == 12:
                        launch.main()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if validquit:
                    """vérifie si souris sur le boton quitter et quitte tuto si clique dans la zone"""
                    if pos_souris[0] > 465 and pos_souris[0] < 605 and pos_souris[1] > 440 and pos_souris[1] < 490:
                        launch.main()
                appel += 1
                if appel == 11:
                    HUD.bravo()
                    validquit = True
                    
            

        if appel <= 7:
            HUD.affichage(appel) # Affichage des élément 

        
        pygame.display.flip() # Affichage final
    

if __name__ == '__main__':
    main()