from cmath import phase
import math
import math
from os import times, walk
import kepler as kp
import pygame
import sys
from time import time, gmtime
import launch
import Temps
import pygame.mixer
import random
from tools import main_path, Tuple, List
import random
from PIL import Image



BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
DARK_GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
SOFT_WHITE = (200, 200, 200)
GREEN = (0, 255, 0)
GREEN_CUSTOM2 = (25, 150, 25)
GREEN_CUSTOM = (25, 200, 25)
MARRON = (179, 139, 109)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLEU_STP = (2, 75, 85)
OR_STP = (211, 155, 0)
BLEU_FC = (0, 0, 25)
ORANGE = (255, 127, 0)

luneSur100 = 29.53 / 100

width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720
pygame.init()
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior")
pygame.display.set_icon(pygame.image.load(main_path+'images/logo.png'))
screen.fill(BLACK)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 30)
moyfont = pygame.font.Font(None, 40)
grandfont = pygame.font.Font(None, 60)
# pygame.mixer.music.load(main_path+"musique/musique.mp3")
jouer = False

# Données planètes

data = {'A' : ['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 
              'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j',
              'température moyenne = 462°C', "images/mercure.png"],
        'B' : ['Venus', 'poids = 4,867 5x10^24 kg', 'rayon = 6050 km',
              'distance soleil = 104 mm km', 'temps de rotation = 243 j',
              'température moyenne = 440°C', "images/venus.png"],
        'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km',
              'distance soleil = 150 mm km', 'temps de rotation = 365 j',
              'température moyenne = 14°C', "images/terre.png"],
        'D' : ['Mars', 'poids = 6,418 x 10^23 kg', 'rayon = 3 396 km',
              'distance soleil = 227 mm km', 'temps de rotation = 696 j',
              'température moyenne = -60°C', "images/mars.png"],
        'E' : ['Jupiter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km',
              'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j',
              'température moyenne = -163°C', "images/jupyter.png"],
        'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km',
              'distance soleil = 1,4 md km', 'temps de rotation = 29 ans 167 j',
              'température moyenne = -189°C', "images/saturne.png"],
        'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km',
              'distance soleil = 2,8 md km', 'temps de rotation = 84 ans',
              'température moyenne = -218°C', "images/uranus.png"],
        'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km',
              'distance soleil = 4,5 md km', 'temps de rotation = 165 ans',
              'température moyenne = -220°C', "images/neptune.png"],
        'I' : ['Pluton', 'poids = 1,3 X 10^22 kg', 'rayon = 1185 km',
              'distance soleil = 6 md km', 'temps de rotation = 248 ans',
              'température moyenne = -225°C', "images/pluton.png"],
        'Z' : ['', '', '', '', '', '', '']}

# On charge les images (démarage plus long, mais permet au programme d'être ensuite beaucoup plus fluide)
for key in list(data.keys())[:-1]: # Le "[:-1]" permet de ne pas charger la dernière planête car elle n'est pas encore définie
    data[key][-1] = pygame.transform.scale(pygame.image.load(str(main_path+data[key][-1])), (280, 275))

# Données signes astrologiques

signes = {'A': ["  Bélier  ", "21 Mars - 20 Avril",        "Élément : Feu"],
          'B': ["  Taureau ", "21 Avril - 21 Mai",         "Élément : Terre"],
          'C': ["  Gémaux  ", "22 Mai- 21 Juin",           "Élément : Air"],
          'D': ["  Cancer  ", "22 Juin - 22 Juillet",      "Élément : Eau"],
          'E': ["    Lion  ", "23 Juillet - 22 Août",      "Élément : Feu"],
          'F': ["  Vierge  ", "23 Août - 22 Septembre",    "Élément : Terre"],
          'G': ["  Balance ", "23 Septembre - 22 Octobre", "Élément : Air"],
          'H': [" Scorpion ", "23 Octobre - 22 Novembre",  "Élément : Feu"],
          'I': ["Sagittaire", "23 Novembre - 21 Décembre", "Élément : Feu"],
          'J': ["Capricorne", "22 Décembre - 20 Janvier",  "Élément : Terre"],
          'K': ["  Verseau ", "21 Janvier - 18 Février",   "Élément : Air"],
          'L': ["  Poisson ", "19 Février - 20 Mars",      "Élément : Eau"],
          'M': ["  Dragon  ", "Dernière Année : 2012",     "Prochaine : 2024"],
          'N': ["  serpent ", "Dernière Année : 2013",     "Prochaine : 2025"],
          'O': ["  Cheval  ", "Dernière Année : 2014",     "Prochaine : 2026"],
          'P': ["  Mouton  ", "Dernière Année : 2015",     "Prochaine : 2027"],
          'Q': ["   Singe  ", "Dernière Année : 2016",     "Prochaine : 2028"],
          'R': ["    Coq   ", "Dernière Année : 2017",     "Prochaine : 2029"],
          'S': ["   Chien  ", "Dernière Année : 2018",     "Prochaine : 2030"],
          'T': ["  Cochon  ", "Dernière Année : 2019",     "Prochaine : 2031"],
          'U': ["    Rat   ", "Dernière Année : 2020",     "Prochaine : 2032"],
          'V': ["   Boeuf  ", "Dernière Année : 2021",     "Prochaine : 2033"],
          'W': ["   Tigre  ", "Dernière Année : 2022",     "Prochaine : 2034"],
          'X': ["  Lièvre  ", "Dernière Année : 2023",     "Prochaine : 2035"]}


def extract_gif(gif_path: str) -> List(pygame.Surface):
    '''Permet de séparer un GIF en une liste d'images'''
    
    gif = Image.open(gif_path) # On ouvre le GIF
    images = [] # On créer une liste vide
    
    # On parcourt les frames du GIF
    for i in range(gif.n_frames):
        gif.seek(i) # On cherche la frame actuelle
        image = gif.copy() # On la copie
        
        # On garde en mémoire ses informations
        mode = image.mode
        size = image.size
        data = image.tobytes()
        
        # On la convertie en image pygame
        py_image = pygame.image.fromstring(data, size, mode)
        
        # On ajoute cette nouvelle image à notre liste
        images.append(py_image)
    
    return images # On retourne la liste d'images


def load_folder(folder_path: str) -> List(pygame.Surface):
    '''Permet de charger l'ensemble des images contenues dans un dossier'''

    images = [] # On créer une liste vide

    # On parcours le dossier
    for filename in next(walk(folder_path), (None, None, []))[2]:

        # On charge l'image
        images.append(pygame.image.load(str(folder_path + filename)))
    
    return images # On retourne la liste d'images
        


# IMAGES_LUNE = extract_gif(str(main_path + "images/gif_lune/lune.gif"))[1:]
IMAGES_LUNE = load_folder(str(main_path + "images/lune/"))


def update_time(temps: float, j: float, last_frame: float=time()) -> float:
    '''Permet d'avancer dans le temps'''
    new_frame = time() # Permet de faire avancer le temps non pas en fonction
                       # des FPS mais du temps réel
    true_speed = j*(new_frame-last_frame)
    return temps + true_speed, true_speed, new_frame


