from multiprocessing.sharedctypes import Value
import kepler as kp
import pygame
import sys
from time import time


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
pygame.display.set_caption("Spacior")
pygame.display.set_icon(pygame.image.load('./simulator/images/logo.png'))
screen.fill(BLACK)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
jouer = False

#données palnètes

data = {'A' :['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j', 'température moyenne = 462°C', "simulator/images/mercure.png"],
                'B' : ['Venus','poids = 4,867 5x10^24 kg', 'rayon = 6050 km', 'distance soleil = 104 mm km', 'temps de rotation = 243 j', 'température moyenne = 440°C',"simulator/images/venus.png"],
                'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km', 'distance soleil = 150 mm km', 'temps de rotation = 365 j', 'température moyenne = 14°C',"simulator/images/terre.png"],
                'D' : ['Mars', 'poids = 6,418 x 10^23 kg','rayon = 3 396 km', 'distance soleil = 227 mm km', 'temps de rotation = 696 j', 'température moyenne = -60°C',"simulator/images/mars.png"],
                'E' : ['Jupyter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km', 'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j', 'température moyenne = -163°C',"simulator/images/jupyter.png"],
                'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km', 'distance soleil = 1,4 md km', 'temps de rotation = 29 ans et 167 j', 'température moyenne = -189°C',"simulator/images/saturne.png"],
                'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km','distance soleil = 2,8 md km', 'temps de rotation = 84 ans', 'température moyenne = -218°C',"simulator/images/uranus.png"],
                'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km', 'distance soleil = 4,5 md km', 'temps de rotation = 165 ans', 'température moyenne = -220°C',"simulator/images/neptune.png"]}




def update_time(temps: float, j: float, last_frame: float=time()) -> float:
    '''Permet d'avancer dans le temps'''
    new_frame = time() # Permet de faire avancer le temps non pas en fonction des FPS mais du temps réel
    return temps + (j/365.25)*(new_frame-last_frame), new_frame


class ecran():

    def __init__(self) -> None:
        # Paramètres du bouton pause
        self.bouton_pause_pos = (1015, 552) # Position du bouton pause
        self.bouton_pause_size = (50, 45) # Dimensions du bouton pause
        self.bouton_pause_images = { # Sprites du bouton pause
                                    "play": pygame.transform.scale(pygame.image.load("simulator/images/play.png"), self.bouton_pause_size),
                                    "pause": pygame.transform.scale(pygame.image.load("simulator/images/pause.png"), self.bouton_pause_size)}

    def espace_donnee(self) -> None:
        '''Dessine une zone pour photo planete et infos en dessous'''
        pygame.draw.rect(screen, BLEU_FC, ((800, 0), (1080, 275)))#photo planete
        pygame.draw.rect(screen, WHITE, ((800, 275), (1080, 600)))#affichage donnees

    def play_pause_date(self) -> None:
        pygame.draw.rect(screen, GRAY, ((800, 550), (1080, 600)))#barre date
        pygame.draw.rect(screen, OR_STP, ((1000, 550), (1080, 600)))#bouton play/pause
        
    def display_bouton_pause(self, jeu_en_marche: bool) -> None:
        '''Affichage du bouton pause dans son état "pause" ou "play"'''
        if jeu_en_marche:
            screen.blit(self.bouton_pause_images['play'], self.bouton_pause_pos)
        else:
            screen.blit(self.bouton_pause_images['pause'], self.bouton_pause_pos)

    def barre_action(self):
        '''Créer une barre sur la gauche pour ajouter boutons et actions'''
        # pygame.draw.rect(screen, OR_STP, ((44, 0), (45, 600)))
        pygame.draw.rect(screen, BLEU_STP, ((0, 0), (50, 600)))
        pygame.draw.rect(screen, OR_STP, ((0, 120), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 270), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 420), (50, 50)))
        
    def affichage_info(self) -> dict:
        '''pour retrouver les données associer a la planete dans le dico'''
        # Retourne sous forme de dico : {poids, rayon, distance au soleil, temps rotation soleil}
        for planete in data:
            if planete == data.key:
                return data.value
        
    def ecriture(self):
        '''Fait apparaitre les données de la planète choisie'''
        # Cherche dans le dictionnaire ==> (work in progress)
        dataget = data.get("F")
        # Récupérations des données + mise en forme
        text = font.render(dataget[0], 18, (0, 0, 0))
        poids = font.render(dataget[1], 1, (0, 0, 0))
        rayon = font.render(dataget[2], 1, (0, 0, 0))
        distance = font.render(dataget[3], 1, (0, 0, 0))
        rotation = font.render(dataget[4], 1, (0, 0, 0))
        temperature = font.render(dataget[5], 1, (0, 0, 0))
        # Affichage des données
        screen.blit(text, (900, 290))
        screen.blit(poids, (815, 350))
        screen.blit(rayon, (815, 375))
        screen.blit(distance, (815, 400))
        screen.blit(rotation, (815,425))
        screen.blit(temperature, (815,450))

        img = pygame.image.load(dataget[-1])
        img = pygame.transform.scale(img, (280, 275))
        screen.blit(img, (800, 0))
        pass




def main() -> None:
    
    HUD = ecran()
    data = False
    jouer = True
    

    sunpos = (int(width/2), int(height/2))

    moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)

    temps = 1
    vitesse = 30 # Jours par secondes
    frame_time = time() # Permet d'évaluer les fps de l'ordi afin d'adapter la vitesse
    
    while True:
        
        dt = clock.tick(144)
        #on creer un fond de couleur noir
        screen.fill(BLACK)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:

                # Affichage ou non des informations sur la planête
                if event.key == pygame.K_z:
                    data = not data

                # Pause ou marche
                if event.key == pygame.K_SPACE:
                    jouer = not jouer
                
                    
    
        if data == True:
            HUD.espace_donnee()
            HUD.ecriture()


        moon_pos = moon.calculate_point_from_time(temps)
        #mise en place des éléments de l'interface
        HUD.play_pause_date()
        HUD.barre_action()
        HUD.display_bouton_pause(jouer)

        # on fait apparaitre les différents astres 
        pygame.draw.circle(screen, WHITE, [int(moon_pos[0]), int(moon_pos[1])], 15) # Astre random sorti de mon imaginaire
        pygame.draw.circle(screen, YELLOW, sunpos, 30) # Soleil
        for point in moon.orbit_path :
            screen.set_at((int(point[0]), int(point[1])), WHITE)
    
        if jouer:
            temps, frame_time = update_time(temps, vitesse, frame_time) # Permet de finaliser l'acutalisation du temps
        else:
            temps, frame_time = update_time(temps, 0, frame_time) # Permet d'avoir un semblant de pause
        pygame.display.flip() # Affichage final

if __name__ == '__main__':
    main()