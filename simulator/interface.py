import kepler as kp
import pygame
import sys
from time import time
import launch
import Temps
import pygame.mixer
import random
from tools import main_path


BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREEN_CUSTOM = (25, 200, 25)
RED = (200, 0, 0)
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
moyfont = pygame.font.Font(None, 40)
grandfont = pygame.font.Font(None, 60)
# pygame.mixer.music.load(main_path+"musique/musique.mp3")
jouer = False

#données palnètes

data = {'A' :['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j', 'température moyenne = 462°C', main_path+"images/mercure.png"],
                'B' : ['Venus','poids = 4,867 5x10^24 kg', 'rayon = 6050 km', 'distance soleil = 104 mm km', 'temps de rotation = 243 j', 'température moyenne = 440°C',main_path+"images/venus.png"],
                'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km', 'distance soleil = 150 mm km', 'temps de rotation = 365 j', 'température moyenne = 14°C',main_path+"images/terre.png"],
                'D' : ['Mars', 'poids = 6,418 x 10^23 kg','rayon = 3 396 km', 'distance soleil = 227 mm km', 'temps de rotation = 696 j', 'température moyenne = -60°C',main_path+"images/mars.png"],
                'E' : ['Jupiter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km', 'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j', 'température moyenne = -163°C',main_path+"images/jupyter.png"],
                'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km', 'distance soleil = 1,4 md km', 'temps de rotation = 29 ans 167 j', 'température moyenne = -189°C',main_path+"images/saturne.png"],
                'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km','distance soleil = 2,8 md km', 'temps de rotation = 84 ans', 'température moyenne = -218°C',main_path+"images/uranus.png"],
                'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km', 'distance soleil = 4,5 md km', 'temps de rotation = 165 ans', 'température moyenne = -220°C',main_path+"images/neptune.png"],
                'I' : ['Pluton', 'poids = 1,3 X 10^22 kg', 'rayon = 1185 km', 'distance soleil = 6 md km', 'temps de rotation = 248 ans', 'température moyenne = -225°C',main_path+"images/pluton.png"],
                'Z' : ['', '', '', '', '', '',""]}




def update_time(temps: float, j: float, last_frame: float=time()) -> float:
    '''Permet d'avancer dans le temps'''
    new_frame = time() # Permet de faire avancer le temps non pas en fonction des FPS mais du temps réel
    return temps + (j)*(new_frame-last_frame), new_frame


