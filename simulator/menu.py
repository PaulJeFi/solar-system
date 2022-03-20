import pygame
import sys

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
pygame.display.set_icon(pygame.image.load('./simulator/images/logo.png'))
font = pygame.font.Font(None, 40)
grandfont = pygame.font.Font(None, 75)


class ecran:

    def __init__(self) -> None:
        pass

    def affichage(self):
        """affichage image de fond"""
        background = pygame.image.load("simulator/images/backmenu.jpg")
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

    def clique(self):
        pass

def main():

    HUD = ecran()
   
    while True:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            # if 

        HUD.affichage()

        #création du fond
        # background = pygame.image.load("simulator/images/backmenu.jpg")
        # background = pygame.transform.scale(background, (1080, 640))
        # screen.blit(background, (0, -20))
        pygame.display.flip()
    

if __name__ == '__main__':
    main()