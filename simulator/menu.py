import pygame
import sys

BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLEU_STP = (2, 75, 85)
OR_STP = (211, 155, 0)
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
font = pygame.font.Font(None, 25)

#création du fond
screen.fill(WHITE)
background = pygame.image.load("simulator/images/backmenu.jpg")
background = pygame.transform.scale(background, (1080, 600))
screen.blit(background, (0, 0))

def main():

    #création du fond
    screen.fill(WHITE)
    background = pygame.image.load("simulator/images/backmenu.jpg")
    background = pygame.transform.scale(background, (1080, 640))
    screen.blit(background, (0, -20))
    pygame.display.flip()

    while True:

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

    

if __name__ == '__main__':
    main()