class ecran():

    def __init__(self) -> None:
        # Paramètres du bouton pause
        self.bouton_pause_pos = (915, 503) # Position du bouton pause
        self.bouton_pause_size = (50, 43) # Dimensions du bouton pause
        self.bouton_pause_images = { # Sprites du bouton pause
                                    "play": pygame.transform.scale(pygame.image.load(main_path+"images/play.png"), self.bouton_pause_size),
                                    "pause": pygame.transform.scale(pygame.image.load(main_path+"images/pause.png"), self.bouton_pause_size)}
        # Paramètres des boutons de vitesse de lecture
        self.bouton_vitesse_lecture_pos = (820, 502)
        self.bouton_vitesse_lecture_size = (50, 45)
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
        self.walle_y = 150 #position y wall-E
        self.wallE_rotation  = 4 #rotation wall-E

    def espace_donnee(self) -> None:
        '''Dessine une zone pour photo planete et infos en dessous'''
        pygame.draw.rect(screen, BLEU_FC, ((800, 0), (1080, 275)))#photo planete
        pygame.draw.rect(screen, WHITE, ((800, 275), (1080, 600)))#affichage donnees
        pygame.draw.line(screen, OR_STP, (800, 498), (1080, 498), 3)#lignes de séparation
        pygame.draw.line(screen, OR_STP, (798, 0), (798, 600), 3)

    def play_pause_date(self) -> None:
        '''dessine la zone pour entrer la date '''
        pygame.draw.rect(screen, GRAY, ((800, 550), (1080, 600)))#barre date
        pygame.draw.rect(screen, OR_STP, ((990, 550), (90, 600)))#bouton validation date
        pygame.draw.line(screen, WHITE, (513, 551), (1080, 551), 3)#ligne de séparation
        pygame.draw.line(screen, WHITE, (513, 550), (513, 600), 3)#ligne de séparation
        pygame.draw.line(screen, WHITE, (798, 550), (798, 600), 3)#ligne de séparation
        pygame.draw.rect(screen, BLEU_STP, ((800, 500), (280, 50)))#barre contrôle temps
        pygame.draw.rect(screen, GRAY, ((800, 500), (90, 50)))#bouton sens inverse
        pygame.draw.rect(screen, GRAY, ((990, 500), (280, 50)))#bouton vitesse
        ok = grandfont.render("OK", 1, BLACK)
        screen.blit(ok, (1003, 558))
        
    def display_bouton_pause(self, jeu_en_marche: bool) -> None:
        '''Affichage du bouton pause dans son état "pause" ou "play"'''
        if jeu_en_marche:
            screen.blit(self.bouton_pause_images['play'], self.bouton_pause_pos)
        else:
            screen.blit(self.bouton_pause_images['pause'], self.bouton_pause_pos)

    def vitesse_lecture(self, vitesse: int) -> None:
        '''Affiche l'icone si la lecture rapide/lente est en cours'''
        if vitesse > 30:
            screen.blit(self.bouton_vitesse_lecture_image["rapide"], self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["rapide2"], self.bouton_vitesse_lecture_pos)
        elif vitesse == 30:
            screen.blit(self.bouton_vitesse_lecture_image["normal"], self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["normal2"], self.bouton_vitesse_lecture_pos)
        elif vitesse < 30:
            screen.blit(self.bouton_vitesse_lecture_image["lent"], self.bouton_vitesse_lecture2_pos)
            screen.blit(self.bouton_vitesse_lecture_image["lent2"], self.bouton_vitesse_lecture_pos)
        
    def zoom_slider(self) -> None:
        '''Affichage et gestion du slider de zoom. Permet d'avoir le facteur de zoom actuel'''

        '''Partie "click and drag"'''
        mouse = pygame.mouse.get_pos() # On récupère la position de la souris
        # Si l'utilisateur clique sur le petit bouton du slider : (désolé pour la longueur)
        # Ci-dessous, la version du code où il faut précisément cliquer sur le bouton pour le sélectionner
        #if pygame.mouse.get_pressed()[0] and self.zoom_slider_current_x_pos <= mouse[0] <= self.zoom_slider_current_x_pos+4*self.zoom_slider_size_factor and self.zoom_slider_pos[1]+5*self.zoom_slider_size_factor <= mouse[1] <= self.zoom_slider_pos[1]+15*self.zoom_slider_size_factor and not self.zoom_slider_clicked:
        # Ci-dessous, la version du code où il faut cliquer n'importe où sur la barre sur laquelle le bouton coulisse
        if pygame.mouse.get_pressed()[0] and self.zoom_slider_pos[0]+20*self.zoom_slider_size_factor <= mouse[0] <= self.zoom_slider_pos[0]+100*self.zoom_slider_size_factor and self.zoom_slider_pos[1]+4*self.zoom_slider_size_factor <= mouse[1] <= self.zoom_slider_pos[1]+16*self.zoom_slider_size_factor and not self.zoom_slider_clicked:
            self.zoom_slider_clicked = True
        # Si l'utilisateur arrète de cliquer (donc "lache" le bouton) :
        elif not pygame.mouse.get_pressed()[0]:
            self.zoom_slider_clicked = False
        # PS : pygame.mouse.get_pressed() = Bouton de la souris pressés ? -> (LMB, MMB, RMB) avec dans chacun des emplacement un boolean

        '''Partie déplacement'''
        mouse_x = mouse[0] - self.zoom_slider_size_factor*2 # Ajustement automatique
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
        self.zoom_factor = 2**((0.5)*(self.zoom_slider_current_x_pos-self.zoom_slider_x_range[1]+1)/(self.zoom_slider_current_x_pos-self.zoom_slider_x_range[0]+1)+1)
        # WARNING : le zoom ne doit pas être plus grand que 2 (sinon...)

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

    def barre_action(self) -> None:
        '''Créer une barre sur la gauche pour ajouter boutons et actions'''
        # pygame.draw.rect(screen, OR_STP, ((44, 0), (45, 600)))
        pygame.draw.rect(screen, BLEU_STP, ((0, 0), (50, 600)))
        pygame.draw.rect(screen, OR_STP, ((0, 120), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 270), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 420), (50, 50)))
        pygame.draw.rect(screen, RED, ((0, 550),(50, 50)))

        '''bouton menu'''
        pygame.draw.rect(screen, GRAY, ((0, 0), (50, 50)))
        pygame.draw.line(screen, WHITE, (10, 12),(40, 12), 3)
        pygame.draw.line(screen, WHITE, (10, 25),(40, 25), 3)
        pygame.draw.line(screen, WHITE, (10, 38),(40, 38), 3)
        
        '''bouton quitter'''
        quitter = grandfont.render("X", 1, BLACK)
        screen.blit(quitter, (11, 557))
        
        
    def ecriture(self, planète) -> None:
        '''Fait apparaitre les données de la planète choisie'''
        # Cherche dans le dictionnaire ==> (work in progress)
        dataget = data.get(planète)
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

    def confirmation(self) -> None:
        '''Dessine écran validation quitter'''
        pygame.draw.rect(screen, GRAY, ((340, 200),(400, 200)), 0, 5)
        pygame.draw.rect(screen, GREEN_CUSTOM, ((400, 300),(100, 50)), 0, 10)
        pygame.draw.rect(screen, RED, ((590, 300),(100, 50)), 0, 10)
        sur = moyfont.render("Sûr de vouloir quitter ?", 1, OR_STP)
        screen.blit(sur, (387, 233))
        quitter = moyfont.render("Oui", 1, WHITE)
        screen.blit(quitter, (425, 312))
        non = moyfont.render("Non", 1, WHITE)
        screen.blit(non, (615, 312))

    def wallE(self):
        img = pygame.transform.scale(pygame.image.load(main_path+"images/wallE.png"), (400, 200))
        img = pygame.transform.rotate(img, self.wallE_rotation)
        screen.blit(img, (self.wallE_x, self.walle_y))
        self.wallE_x -= 2
        self.wallE_rotation += 1
    
        pass