class ecran():

    def __init__(self) -> None:
        # Paramètres du bouton pause
        self.bouton_pause_pos  = (915, 503) # Position du bouton pause
        self.bouton_pause_size = ( 45,  43) # Dimensions du bouton pause
        self.bouton_pause_images = { # Sprites du bouton pause
                                    "play": pygame.transform.scale(pygame.image.load(main_path+"images/play.png"), self.bouton_pause_size),
                                    "pause": pygame.transform.scale(pygame.image.load(main_path+"images/pause.png"), self.bouton_pause_size)}
        # Paramètres des boutons de vitesse de lecture
        self.bouton_vitesse_lecture_pos = (820, 502)
        self.bouton_vitesse_lecture_size = (45, 45 )
        self.bouton_vitesse_lecture2_pos = (1012, 503)
        self.bouton_vitesse_lecture_image = {"normal": pygame.transform.scale(pygame.image.load(main_path+"images/vitesselecture.png"), self.bouton_vitesse_lecture_size),
                                             "rapide": pygame.transform.scale(pygame.image.load(main_path+"images/vitessecours.png"), self.bouton_vitesse_lecture_size),
                                             "lent": pygame.transform.scale(pygame.image.load(main_path+"images/vitesselecture.png"), self.bouton_vitesse_lecture_size),
                                             "normal2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load(main_path+"images/vitesselecture.png"), 180), self.bouton_vitesse_lecture_size),
                                             "rapide2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load(main_path+"images/vitesselecture.png"), 180), self.bouton_vitesse_lecture_size),
                                             "lent2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load(main_path+"images/vitessecours.png"), 180), self.bouton_vitesse_lecture_size)}
        # Paramètres du slider pour le zoom
        self.zoom_slider_pos = (515, 553) # Position du background du slider (le boutton est placé en conséquance)
        self.zoom_slider_size_factor = 2.35 # Facteur de taille
        ''' Le sprite à été remplacé par un assemblage de rectangles en utilisant pygame.draw.rect()
        self.zoom_slider_size = { # Les tailles des éléments (ne pas toucher ces valeurs, modifiez celle au-dessus)
                                'background': (120*self.zoom_slider_size_factor, 20*self.zoom_slider_size_factor),
                                'button': (4*self.zoom_slider_size_factor, 10*self.zoom_slider_size_factor)}
        self.zoom_slider_images = { # Les images utilisées pour le slider
                                    'background': pygame.transform.scale(pygame.image.load(main_path+"images/zoom_slider_bg.png"), self.zoom_slider_size['background']),
                                    'button': pygame.transform.scale(pygame.image.load(main_path+"images/zoom_slider_button.png"), self.zoom_slider_size['button'])}
        '''
        self.zoom_slider_x_range = (self.zoom_slider_pos[0]+18*self.zoom_slider_size_factor, self.zoom_slider_pos[0]+98*self.zoom_slider_size_factor) # Entre quelles coordonnées y le bouton slider peut se situer
        self.zoom_slider_current_x_pos = (self.zoom_slider_x_range[0]+self.zoom_slider_x_range[1])/2 # Possition x actuelle du bouton du slider
        self.zoom_slider_clicked = False # Permet de savoir si le curseur "tient" le bouton pour le faire slider
        self.zoom_factor = 1 # Facteur de zoom de la simulation
        self.wallE_x = 1080 #position x wall-E
        self.wallE_y = 25 #position y wall-E
        self.wallE_rotation  = 4 #rotation wall-E

    def espace_donnee(self) -> None:
        '''Dessine une zone pour photo planete et infos en dessous'''
        # Photo de la planète
        pygame.draw.rect(screen, BLEU_FC,  ((800,   0), (1080, 275)))
        # Affichage des données
        pygame.draw.rect(screen, WHITE,    ((800, 275), (1080, 600)))
        # Lignes de séparation
        pygame.draw.line(screen, OR_STP,    (800, 276), (1080, 276), 3)
        pygame.draw.line(screen, OR_STP,    (800, 498), (1080, 498), 3)
        pygame.draw.line(screen, OR_STP,    (798,   0), ( 798, 600), 3)
        pygame.draw.line(screen, OR_STP,    (798, 495), ( 1080, 495), 3)

    def play_pause_date(self) -> None:
        '''Dessine la zone pour entrer la date '''
        # Barre pour la date
        pygame.draw.rect(screen, GRAY,     ((800, 550), (1080, 600)))
        # Bouton pour valider la date
        pygame.draw.rect(screen, OR_STP,   ((990, 550), (  90, 600)))
        # Lignes de séparation (x4)
        pygame.draw.line(screen, WHITE,     (513, 551), (1080, 551), 3)
        pygame.draw.line(screen, WHITE,     (513, 550), ( 513, 600), 3)
        pygame.draw.line(screen, WHITE,     (798, 550), ( 798, 600), 3)
        pygame.draw.line(screen, WHITE,     (991, 550), ( 991, 600), 3)
        pygame.draw.line(screen, WHITE,     (800, 498), (1080, 498), 3)
        pygame.draw.line(screen, WHITE,     (798, 497), ( 798, 550), 3)
        # Barre de contrôle du temps
        pygame.draw.rect(screen, BLEU_STP, ((800, 500), ( 280,  50)))
        # Bouton sens inverse
        pygame.draw.rect(screen, GRAY,     ((800, 500), (  90,  50)))
        # Bouton pour la vitesse
        pygame.draw.rect(screen, GRAY,     ((990, 500), ( 280,  50)))
        # Bouton OK pour l'imput de date
        screen.blit(grandfont.render("OK", 1, BLACK), (1003, 558))
        
    def display_bouton_pause(cls, jeu_en_marche: bool) -> None:
        '''Affichage du bouton pause dans son état "pause" ou "play"'''
        # cls : comme self (utilisé dans d'autres langages comme JS, C#, ...)
        # Son utilisation n'est pas très "Pythonnesque", mais c'est pour la
        # limite des 80 caractères pas lignes ... (la bonne cause)
        if jeu_en_marche:
            screen.blit(cls.bouton_pause_images['play'],  cls.bouton_pause_pos)
        else:
            screen.blit(cls.bouton_pause_images['pause'], cls.bouton_pause_pos)

    def vitesse_lecture(self, vitesse: int) -> None:
        '''Affiche l'icone si la lecture rapide/lente est en cours'''
        if vitesse > 30:
            screen.blit(self.bouton_vitesse_lecture_image["rapide"],
                        self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["rapide2"],
                        self.bouton_vitesse_lecture_pos)
        elif vitesse == 30:
            screen.blit(self.bouton_vitesse_lecture_image["normal"],
                        self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["normal2"],
                        self.bouton_vitesse_lecture_pos)
        elif vitesse < 30:
            screen.blit(self.bouton_vitesse_lecture_image["lent"],
                        self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["lent2"],
                        self.bouton_vitesse_lecture_pos)
        
    def zoom_slider(self) -> None:
        '''Affichage et gestion du slider de zoom. Permet d'avoir le facteur de
           zoom actuel'''

        # Partie "click and drag"
        mouse = pygame.mouse.get_pos() # On récupère la position de la souris
        # Si l'utilisateur clique sur le petit bouton du slider : (désolé pour 
        # la longueur) <------------- TKT, tu vas voir du beau code conditionnel
        # Ci-dessous, la version du code où il faut précisément cliquer sur le 
        # bouton pour le sélectionner
        # if pygame.mouse.get_pressed()[0] and self.zoom_slider_current_x_pos <= mouse[0] <= self.zoom_slider_current_x_pos+4*self.zoom_slider_size_factor and self.zoom_slider_pos[1]+5*self.zoom_slider_size_factor <= mouse[1] <= self.zoom_slider_pos[1]+15*self.zoom_slider_size_factor and not self.zoom_slider_clicked:
        # Ci-dessous, la version du code où il faut cliquer n'importe où sur la 
        # barre sur laquelle le bouton coulisse
        me = self
        tool1 = lambda x, y : me.zoom_slider_pos[y]+x*me.zoom_slider_size_factor
        cond1 = pygame.mouse.get_pressed()[0]
        cond2 = tool1(20, 0) <= mouse[0] <= tool1(100, 0)
        cond3 = tool1(4, 1) <= mouse[1] <= tool1(16, 1)
        if cond1 and cond2 and cond3 and not self.zoom_slider_clicked:
            self.zoom_slider_clicked = True
        # Si l'utilisateur arrète de cliquer (donc "lache" le bouton) :
        elif not pygame.mouse.get_pressed()[0]:
            self.zoom_slider_clicked = False
        # PS : pygame.mouse.get_pressed() = Bouton de la souris pressés ? ->
        #            (LMB, MMB, RMB) avec dans chacun des emplacement un boolean

        '''Partie déplacement'''
        # Ajustement automatique
        mouse_x = mouse[0] - self.zoom_slider_size_factor*2
        if self.zoom_slider_clicked:
            # Le bouton doit rester dans les limites du slider
            if mouse_x < self.zoom_slider_x_range[0]: # Limite gauche
                self.zoom_slider_current_x_pos = self.zoom_slider_x_range[0]
            elif mouse_x > self.zoom_slider_x_range[1]: # Limite droite
                self.zoom_slider_current_x_pos = self.zoom_slider_x_range[1]
            else: # Cas où le bouton est bien entre les limites
                self.zoom_slider_current_x_pos = mouse_x
        
        '''Partie affichage'''
        #screen.blit(self.zoom_slider_images['background'], self.zoom_slider_pos)
        #screen.blit(self.zoom_slider_images['button'], (self.zoom_slider_current_x_pos, self.zoom_slider_pos[1] + 5*self.zoom_slider_size_factor))
        self.display_zoom_slider()
        # Ci-dessus, affichage de l'arrière plan du slider, puis du bouton pour le slider

        '''Partie utilitaire'''
        # Le facteur de zoom va de 1x à 64x (soit de 0.005 (min) à 0.32 (max))
        # En détail :
        #   0.005 est le facteur minimum (1x avec x = 0.005)
        #   6 est la puissance de 2 maximale par laquelle on peut multiplier le facteur minimum (2**6x <=> 64x)
        #   L'équation au milieu donne un résultat compris entre 1 et 2
        # Au final, on a :
        #   self.zoom_factor = facteur minimum * (équation ** puissance)
        self.zoom_factor = 0.005*((self.zoom_slider_current_x_pos-self.zoom_slider_x_range[0])/(self.zoom_slider_x_range[1]-self.zoom_slider_x_range[0])+1)**6
        # WARNING : le zoom ne doit pas être plus grand que 1 (sinon...)

    def display_zoom_slider(self) -> None:
        '''Affichage du slider de zoom'''
        # Base du slider
        pygame.draw.rect(screen, BLEU_STP, (self.zoom_slider_pos, (int(120*self.zoom_slider_size_factor), int(20*self.zoom_slider_size_factor))))
        # Barre ou le bouton glisse
        pygame.draw.rect(screen, WHITE, ((int(self.zoom_slider_pos[0]+20*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+6*self.zoom_slider_size_factor)), (int(80*self.zoom_slider_size_factor), int(8*self.zoom_slider_size_factor))), 0, int(2*self.zoom_slider_size_factor))
        pygame.draw.rect(screen, BLACK, ((int(self.zoom_slider_pos[0]+21*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+7*self.zoom_slider_size_factor)), (int(40*self.zoom_slider_size_factor), int(6*self.zoom_slider_size_factor))), 0, int(3*self.zoom_slider_size_factor))
        pygame.draw.rect(screen, BLACK, ((int(self.zoom_slider_pos[0]+59*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+7*self.zoom_slider_size_factor)), (int(40*self.zoom_slider_size_factor), int(6*self.zoom_slider_size_factor))), 0, int(3*self.zoom_slider_size_factor))
        # Le + et le -
        pygame.draw.rect(screen, OR_STP, ((int(self.zoom_slider_pos[0]+4*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+8*self.zoom_slider_size_factor)), (int(12*self.zoom_slider_size_factor), int(4*self.zoom_slider_size_factor))))
        pygame.draw.rect(screen, OR_STP, ((int(self.zoom_slider_pos[0]+104*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+8*self.zoom_slider_size_factor)), (int(12*self.zoom_slider_size_factor), int(4*self.zoom_slider_size_factor))))
        pygame.draw.rect(screen, OR_STP, ((int(self.zoom_slider_pos[0]+108*self.zoom_slider_size_factor), int(self.zoom_slider_pos[1]+4*self.zoom_slider_size_factor)), (int(4*self.zoom_slider_size_factor), int(12*self.zoom_slider_size_factor))))
        # Le bouton
        pygame.draw.rect(screen, RED, ((self.zoom_slider_current_x_pos, int(self.zoom_slider_pos[1]+4*self.zoom_slider_size_factor)), (int(4*self.zoom_slider_size_factor), int(12*self.zoom_slider_size_factor))), 0, int(2*self.zoom_slider_size_factor))

    def barre_action(self, gre, chn, lune) -> None:
        '''Créer une barre sur la gauche pour ajouter boutons et intéractions'''
        # Change la couleur en fonction de l'activation du module
        if chn:
            color_chn = GREEN
        else:
            color_chn = OR_STP 
        if gre:
            color_gre = GREEN
        else:
            color_gre = OR_STP
        if lune:
            color_lune = GREEN
        else:
            color_lune = OR_STP
        # Fais apparaitre les differents boutons 
        pygame.draw.rect(screen, BLEU_STP, ((0, 0),   (50, 600)))
        pygame.draw.rect(screen, color_gre,   ((0, 120), (50, 50)))
        pygame.draw.rect(screen, color_chn,   ((0, 270), (50, 50)))
        pygame.draw.rect(screen, color_lune,   ((0, 420), (50, 50)))
        pygame.draw.rect(screen, RED,      ((0, 550), (50, 50)))
        picto_astro = pygame.transform.scale(pygame.image.load(main_path+"images/pictoastro.png"), (46, 46))
        screen.blit(picto_astro, (2, 122))
        picto_astro_ch = pygame.transform.scale(pygame.image.load(main_path+"images/pictofire.png"), (42, 42))
        screen.blit(picto_astro_ch, (2, 273))
        pictolune = pygame.transform.scale(pygame.image.load(main_path+"images/pictolune.png"), (65, 50))
        screen.blit(pictolune, (-10, 420))

        '''bouton menu'''
        pygame.draw.rect(screen, GRAY,  ((0, 0),  (50, 50)))
        pygame.draw.line(screen, WHITE, (10, 12), (40, 12), 3)
        pygame.draw.line(screen, WHITE, (10, 25), (40, 25), 3)
        pygame.draw.line(screen, WHITE, (10, 38), (40, 38), 3)
        
        '''bouton quitter'''
        quitter = grandfont.render("X", 1, BLACK)
        screen.blit(quitter, (11, 557))

    def date_actiuelle(self, time):
        '''affiche la date actuelle du système à gauche du slider zoom'''
        date = Temps.gregorien(time)
        if round(date[2]) < 10: 
            jour = "0" + str(round(date[2]))
        else:
            jour = str(round(date[2]))
        if date[1] < 10: 
            mois = "0" + str(date[1])
        else:
            mois = str(date[1])
        année = str(date[0])
        pygame.draw.rect(screen, GRAY,  ((50, 550),  (462, 50)))
        pygame.draw.line(screen, WHITE, (50, 551),  (600, 551), 3)
        pygame.draw.line(screen, WHITE, (51, 550),  (51, 600), 3)
        affichage = moyfont.render("Date actuelle : " + jour + "/" + mois + "/" + année, 1, BLACK)
        screen.blit(affichage, (100, 565))

    def signe_astro(self, signe, data, lunaison):
        """"affiche le signe asrtrologique et ses informations"""
        getsigne = signes.get(signe)
        if data or lunaison:
            '''petite version si les données planètes sont affichées'''
            pygame.draw.rect(screen, BLEU_STP, ((225, 200), (400, 200)), 0, 10)
            pygame.draw.rect(screen, GRAY,     ((225, 200), (400, 45)),  0, 0, 10, 10, 0, 0)
            pygame.draw.rect(screen, RED,      ((225, 200), (45,  45)),  0, 0, 10, 0, 0, 30)
            text = moyfont.render(getsigne[0], 1, OR_STP)
            text2 = moyfont.render(getsigne[1], 1, BLEU_FC)
            text3 = moyfont.render(getsigne[2], 1, BLEU_FC)
            croix = moyfont.render("X", 1, WHITE)
            screen.blit(text, (350, 210))
            screen.blit(text2, (250, 280))
            screen.blit(text3, (250, 330))
            screen.blit(croix, (235, 210))
        if not data and not lunaison:
            '''version plus large si les données des planètes ne sont pas à l'écran'''
            pygame.draw.rect(screen, BLEU_FC,  ((640, 200), (210, 200)), 0, 0,  0, 10, 0, 10)
            pygame.draw.rect(screen, BLEU_STP, ((250, 200), (400, 200)), 0, 10)
            pygame.draw.rect(screen, GRAY,     ((250, 200), (400, 45)),  0, 0, 10, 10, 0, 0)
            pygame.draw.rect(screen, RED,      ((250, 200), (45,  45)),  0, 0, 10,  0, 0, 30)
            img_name = getsigne[0].replace(' ', '')    
            '''images'''
            img = pygame.image.load(main_path+"images/"+ img_name +".png")
            img = pygame.transform.scale(img, (175, 125))
            screen.blit(img, (660, 240))
            '''textes'''
            text = moyfont.render(getsigne[0], 1, OR_STP)
            text2 = moyfont.render(getsigne[1], 1, BLEU_FC)
            text3 = moyfont.render(getsigne[2], 1, BLEU_FC)
            croix = moyfont.render("X", 1, WHITE)
            '''affichage final'''
            screen.blit(text, (400, 210))
            screen.blit(text2, (265, 280))
            screen.blit(text3, (265, 330))
            screen.blit(croix, (260, 210))


    def signe_astro_ch(self, signe, data, lunaison):
        """"affiche le signe asrtrologique et ses informations"""
        getsigne = signes.get(signe)
        if data or lunaison:
            '''petite version si les données planètes sont affichées'''
            pygame.draw.rect(screen, BLEU_STP, ((225, 200), (400, 200)), 0, 10)
            pygame.draw.rect(screen, GRAY,     ((225, 200), (400, 45)),  0, 0, 10, 10, 0, 0)
            pygame.draw.rect(screen, RED,      ((225, 200), (45,  45)),  0, 0, 10, 0, 0, 30)
            text = moyfont.render(getsigne[0], 1, OR_STP)
            text2 = moyfont.render(getsigne[1], 1, BLEU_FC)
            text3 = moyfont.render(getsigne[2], 1, BLEU_FC)
            croix = moyfont.render("X", 1, WHITE)
            screen.blit(text, (350, 210))
            screen.blit(text2, (250, 280))
            screen.blit(text3, (250, 330))
            screen.blit(croix, (235, 210))
        if not data and not lunaison:
            '''version plus large si les données des planètes ne sont pas à l'écran'''
            pygame.draw.rect(screen, BLEU_FC,  ((640, 200), (210, 200)), 0, 0,  0, 10, 0, 10)
            pygame.draw.rect(screen, BLEU_STP, ((250, 200), (400, 200)), 0, 10)
            pygame.draw.rect(screen, GRAY,     ((250, 200), (400, 45)),  0, 0, 10, 10, 0, 0)
            pygame.draw.rect(screen, RED,      ((250, 200), (45,  45)),  0, 0, 10,  0, 0, 30)
            img_name = getsigne[0].replace(' ', '')    
            '''images'''
            img = pygame.image.load(main_path+"images/"+ img_name +".jpg")
            img = pygame.transform.scale(img, (175, 175))
            screen.blit(img, (662, 213))
            '''textes'''
            text = moyfont.render(getsigne[0], 1, OR_STP)
            text2 = moyfont.render(getsigne[1], 1, BLEU_FC)
            text3 = moyfont.render(getsigne[2], 1, BLEU_FC)
            croix = moyfont.render("X", 1, WHITE)
            '''affichage final'''
            screen.blit(text, (400, 210))
            screen.blit(text2, (265, 280))
            screen.blit(text3, (265, 330))
            screen.blit(croix, (260, 210))
        
        
    def ecriture(self, planete, dist) -> None:
        '''Fait apparaitre les données de la planète choisie'''
        # Cherche dans le dictionnaire ==> (work in progress)
        dataget = data.get(planete)
        # Récupérations des données + mise en forme
        text = font.render(dataget[0], 1, BLACK)
        poids = font.render(dataget[1], 1, BLACK)
        rayon = font.render(dataget[2], 1, BLACK)
        distance = font.render("distance = " + dist + " Ua", 1, BLACK)
        rotation = font.render(dataget[4], 1, BLACK)
        temperature = font.render(dataget[5], 1, BLACK)
        # Affichage des données
        screen.blit(text, (900, 290))
        screen.blit(poids, (815, 350))
        screen.blit(rayon, (815, 375))
        screen.blit(distance, (815, 400))
        screen.blit(rotation, (815,425))
        screen.blit(temperature, (815,450))

        # img = pygame.image.load(dataget[-1])
        # img = pygame.transform.scale(img, (280, 275))
        screen.blit(dataget[-1], (800, 0))

    def lunaison(self):
        '''dessine la zone de texte por les infos de la lune avec le gif'''
        # affichage gif 
        pygame.draw.rect(screen, BLEU_FC,  ((800,   0), (1080, 275)))
        # Affichage espace données
        pygame.draw.rect(screen, WHITE,    ((800, 275), (1080, 600)))
        pygame.draw.rect(screen, DARK_GRAY,     ((800, 381), (1080, 498)))
        # Lignes de séparation
        pygame.draw.line(screen, OR_STP,    (800, 276), (1080, 276), 3)
        pygame.draw.line(screen, OR_STP,    (800, 380), (1080, 380), 3)
        pygame.draw.line(screen, OR_STP,    (800, 498), (1080, 498), 3)
        pygame.draw.line(screen, OR_STP,    (798,   0), ( 798, 600), 3)
        pygame.draw.line(screen, OR_STP,    (798, 495), (1080, 495), 3)

    def ecriture_lune(self, temps): 
        '''Fait apparaitre les données de la planète choisie'''
        TLune = Temps.phase_lune(temps)
        # gif = Image.open(main_path + "images/gif_lune/lune.gif")
        # Affichage informations complémentaire
        text = moyfont.render("La Lune", 1, BLACK)
        pourcent = (2 * TLune / 29.53) * 100 if TLune < 29.53/2 else (200 * (29.53-TLune) / 29.53)
        pourcentage = font2.render(f"Pourcentage = {round(pourcent, 2)} %", 1, BLEU_FC)
        # Utilise cette différence pour déduire phase actuelle de la Lune 
        if TLune >= 0 * luneSur100 and TLune <= 12 * luneSur100:
            lunaison = font2.render("Nouvelle Lune", 1 , BLEU_STP)
        elif 12 * luneSur100 < TLune < 25 * luneSur100:
            lunaison = font2.render("1er Croissant", 1 , BLEU_STP)
        elif 20 * luneSur100 < TLune <= 30 * luneSur100:   
            lunaison = font2.render("1er Quartier", 1 , BLEU_STP)
        elif 30 * luneSur100 < TLune <= 45 * luneSur100:
            lunaison = font2.render("Lune Gibbeuse Croissante", 1 , BLEU_STP)
        elif 45 * luneSur100 < TLune <= 55 * luneSur100:
            lunaison = font2.render("Pleine Lune", 1 , BLEU_STP)
        elif 55 * luneSur100 < TLune <= 70 * luneSur100:
            lunaison = font2.render("Lune Gibbeuse Déroissante", 1 , BLEU_STP)
        elif 70 * luneSur100 < TLune <= 80 * luneSur100:
            lunaison = font2.render("Dernier Quartier", 1 , BLEU_STP)
        elif 80 * luneSur100 < TLune <= 95 * luneSur100:
            lunaison = font2.render("Dernier Croissant", 1 , BLEU_STP)
        elif 95 * luneSur100 < TLune <= 101 * luneSur100:
            lunaison = font2.render("Nouvelle Lune", 1 , BLEU_STP)
        else:
            lunaison = font2.render("Erreur", 1 , BLEU_STP)
        gif = IMAGES_LUNE[round((TLune/29.53*(len(IMAGES_LUNE)-1)) + (len(IMAGES_LUNE)-1)/2) % (len(IMAGES_LUNE)-1)]
        distance = font.render("Distance Terre = 384 400 km", 1, SOFT_WHITE)
        rotation = font.render("Durrée Lunaison = 27 jours", 1, SOFT_WHITE)
        temperature = font.render("temperature = -230°C / 120°C", 1, SOFT_WHITE)
        # Affichage final des données
        screen.blit(text, (880, 285))
        screen.blit(lunaison, (815, 325))
        screen.blit(pourcentage, (815, 352))
        screen.blit(distance, (815, 400))
        screen.blit(rotation, (815,430))
        screen.blit(temperature, (815,460))
        # Gif lune
        lune = pygame.transform.scale(gif, (280, 280))
        screen.blit(lune, (800, 0))


    def confirmation(self) -> None:
        '''Dessine écran validation quitter'''
        pygame.draw.rect(screen, GRAY,         ((340, 200), (400, 200)), 0, 5)
        pygame.draw.rect(screen, GREEN_CUSTOM, ((400, 300), (100, 50)),  0, 10)
        pygame.draw.rect(screen, RED,          ((590, 300), (100, 50)),  0, 10)
        sur = moyfont.render("Sûr de vouloir quitter ?", 1, OR_STP)
        screen.blit(sur, (387, 233))
        quitter = moyfont.render("Oui", 1, WHITE)
        screen.blit(quitter, (425, 312))
        non = moyfont.render("Non", 1, WHITE)
        screen.blit(non, (615, 312))

    def wallE(self, objet, rotation):
        '''fait apparaitre et deplace de l'objet demandé   :)'''
        img = pygame.transform.scale(pygame.image.load(main_path+"images/"+ objet +".png"), (350, 175))
        img = pygame.transform.rotate(img, self.wallE_rotation + rotation)
        screen.blit(img, (self.wallE_x, self.wallE_y))
        self.wallE_x -= 5
        self.wallE_rotation += 0.3
        if self.wallE_rotation >= 88 or self.wallE_rotation <= 90 or self.wallE_rotation >= 168 or self.wallE_rotation <= 170:
            self.wallE_y += 0.4
        if self.wallE_rotation >= 178 or self.wallE_rotation <= 180 or self.wallE_rotation >= 358 or self.wallE_rotation <= 0:
            self.wallE_y += 0.4

    def verif_object(self):
        '''vérifie l'emplacement de l'objet pour l'arreter si son animation est fini et replacer au point de départ'''
        if self.wallE_x == -300:
            self.wallE_x = 1080 #position x wall-E
            self.wallE_y = 25 #position y wall-E
            self.wallE_rotation  = 4
            return False
        else: 
            return True


# class sons():

#     def __init__(self) -> None:
#         pygame.mixer.init()
        
#     def lecture(self):
#         sound = pygame.mixer.Sound(main_path+"musique/musiques.mp3")
#         pygame.mixer.Sound.play(sound)

#     def pause(self):
#         pygame.mixer.music.pause()


class Gestion_Planete:

    def __init__(self, mass_center: Tuple(int, int)) -> None :
        '''initialisation des planètes'''
        # Définition des planètes : 
        #              [PLanète   (perigée,            apogée,              centre de masse,            angle perigée avec Mercure), date perigee,       periode orbitale,  couleur,         taille]
        self.mercury = [kp.Planete(0.3055966332078965, 0.46842943478058124, center_of_mass=mass_center, angle=0),                    2459507.4984667003, 87.969_349_63,     (110, 120,  80), 63    ]
        self.venus   = [kp.Planete(0.7096395277449469, 0.73676134561161,    center_of_mass=mass_center, angle=0.42216048217738344),  2459378.050801399,  224.700_818_8,     (255, 130,  10), 91    ]
        self.terre   = [kp.Planete(0.9759349503905891, 1.0231627778961105,  center_of_mass=mass_center, angle=0.15288811480428713),  2459217.95935868,   365.259_635_8,     ( 40, 130, 250), 96    ]
        self.mars    = [kp.Planete(1.3892063960381649, 1.6568787018388922,  center_of_mass=mass_center, angle=0.1933828995017202),   2459064.98384513,   686.995_785_7,     (165, 110,  35), 51    ]
        self.jupiter = [kp.Planete(4.959802875063826,  5.454701809756877,   center_of_mass=mass_center, angle=0.059062298186004995), 2459969.8332017004, 4_332.897_065,     (220, 190, 140), 120   ]
        self.saturne = [kp.Planete(9.034936763609108,  10.072123061732313,  center_of_mass=mass_center, angle=0.0062405892185779),   2452830.12,         10_764.216_76,     (190, 180, 160), 170   ]
        # Les deux planètes qui suivent ont des données imprécises :
        self.uranus  = [kp.Planete(20.486593604250178, 21.01928151424853,   center_of_mass=mass_center, angle=0.032404368695452976),  2470004.5,         30_698,            (109, 180, 255), 500   ]
        self.neptune = [kp.Planete(           0000000,             00000,   center_of_mass=mass_center, angle=000000000           ),  000000000,         60 216.8,          (104, 111, 255), 3000  ]

        self.planetes = [self.mercury, self.venus, self.terre, self.mars, self.jupiter, self.saturne, self.uranus]

        # Ajout d'un dernier argument : La planète est-elle suivie par la caméra ?
        #                               Sa position
        #                               Sa taille (relative au zoom)
        #                               Les coordonnées à ajouter à la caméra pour suivre la planête
        self.data_index = len(self.planetes[0]) # Index de cet argument
        for planete in self.planetes:
            planete.append([False, (0, 0), 0, (0, 0)]) # Argument ajouté

    def draw_planet(self, date: int, planete: list, camera_zoom: float, camera_true_pos: List(int, int), camera_focus: List(int, int), sun_pos: List(int, int), vitesse: float) -> None:
        '''Permet de dessiner une planète au bon endroit'''
        # Calcul des positions
        time_to_calc = date - planete[1] # Calcul de la date (depuis un temps donné permettant de faciliter la création de ce système solaire)
        pos = planete[0].calculate_point_from_time(time_to_calc/planete[2]) # Calcul de la position
        time_to_calc_next = time_to_calc + vitesse # On "prédit" le temps de la frame suivante
        pos_next = planete[0].calculate_point_from_time(time_to_calc_next/planete[2]) # Nouvelle position
        # Ci-dessous, ajustement de la position et de la taille
        pos_final = (int(sun_pos[0] + camera_focus[0] + (pos[0] - sun_pos[0]) * camera_zoom*3000 + (sun_pos[0] - camera_true_pos[0]) * camera_zoom), int(sun_pos[1] + camera_focus[1] + (pos[1] - sun_pos[1]) * camera_zoom*3000 + (sun_pos[1] - camera_true_pos[1]) * camera_zoom))
        pos_alt = (int((sun_pos[0] - pos_next[0]) * camera_zoom*3000), int((sun_pos[1] - pos_next[1]) * camera_zoom*3000))
        # Taille apparente de la planête
        size = int(planete[4]*camera_zoom+1)
        # Affichage de la planète
        pygame.draw.circle(screen, planete[3], pos_final, size)
        # On garde en mémoire la position et la taille (apparente) de la planète
        planete[self.data_index] = [planete[self.data_index][0], pos_final, size, pos_alt]

    def draw_all_planets(self, date: int, camera_zoom: float, camera_true_pos: List(int, int), camera_focus: List(int, int), sun_pos: List(int, int), vitesse: float) -> None:
        '''Dessine toutes les planètes'''
        for planete in self.planetes:
            self.draw_planet(date, planete, camera_zoom, camera_true_pos, camera_focus, sun_pos, vitesse)
    
    def get_followed_pos(self) -> Tuple(float, float) :
        '''Permet de récupérer les coordonnées de la planète suivie'''
        for planete in self.planetes:
            if planete[self.data_index][0]:
                return planete[self.data_index][3]
        return (0, 0) # Cas où aucune planète n'est suivie
    
    def follow(self) -> tuple:
        '''Permet de commencer à suivre une planète'''
        mouse = pygame.mouse.get_pos() # On récupère la position du curseur
        for planete in self.planetes:
            # Le +5 à la fin de la condition ci-dessous permet de pouvoir cliquer plus facilement sur une planète
            if ((mouse[0]-planete[self.data_index][1][0])**2 + (mouse[1]-planete[self.data_index][1][1])**2)**0.5 <= planete[self.data_index][2] + 5:
                # Cas où une planète est cliquée
                planete[self.data_index][0] = True
                return True, planete[self.data_index][3]
        # Cas où aucune planète n'est cliquée (else:)
        return False, (0, 0)
    
    def unfollow_all(self) -> None:
        '''Permet d'arrêter de suivre toutes les planêtes'''
        for planete in self.planetes:
            planete[self.data_index][0] = False

    def distance(self, sunpos, camera_focus):
        distance = math.sqrt(abs((camera_focus[0]**2 - sunpos[0]**2) + (camera_focus[1]**2 - sunpos[1]**2)))# Calcule distance entre les deux points 
        return str(round(distance))

def get_followed_planet(gest: Gestion_Planete) :
        '''Permet de récupérer la planète suivie'''
        for planete in gest.planetes:
            if planete[gest.data_index][0]:
                return 'A B C D E F G H'.split()[gest.planetes.index(planete)]
        return (0, 0) # Cas où aucune planète n'est suivie


class Text_Input:

    def __init__(self) -> None:
        '''initialisation'''
        self.pos = [830, 568] # Position de la barre d'input textuelle
        self.text = '' # Le contenu de la barre d'input textuelle
        self.bg_text = 'JJ / MM / AAAA' # Le texte "place holder"
        self.selected = False # Permet de savoir si la barre d'input textuelle est sélectionnée
        self.rect = ((800, 553), (190, 48)) # Position de l'encadrement de la barre d'input textuelle (utilisé pour les collisions)
        self.statut = 0 # x < 0 --> rouge ; x = 0 --> jaune ; x > 0 --> vert
    
    def clicked(self, mouse_pos: Tuple(int, int)) -> None:
        '''On vérifie si la barre d'input textuelle est cliquée (ou non)'''
        if pygame.Rect(self.rect).collidepoint(mouse_pos):
            self.selected = not self.selected
        else:
            self.selected = False

    def check_input(self, event: pygame.KEYDOWN, temps: float) -> float:
        '''Fonction permettant d'écrire dans la barre d'input textuelle et renvoyer le temps si nécessaire'''
        
        # Valider l'input
        if event.key == pygame.K_RETURN:
            # On vérifie que l'imput et valide
            if self.verif():
                # Cas où l'imput est valide
                return Temps.JJ(int(self.text[4:]), int(self.text[2:4]), int(self.text[:2]))
            # Cas échéant (else:)
            return temps
        
        # Retour en arrière
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        
        # Input
        else:
            self.text += str(event.unicode)
        
        # Si rien n'est touché
        return temps

    def retour_date(self):
        '''renvoie la date convertie en jour juliens'''
        date = Temps.JJ(int(self.text[4:]), int(self.text[2:4]), int(self.text[:2]))
        return date

    def retour_date_complete(self):
        '''renvoie la date complète (pour usages spécifiques)'''
        date = [int(self.text[4:]), int(self.text[2:4]), int(self.text[:2])]
        return date
        
    def verif(self):
        '''verifie si la date est compatible avec les signes astrologiques'''
        # Si on a bien : JJ / MM / AAAA avec AAAA contenant au moins 1 chiffre
        if len(self.text) > 4:
            # Test pour voir si tous les chiffres sont valide
            for index, letter in enumerate(self.text):
                # Il ne peut y avoir de signe "-" qu'en 5ème position (année)
                if index == 4 and len(self.text) > 5:
                    if not letter in [str(x) for x in range(10)]+['-']:
                        self.statut = -45
                        return False # Erreur
                else:
                    if not letter in [str(x) for x in range(10)]:
                        self.statut = -45
                        return False # Erreur

            # Le jour, mois ou année ne peut être égal à 0, ni suppérieur à 31 ou 12 
            if 32 > int(self.text[:2]) != 0 and 13 > int(self.text[2:4]) != 0 and int(self.text[4:]) != 0:

                # Vérifie le nombre de jour pour le mois de fevrier 
                if int(self.text[2:4]) == 2:
                    # En fonction des années bissextiles 
                    if (int(self.text[4:]) - 2016) % 4 == 0:
                        if int(self.text[:2]) <= 29:
                            self.statut = 45
                            return True
                    # Et non bissextiles
                    elif int(self.text[:2]) <= 28:
                        self.statut = 45
                        return True
                    # Cas échéant (else:)
                    self.statut = -45
                    return False

                # Vérifie le nombre de jour pour les mois de 30 j 
                elif int(self.text[2:4]) == 4 or int(self.text[2:4]) == 6 or int(self.text[2:4]) == 9 or int(self.text[2:4]) == 11:
                    if int(self.text[:2]) < 31:
                        self.statut = 45
                        return True
                    # Cas échéant (else:)
                    self.statut = -45
                    return False
                
                # Condition déjà testé lors de   -->   if 32 > int(self.text[:2]) != 0 and 13 > int(self.text[2:4]) != 0 and int(self.text[4:]) != 0:
                #
                # Vérifie le nombre de jour pour les mois de 31 j 
                # if int(self.text[2:4]) == 1 or int(self.text[2:4]) == 3 or int(self.text[2:4]) == 5 or int(self.text[2:4]) == 7 or int(self.text[2:4]) == 8 or int(self.text[2:4]) == 10 or int(self.text[2:4]) == 12:
                #     if int(self.text[:2]) < 32:
                #         self.statut = 45
                #         return True

                # Tous les autres cas sont bons (else:)
                self.statut = 45
                return True

        # Sinon renvoie une erreur 
        self.statut = -45
        return False # Erreur
        
    def display(self) -> None:
        '''Affichage de la barre d'input textuelle'''
        # Encadrement de la barre d'input textuelle
        if self.selected:
            color = OR_STP
        else:
            color = BLEU_STP
        # Choix de la couleur lors de l'encadrement de la barre d'input textuelle
        if abs(self.statut) % 30 <= 15:
                if self.statut > 0:
                    color = GREEN
                elif self.statut < 0:
                    color = RED
        pygame.draw.rect(screen, color, self.rect, 5)
        # Création du texte affiché (on met en forme et en fait une surface affichable)
        if len(self.text) > 4:
            text_list = [self.text[:2], self.text[2:4], self.text[4:]]
        elif len(self.text) > 2:
            text_list = [self.text[:2], self.text[2:]]
        else:
            text_list = [self.text]
        text_str = ' / '.join(text_list)
        text = font.render(text_str, 1, OR_STP)
        # Création du texte de "place holder"
        if len(text_str) >= len(self.bg_text):
            bg_text_str = ''
        else:
            bg_text_str = text_str[:len(text_str)] + self.bg_text[len(text_str):]
        text_bg = font.render(bg_text_str, 1, BLEU_STP)
        # Affichage
        screen.blit(text_bg, self.pos)
        screen.blit(text, self.pos)
        # Actualisation du statut de la barre d'input textuelle
        if self.statut < 0:
            self.statut += 1
        elif self.statut > 0:
            self.statut -= 1


class Trainee:

    def __init__(self, anim_speed: int=1, init_now: bool=False):
        self.anim_speed = anim_speed
        self.current_frame = 0
        self.all_points = [] # Argument : [pos x y, durée de vie]
        if init_now:
            self.pre_start()
    
    def pre_start(self):
        for i in range(255):
            self.all_points.append([(random.randint(0, width), random.randint(0, height)), 255-i])
    
    def add_point(self, pos: Tuple(float, float)):
        '''Ajouter un point à afficher'''
        if not self.current_frame:
            self.all_points.append([pos, 255])
            self.current_frame = self.anim_speed
        self.current_frame -= 1

    def display(self):
        '''Affichage plus actualisation des points'''
        for point in self.all_points:
            if point[1] > 0:
                screen.set_at(point[0], [255 - abs(point[1] * 2 - 255)] * 3)
                if not self.current_frame:
                    point[1] -= 1
            else:
                self.all_points.remove(point)


def main() -> None:

    HUD = ecran()
    trainee = Trainee(5, True)
    data = False
    jouer = True
    validquit = False
    signe_astro = False
    signe_astro_ch = False
    appel = "C"
    # SON = sons()
    can_press_button = True
    lunaison = False
    objet = False
    sprite = "wallE"
    rotation = 0

    time_set = Text_Input()

    sunpos = (int(width/2), int(height/2))

    #moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)
    planetes = Gestion_Planete(sunpos)
    temps = Temps.JJ(*list(gmtime(time()))[:3]) # Date actuelle
    vitesse_normale = 30 # Jours par secondes
    true_speed = 0 # Vitesse en jour par frame
    frame_time = time() # Permet d'évaluer les fps de l'ordi afin d'adapter la vitesse

    vitesse = vitesse_normale
    vitesse_lente = vitesse / 4
    vitesse_rapide = vitesse * 4
    
    cam_speed = 5 # Vitesse de déplacement de la caméra
    camera_zoom = 1 # Facteur de zoom sur la simulation
    camera_true_pos = list(sunpos) # Position théorique de la caméra
    camera_focus = (0, 0) # Postion de l'objet à suivre
    is_following = False # Permet de savoir si la caméra suit une planète
    # SON.lecture()

    # Nom des objets à déplacer 
    wallE = "wallE"
    buzz = "buzz"
    falcon = "falcon"
    iss = "iss"
    apollo = "apollo"

    # Variable utilisée pour le "click and drag"
    mouse_current_pos = (0, 0)

    while True:

        
        dt = clock.tick(144)
        #on creer un fond de couleur noir
        screen.fill(BLACK)

        # Actualisation du zoom
        if camera_zoom != HUD.zoom_factor:
            camera_zoom = HUD.zoom_factor
            #moon.compute_orbit_path(camera_zoom, camera_pos)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            
            # Actions à ne faire qu'une seule fois par clique
            if event.type == pygame.KEYDOWN:

                if time_set.selected:
                    # Input pour la barre d'input textuelle
                    temps = time_set.check_input(event, temps)
                    
                    # J'ai "Ctrl + C" puis "Ctrl + V" le code plus bas pour ajouter cette condition
                    if event.key == pygame.K_RETURN:
                        if time_set.verif():
                            temps = time_set.retour_date()
                            # Wall-E en 2008
                            if temps > 2454466 and temps < 2454832:
                                sprite = wallE
                                rotation = 0
                                objet = True
                            # L'ISS en 2011
                            elif temps > 2455561.5 and temps < 2455927.5:
                                sprite = iss
                                rotation = random.randint(0, 359)
                                objet = True
                            # Buzz l'éclaire en 1995
                            elif temps > 2449717.5 and temps < 2450083.5:
                                sprite = buzz
                                rotation = 315
                                objet = True
                            # Star Wars ( Faucon Millénium ) en 1977
                            elif temps > 2443143.5 and temps < 2443509.5:
                                sprite = falcon
                                rotation = 325
                                objet = True
                            # Fusée apollo 11 en 1969
                            elif temps > 2440221.5 and temps < 2440587.5:
                                sprite = apollo
                                rotation = 50
                                objet = True
                else:
                    # Affichage ou non des informations sur la planête
                    if event.key == pygame.K_z:
                        data = not data

                    # Pause ou marche
                    if event.key == pygame.K_SPACE:
                        jouer = not jouer

                    if event.key == pygame.K_q:
                        vitesse /= 2
                        
                    if event.key == pygame.K_s:
                        vitesse = vitesse_normale

                    if event.key == pygame.K_d:
                        vitesse *= 2
                    
                    if event.key == pygame.K_w:
                        objet = not objet
                    
                    if event.key == pygame.K_a:
                        if time_set.verif():
                            signe_astro = not signe_astro

                    if event.key == pygame.K_c:
                        if time_set.verif():
                            signe_astro_ch = not signe_astro_ch

                # On arrète de suivre la planète
                if event.key == pygame.K_BACKSPACE and not time_set.selected:
                    planetes.unfollow_all()
                    camera_true_pos = list(sunpos)
                    camera_focus = [0, 0]
                    is_following = False
                    data = False

        # Actions à faire tant que la touche est pressée
        pressed = pygame.key.get_pressed()

        # On définit la vitesse
        speed = cam_speed/camera_zoom

        # Déplacement vers le haut
        if pressed[pygame.K_UP]:
            camera_true_pos[1] -= speed
        # Déplacement vers le bas
        if pressed[pygame.K_DOWN]:
            camera_true_pos[1] += speed
        # Déplacement vers la gauche
        if pressed[pygame.K_LEFT]:
            camera_true_pos[0] -= speed
        # Déplacement vers la droite
        if pressed[pygame.K_RIGHT]:
            camera_true_pos[0] += speed
        
        # Click and drag
        if not can_press_button and not HUD.zoom_slider_clicked:
            mouse = pygame.mouse.get_pos()
            camera_true_pos = [camera_true_pos[0] - (mouse[0] - mouse_current_pos[0]) / camera_zoom, camera_true_pos[1] - (mouse[1] - mouse_current_pos[1]) / camera_zoom]
            mouse_current_pos = mouse

        # Actualisation de la position finale de la caméra
        if is_following:
            camera_focus = planetes.get_followed_pos()
            data = True
            appel = get_followed_planet(planetes)


        if jouer:
            temps, true_speed, frame_time = update_time(temps, vitesse, frame_time) # Permet de finaliser l'acutalisation du temps
        else:
            temps, true_speed, frame_time = update_time(temps, 0, frame_time) # Permet d'avoir un semblant de pause


        trainee.add_point((random.randint(0, width), random.randint(0, height)))
        trainee.display()


        # Formule simplifiée utilisé pour le zoom :
        # centre_ecran + (pos_initialle - pos_camera) * zoom_camera

        # Formule complète :
        # Etape 1 (effet de zoom sur les objets)   ->   centre_ecran + (pos_initialle - centre_ecran) * zoom_camera
        # Etape 2 (repositionnement de la caméra)   ->   (centre_ecran - pos_camera) * zoom_camera
        # Position finale = Etape 1 + Etape 2

        # on fait apparaitre les différents astres
        #pygame.draw.circle(screen, WHITE, [int(sunpos[0] + (moon_pos[0] - camera_pos[0]) * camera_zoom), int(sunpos[1] + (moon_pos[1] - camera_pos[1]) * camera_zoom)], 15*camera_zoom) # Astre random sorti de mon imaginaire
        planetes.draw_all_planets(temps, camera_zoom, camera_true_pos, camera_focus, sunpos, true_speed)
        pygame.draw.circle(screen, YELLOW, [int(sunpos[0] + camera_focus[0] + (sunpos[0] - camera_true_pos[0]) * camera_zoom), int(sunpos[1] + camera_focus[1] + (sunpos[1] - camera_true_pos[1]) * camera_zoom)], 200*camera_zoom+1) # Soleil
        #for point in moon.orbit_path :
            #screen.set_at((int(point[0]), int(point[1])), WHITE)
            # print(int(point[0]), int(point[1]))


        #mise en place des éléments de l'interface
        
        if objet:
            HUD.wallE(sprite, rotation)
        if data:
            lunaison = False
            HUD.espace_donnee()
            HUD.ecriture(appel, planetes.distance(sunpos, camera_focus))
        if lunaison:
            vitesse = 1
            data = False
            HUD.lunaison()
            HUD.ecriture_lune(temps)

        HUD.barre_action(signe_astro, signe_astro_ch, lunaison)
        HUD.play_pause_date()
        HUD.vitesse_lecture(vitesse)
        HUD.display_bouton_pause(jouer)
        HUD.zoom_slider()
        HUD.date_actiuelle(temps)
        time_set.display()


        '''affiche le signe astrologique grégorien'''
        if signe_astro:
            signe_astro_ch = False
            saisie = time_set.retour_date_complete()
            HUD.signe_astro(Temps.astro_fra(saisie[0], saisie[1], saisie[2]), data, lunaison)
            if time_set.selected:
                signe_astro = False

        '''affiche le signe astrologique chinois'''
        if signe_astro_ch:
            signe_astro = False
            saisie = time_set.retour_date_complete()
            HUD.signe_astro_ch(Temps.astro_chn(saisie[0], saisie[1], saisie[2]), data, lunaison)
            if time_set.selected:
                signe_astro_ch = False

        # Ci-dessous tous les boutons cliquables

        # Lors du clique de la souris
        if can_press_button and pygame.mouse.get_pressed()[0]:

            can_press_button = False # Permet d'éviter de cliquer plusieurs fois sans le vouloir

            # Récupération coordonnées souris
            pos_souris = pygame.mouse.get_pos()

            # Permet de detecter le clic de la souris

            time_set.clicked(pos_souris) # On check si la barre d'input textuelle est cliquée

            '''Bouton vitesse lente change en fonction de la vitesse actuelle'''
            if pos_souris[0] > 800 and pos_souris[0] < 890 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == vitesse_lente :
                    vitesse = vitesse_normale
                else:
                    vitesse = vitesse_lente

            '''Bouton vitesse rapide change en fonction de la vitesse actuelle'''
            if pos_souris[0] > 990 and pos_souris[0] < 1080 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == vitesse_rapide:
                    vitesse = vitesse_normale
                else:
                    vitesse = vitesse_rapide

            '''Bouton play/pause change en fonction du mode actuelle'''
            if pos_souris[0] > 890 and pos_souris[0] < 990 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if jouer:
                    jouer = False
                else:
                    jouer = not jouer

            '''valide la date et change les planètes de places'''
            if pos_souris[0] > 990 and pos_souris[0] < 1080 and pos_souris[1] > 552 and pos_souris[1] < 600:
                if time_set.verif():
                    temps = time_set.retour_date()
                    # Wall-E en 2008
                    if temps > 2454466 and temps < 2454832:
                        sprite = wallE
                        rotation = 0
                        objet = True
                    # L'ISS en 2011
                    elif temps > 2455561.5 and temps < 2455927.5:
                        sprite = iss
                        rotation = random.randint(0, 359)
                        objet = True
                    # Buzz l'éclaire en 1995
                    elif temps > 2449717.5 and temps < 2450083.5:
                        sprite = buzz
                        rotation = 315
                        objet = True
                    # Star Wars ( Faucon Millénium ) en 1977
                    elif temps > 2443143.5 and temps < 2443509.5:
                        sprite = falcon
                        rotation = 325
                        objet = True
                    # Fusée apollo 11 en 1969
                    elif temps > 2440221.5 and temps < 2440587.5:
                        sprite = apollo
                        rotation = 50
                        objet = True
            
            '''Bouton quitter'''
            # Vérifie si la souris est sur le bouton et quitte appli si clic dans la zone
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 550 and pos_souris[1] < 600:
                validquit = True

            '''Si message pour quitter actif'''
            if validquit:
                # Si  quitter
                if pos_souris[0] > 400 and pos_souris[0] < 500 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    pygame.quit()
                    sys.exit()
                # Si annuler
                elif pos_souris[0] > 600 and pos_souris[0] < 700 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    validquit = not validquit

            '''Bouton menu'''
            # Vérifie si la souris est sur le bouton et retourne au menu principal si clic dans la zone
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 0 and pos_souris[1] < 50:
                launch.main()

            '''Sélection de planète à suivre'''
            if not is_following:
                is_following, camera_focus = planetes.follow()
                if is_following:
                    camera_true_pos = list(sunpos)

            # Bouton de signes astrologiques
            '''bouton signe astrologique grégorien'''
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 120 and pos_souris[1] < 170:
                signe_astro_ch = False
                signe_astro = time_set.verif() 

            '''bouton signe astrologique chinois'''
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 270 and pos_souris[1] < 320:
                signe_astro = False
                signe_astro_ch = time_set.verif()

            # Bouton fermeture ( Croix ) signe astrologique ( tous ) en fonction de data 
            '''bouton fermeture signe astrologique (tous) avec data ouverte'''
            if pos_souris[0] > 225 and pos_souris[0] < 270 and pos_souris[1] > 200 and pos_souris[1] < 245:
                if signe_astro and data or signe_astro and lunaison:
                    signe_astro = False
                elif signe_astro_ch and data or signe_astro_ch and lunaison:
                    signe_astro_ch = False

            '''bouton fermeture signe astrologique ( tous ) avec data fermé'''
            if pos_souris[0] > 250 and pos_souris[0] < 295 and pos_souris[1] > 200 and pos_souris[1] < 245:
                if signe_astro and not data or signe_astro and not lunaison:
                    signe_astro = False
                elif signe_astro_ch and not data or signe_astro_ch and not lunaison:
                    signe_astro_ch = False

            '''bouton affichage lunaison et info'''
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 420 and pos_souris[1] < 470:
                planetes.unfollow_all()
                camera_true_pos = list(sunpos)
                camera_focus = [0, 0]
                is_following = False
                data = False
                lunaison = not lunaison
                if not lunaison:
                    vitesse = vitesse_normale
            
            # Variable utilisée pour le "click and drag"
            mouse_current_pos = pygame.mouse.get_pos()
        
        elif not pygame.mouse.get_pressed()[0]:
            can_press_button = True

        # Si message pour quitter actif
        if validquit:
            HUD.confirmation() # Permet d'afficher le message de confirmation 

        # Verifie si un objet se deplace 
        if objet:
            objet = HUD.verif_object() #Arrete l'objet à l'arrivée
        

        pygame.display.flip() # Affichage final

if __name__ == '__main__':
    main()