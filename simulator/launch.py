import pygame
import sys
import interface
from tools import main_path

BLACK = (0, 0, 0)
GRAY = (75, 75, 75)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREEN_CUSTOM = (25, 200, 25)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLEU_STP = (2, 75, 85)
OR_STP = (251, 175, 0)
BLEU_FC = (0, 0, 25)

#test couleurs
#BLEU_STP(10, 50, 150)
#OR_STP = (175, 135, 0)

width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720
pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior - Menu")
pygame.display.set_icon(pygame.image.load(main_path+'images/logo.png'))
font = pygame.font.Font(None, 40)
grandfont = pygame.font.Font(None, 75)
validquit = False


class ecran:

    def __init__(self) -> None:
        pass

    def affichage(self):
        """affichage image de fond"""
        background = pygame.image.load(main_path+"images/backmenu.jpg")
        background = pygame.transform.scale(background, (1080, 640))
        screen.blit(background, (0, -20))

        """message bienvenue en haut"""
        welcome = grandfont.render("Bienvenue sur Spacior", 1, WHITE)
        screen.blit(welcome, (250, 100))

        """bouton lancement"""
        pygame.draw.rect(screen, OR_STP, ((210, 450),(150, 50)), 0, 10)
        play = font.render("START", 1, BLEU_STP)
        screen.blit(play, (240, 462))
        
        """bouton quitter"""
        pygame.draw.rect(screen, OR_STP, ((720, 450),(150, 50)), 0, 10)
        quitter = font.render("QUITTER", 1, BLEU_STP)
        screen.blit(quitter, (733, 462))

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
   
    while True:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            # if 

        HUD.affichage()
        """recupération coordonnées souris"""
        pos_souris = pygame.mouse.get_pos()

        """vérifie si souris sur le boton et lance appli si clique dans la zone"""
        if pos_souris[0] > 210 and pos_souris[0] < 360 and pos_souris[1] > 445 and pos_souris[1] < 502:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.time.wait(100)
                interface.main()
                
        
        """vérifie si souris sur le boton et quitte appli si clique dans la zone"""
        if pos_souris[0] > 720 and pos_souris[0] < 870 and pos_souris[1] > 445 and pos_souris[1] < 502:
            if event.type == pygame.MOUSEBUTTONDOWN:
                validquit = True
                

        if validquit == True:
            """permet d'afficher le message de confirmation pour quitter"""
            HUD.quitter()
            pos_souris = pygame.mouse.get_pos()
            if pos_souris[0] > 400 and pos_souris[0] < 500 and pos_souris[1] > 300 and pos_souris[1] < 350:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            elif pos_souris[0] > 600 and pos_souris[0] < 700 and pos_souris[1] > 300 and pos_souris[1] < 350:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    validquit = not validquit

        #création du fond
        # background = pygame.image.load(main_path+"images/backmenu.jpg")
        # background = pygame.transform.scale(background, (1080, 640))
        # screen.blit(background, (0, -20))
        pygame.display.flip()
    

if __name__ == '__main__':
    main()