# class sons():

#     def __init__(self) -> None:
#         pygame.mixer.init()
        
#     def lecture(self):
#         sound = pygame.mixer.Sound(main_path+"musique/musiques.mp3")
#         pygame.mixer.Sound.play(sound)

#     def pause(self):
#         pygame.mixer.music.pause()

class Gestion_Planete:

    def __init__(self, mass_center: tuple[int, int]) -> None :

        # Définition des planètes : 
        # [PLanète(perigee, apogee) date perigee, periode orbitale]
        self.mercury = [kp.Planete(0.3057031448888919, 0.4679396067760938, center_of_mass=mass_center), 2459596.5, 88]
        self.venus   = [kp.Planete(0.7096386091312117, 0.7367989519021444, center_of_mass=mass_center), 2459617.5, 225]
        self.terre   = [kp.Planete(0.9768982680888847, 1.0219486233072168, center_of_mass=mass_center), 2459601.5, 365.25]
        self.mars    = [kp.Planete(1.3902879805270787, 1.6584426592108024, center_of_mass=mass_center), 2459750.5, 687]
        self.jupiter = [kp.Planete(4.959802763801945,  5.454708507664392,  center_of_mass=mass_center), 2459969.5, 4380]
        self.saturne = [kp.Planete(9.014757970057712,  10.044693667002363, center_of_mass=mass_center), 2463555.5, 10585]

        self.planetes = [self.mercury, self.venus, self.terre, self.mars, self.jupiter, self.saturne]

        # Ajout d'un dernier argument : La planète est-elle suivie par la caméra ?
        #                               Sa position
        #                               Sa taille (relative au zoom)
        #                               Les coordonnées à ajouter à la caméra pour suivre la planête
        self.data_index = len(self.planetes[0]) # Index de cet argument
        for planete in self.planetes:
            planete.append([False, (0, 0), 0, (0, 0)]) # Argument ajouté

