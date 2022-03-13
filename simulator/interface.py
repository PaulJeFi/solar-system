from multiprocessing.sharedctypes import Value
import kepler as kp
import pygame
import sys
from time import time
import donnesplanetes as data

BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#repère pour le dico des planetes (touche pas Paul)
mercure = 1
venus = 2 
terre = 3
mars = 4
jupyter = 5
saturne = 6
uranus = 7
neptune = 8

width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior")
pygame.display.set_icon(pygame.image.load('./simulator/images/logo.png'))
screen.fill(BLACK)
clock = pygame.time.Clock()

def update_time(temps, j, last_frame=time()):
    new_frame = time()
    return temps + (j/365.25)*(new_frame-last_frame), new_frame

class ecran():

    def espace_donnee(self):
        #dessine une zone pour photo planete et infos en dessous 
        pygame.draw.rect(screen, GRAY, 900, 0, 1080, 250)
        pygame.draw.rect(screen, WHITE, 900, 250, 1080, 600)
        pygame.display.flip()

    def barre_action(self):
        #creer une barre sur la gauche pour ajouter boutons et actions 
        pygame.draw.rect(screen, GRAY, 0, 0, 50, 600)
        pygame.draw.rect(screen, GRAY, 50, 0, 55, 600)
        pygame.display.flip()

    def affichage_info(self):
        #pour retrouver les donnees associer a la planete dans le dico
        #retourne sous forme de dico : {poids, rayon, distance au soleil, temps rotation soleil}
        for i in data:
            if i == data.key:
                donneesaafficher = data.value
        return donneesaafficher
        



def main():
    donnee = ecran.espace_donnee
    barre = ecran.barre_action
    sunpos = (int(width/2), int(height/2))

    moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)

    temps = 1
    vitesse = 365.25 / 2
    frame_time = time()
    
    while True:
        donnee()
        barre()
        dt = clock.tick(144)
        screen.fill(BLACK)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        moon_pos = moon.calculate_point_from_time(temps)

        pygame.draw.circle(screen, WHITE, [int(moon_pos[0]), int(moon_pos[1])], 15) # Soleil
        pygame.draw.circle(screen, YELLOW, sunpos, 30) # Soleil
        for point in moon.orbit_path :
            screen.set_at((int(point[0]), int(point[1])), WHITE)
    
        temps, frame_time = update_time(temps, vitesse, frame_time)
        
        pygame.display.flip()

if __name__ == '__main__':
    main()