<<<<<<< HEAD
<<<<<<< HEAD
    def draw_planet(self, date: int, planete: list, camera_zoom: float, camera_pos: List, sun_pos: List, vitesse: int=30) -> None:
=======
    def draw_planet(self, date: int, planete: list, camera_zoom: float, camera_pos: list[float, float], sun_pos: list[int, int], vitesse: int=30) -> None:
>>>>>>> parent of d38b6ca (Update interface.py)
=======
    def draw_planet(self, date: int, planete: list, camera_zoom: float, camera_pos: list[float, float], sun_pos: list[int, int], vitesse: int=30) -> None:
>>>>>>> parent of d38b6ca (Update interface.py)
        '''Permet de dessiner une planète au bon endroit'''
        time_to_calc = date - planete[1] # Calcul de la date (depuis un temps donné permettant de faciliter la création de ce système solaire)
        pos = planete[0].calculate_point_from_time(time_to_calc/planete[2]) # Calcul de la position
        # Ci-dessous, ajustement de la position et de la taille
        pos_final = (int(sun_pos[0] + (pos[0] - sun_pos[0]) * camera_zoom*3000 + (sun_pos[0] - camera_pos[0]) * camera_zoom), int(sun_pos[1] + (pos[1] - sun_pos[1]) * camera_zoom*3000 + (sun_pos[1] - camera_pos[1]) * camera_zoom))
        time_to_calc_next = time_to_calc + vitesse # On "prédit" le temps de la frame suivante
        pos_next = planete[0].calculate_point_from_time(time_to_calc_next/planete[2]) # Nouvelle position
        pos_alt = (sun_pos[0] + (pos_next[0] - sun_pos[0]) * camera_zoom*3000 + (sun_pos[0] - camera_pos[0]) * (camera_zoom-1), sun_pos[1] + (pos_next[1] - sun_pos[1]) * camera_zoom*3000 + (sun_pos[1] - camera_pos[1]) * (camera_zoom-1))
        size = int(60*camera_zoom+1)
        # Affichage de la planète
        pygame.draw.circle(screen, WHITE, pos_final, size)
        # On garde en mémoire la position et la taille (apparente) de la planète
        planete[self.data_index] = [planete[self.data_index][0], pos_final, size, pos_alt]

<<<<<<< HEAD
<<<<<<< HEAD
    def draw_all_planets(self, date: int, camera_zoom: float, camera_pos: List, sun_pos: List) -> None:
=======
    def draw_all_planets(self, date: int, camera_zoom: float, camera_pos: list[float, float], sun_pos: list[int, int]) -> None:
>>>>>>> parent of d38b6ca (Update interface.py)
=======
    def draw_all_planets(self, date: int, camera_zoom: float, camera_pos: list[float, float], sun_pos: list[int, int]) -> None:
>>>>>>> parent of d38b6ca (Update interface.py)
        '''Dessine toutes les planètes'''
        for planete in self.planetes:
            self.draw_planet(date, planete, camera_zoom, camera_pos, sun_pos)
    
    def get_followed_pos(self) -> tuple[float, float]:
        '''Permet de récupérer les coordonnées de la planète suivie'''
        for planete in self.planetes:
            if planete[self.data_index][0]:
                return planete[self.data_index][3]
        return (0, 0) # Cas où aucune planète n'est suivie
    
    def follow(self) -> tuple:
        '''Permet de commencer à suivre une planète'''
        mouse = pygame.mouse.get_pos()
        for planete in self.planetes:
            if ((mouse[0]-planete[self.data_index][1][0])**2 + (mouse[1]-planete[self.data_index][1][1])**2)**0.5 <= planete[self.data_index][2]:
                planete[self.data_index][0] = True
                return True, planete[self.data_index][3]
        return False, (0, 0)
    
    def unfollow_all(self) -> None:
        '''Permet d'arrêter de suivre toutes les planêtes'''
        for planete in self.planetes:
            planete[self.data_index][0] = False



def main() -> None:

    HUD = ecran()
    data = False
    jouer = True
    validquit = False
    appel = "C"
    # SON = sons()
    can_press_button = True
    wallE = False

    sunpos = (int(width/2), int(height/2))

    #moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)
    planetes = Gestion_Planete(sunpos)

    temps = Temps.JJ(2022, 3, 30)
    base_vitesse = 30 # Jours par secondes
    frame_time = time() # Permet d'évaluer les fps de l'ordi afin d'adapter la vitesse
    vitesse = base_vitesse
    
    camera_zoom = 1 # Facteur de zoom sur la simulation
    camera_true_pos = list(sunpos) # Position théorique de la caméra
    camera_focus = (0, 0) # Postion de l'objet à suivre
    is_following = False # Permet de savoir si la caméra suit une planète
    camera_pos = list(sunpos) # Position finale de la caméra
    # SON.lecture()

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

                # Affichage ou non des informations sur la planête
                if event.key == pygame.K_z:
                    data = not data

                # Pause ou marche
                if event.key == pygame.K_SPACE:
                    jouer = not jouer

                if event.key == pygame.K_q:
                    vitesse /= 2
                    
                if event.key == pygame.K_s:
                    vitesse = base_vitesse

                if event.key == pygame.K_d:
                    vitesse *= 2
                
                if event.key == pygame.K_w:
                    wallE = not wallE
                    
                
                # On arrète de suivre la planète
                if event.key == pygame.K_BACKSPACE:
                    planetes.unfollow_all()
                    camera_true_pos = list(camera_pos)
                    camera_focus = [0, 0]
                    is_following = False

        # Actions à faire tant que la touche est pressée
        pressed = pygame.key.get_pressed()
        # Déplacement vers le haut
        if pressed[pygame.K_UP]:
            camera_true_pos[1] -= 1/camera_zoom
            #moon.compute_orbit_path(camera_zoom, camera_pos)
        # Déplacement vers le bas
        if pressed[pygame.K_DOWN]:
            camera_true_pos[1] += 1/camera_zoom
            #moon.compute_orbit_path(camera_zoom, camera_pos)
        # Déplacement vers la gauche
        if pressed[pygame.K_LEFT]:
            camera_true_pos[0] -= 1/camera_zoom
            #moon.compute_orbit_path(camera_zoom, camera_pos)
        # Déplacement vers la droite
        if pressed[pygame.K_RIGHT]:
            camera_true_pos[0] += 1/camera_zoom
            #moon.compute_orbit_path(camera_zoom, camera_pos)
        

        # Actualisation de la position finale de la caméra
        if is_following:
            camera_focus = planetes.get_followed_pos()
            data = True
        
        camera_pos = (camera_true_pos[0] + camera_focus[0], camera_true_pos[1] + camera_focus[1])


        # Calcul de la position de la planète low-cost
        #moon_pos = moon.calculate_point_from_time(temps)

        # Formule simplifiée utilisé pour le zoom :
        # centre_ecran + (pos_initialle - pos_camera) * zoom_camera

        # Formule complète :
        # Etape 1 (effet de zoom sur les objets)   ->   centre_ecran + (pos_initialle - centre_ecran) * zoom_camera
        # Etape 2 (repositionnement de la caméra)   ->   (centre_ecran - pos_camera) * zoom_camera
        # Position finale = Etape 1 + Etape 2

        # on fait apparaitre les différents astres
        #pygame.draw.circle(screen, WHITE, [int(sunpos[0] + (moon_pos[0] - camera_pos[0]) * camera_zoom), int(sunpos[1] + (moon_pos[1] - camera_pos[1]) * camera_zoom)], 15*camera_zoom) # Astre random sorti de mon imaginaire
        planetes.draw_all_planets(temps, camera_zoom, camera_pos, sunpos)
        pygame.draw.circle(screen, YELLOW, [int(sunpos[0] + (sunpos[0] - camera_pos[0]) * camera_zoom), int(sunpos[1] + (sunpos[1] - camera_pos[1]) * camera_zoom)], 150*camera_zoom+1) # Soleil
        #for point in moon.orbit_path :
            #screen.set_at((int(point[0]), int(point[1])), WHITE)
            # print(int(point[0]), int(point[1]))

        #mise en place des éléments de l'interface
        
        if wallE == True:
            HUD.wallE()
        if data == True:
            HUD.espace_donnee()
            HUD.ecriture(appel)
        HUD.barre_action()
        HUD.play_pause_date()
        HUD.vitesse_lecture(vitesse)
        HUD.display_bouton_pause(jouer)
        HUD.zoom_slider()

        

        if jouer:
            temps, frame_time = update_time(temps, vitesse, frame_time) # Permet de finaliser l'acutalisation du temps
        else:
            temps, frame_time = update_time(temps, 0, frame_time) # Permet d'avoir un semblant de pause


        # Ci-dessous tous les boutons cliquables

        # Lors du clique de la souris
        if can_press_button and pygame.mouse.get_pressed()[0]:

            can_press_button = False # Permet d'éviter de cliquer plusieurs fois sans le vouloir

            # Récupération coordonnées souris
            pos_souris = pygame.mouse.get_pos()

            # Permet de detecter le clic de la souris

            '''Bouton vitesse lente change en fonction de la vitesse actuelle'''
            if pos_souris[0] > 800 and pos_souris[0] < 890 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == base_vitesse/2 :
                    vitesse = base_vitesse
                else:
                    vitesse = base_vitesse/2

            '''Bouton vitesse rapide change en fonction de la vitesse actuelle'''
            if pos_souris[0] > 990 and pos_souris[0] < 1080 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == base_vitesse*2 :
                    vitesse = base_vitesse
                else:
                    vitesse = base_vitesse*2

            '''Bouton play/pause change en fonction du mode actuelle'''
            if pos_souris[0] > 890 and pos_souris[0] < 990 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if jouer == True:
                    jouer = False
                else:
                    jouer = not jouer

            '''Bouton quitter'''
            # Vérifie si souris sur le boton et quitte appli si clique dans la zone
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 550 and pos_souris[1] < 600:
                validquit = True

            # Si message pour quitter actif
            if validquit:
                # Si  quitter
                if pos_souris[0] > 400 and pos_souris[0] < 500 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    pygame.quit()
                    sys.exit()
                # Si annuler
                elif pos_souris[0] > 600 and pos_souris[0] < 700 and pos_souris[1] > 300 and pos_souris[1] < 350:
                    validquit = not validquit

            '''Bouton menu'''
            # Vérifie si souris sur le bouton et retourne au menu principal si clique dans la zone
            if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 0 and pos_souris[1] < 50:
                launch.main()

            '''Sélection de planète à suivre'''
            if not is_following:
                is_following, camera_focus = planetes.follow()
                if is_following:
                    camera_true_pos = [0, 0]
        
        elif not pygame.mouse.get_pressed()[0]:
            can_press_button = True

        # Si message pour quitter actif
        if validquit:
            HUD.confirmation() # Permet d'afficher le message de confirmation

                

        pygame.display.flip() # Affichage final

if __name__ == '__main__':
    main()