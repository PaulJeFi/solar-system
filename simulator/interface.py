from multiprocessing.sharedctypes import Value
import kepler as kp
import pygame
import sys
from time import time
import launch


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
# pygame.mixer.music.load("./simulator/musique/musique.mp3")
jouer = False

#données palnètes

data = {'A' :['Mercure', 'poids = 3,33 x 10^23 kg', 'rayon = 4200 km', 'distance soleil = 46 à 70 mm km', 'temps de rotation = 87,969 j', 'température moyenne = 462°C', "simulator/images/mercure.png"],
                'B' : ['Venus','poids = 4,867 5x10^24 kg', 'rayon = 6050 km', 'distance soleil = 104 mm km', 'temps de rotation = 243 j', 'température moyenne = 440°C',"simulator/images/venus.png"],
                'C' : ['La Terre','poids = 5,973 x 10^24 kg', 'rayon = 6378 km', 'distance soleil = 150 mm km', 'temps de rotation = 365 j', 'température moyenne = 14°C',"simulator/images/terre.png"],
                'D' : ['Mars', 'poids = 6,418 x 10^23 kg','rayon = 3 396 km', 'distance soleil = 227 mm km', 'temps de rotation = 696 j', 'température moyenne = -60°C',"simulator/images/mars.png"],
                'E' : ['Jupyter', 'poids = 1,89 X 10^17 kg', 'rayon = 71 492 km', 'distance soleil = 778 mm km', 'temps de rotation = 11 ans 315 j', 'température moyenne = -163°C',"simulator/images/jupyter.png"],
                'F' : ['Saturne', 'poids = 5,68 X 10^26 kg', 'rayon = 58 232 km', 'distance soleil = 1,4 md km', 'temps de rotation = 29 ans 167 j', 'température moyenne = -189°C',"simulator/images/saturne.png"],
                'G' : ['Uranus', 'poids = 8,6 X 10^25 kg', 'rayon = 51 118 km','distance soleil = 2,8 md km', 'temps de rotation = 84 ans', 'température moyenne = -218°C',"simulator/images/uranus.png"],
                'H' : ['Neptune', 'poids = 102 X 10^24 kg', 'rayon = 24 764 km', 'distance soleil = 4,5 md km', 'temps de rotation = 165 ans', 'température moyenne = -220°C',"simulator/images/neptune.png"],
                'I' : ['Pluton', 'poids = 1,3 X 10^22 kg', 'rayon = 1185 km', 'distance soleil = 6 md km', 'temps de rotation = 248 ans', 'température moyenne = -225°C',"simulator/images/pluton.png"],
                'Z' : ['', '', '', '', '', '',""]}




def update_time(temps: float, j: float, last_frame: float=time()) -> float:
    '''Permet d'avancer dans le temps'''
    new_frame = time() # Permet de faire avancer le temps non pas en fonction des FPS mais du temps réel
    return temps + (j/365.25)*(new_frame-last_frame), new_frame


class ecran():

    def __init__(self) -> None:
        # Paramètres du bouton pause
        self.bouton_pause_pos = (915, 503) # Position du bouton pause
        self.bouton_pause_size = (50, 43) # Dimensions du bouton pause
        self.bouton_pause_images = { # Sprites du bouton pause
                                    "play": pygame.transform.scale(pygame.image.load("simulator/images/play.png"), self.bouton_pause_size),
                                    "pause": pygame.transform.scale(pygame.image.load("simulator/images/pause.png"), self.bouton_pause_size)}
        # Paramètres des boutons de vitesse de lecture
        self.bouton_vitesse_lecture_pos = (820, 502)
        self.bouton_vitesse_lecture_size = (50, 45)
        self.bouton_vitesse_lecture2_pos = (1012, 503)
        self.bouton_vitesse_lecture_image = {"normal": pygame.transform.scale(pygame.image.load("./simulator/images/vitesselecture.png"), self.bouton_vitesse_lecture_size),
                                             "rapide": pygame.transform.scale(pygame.image.load("./simulator/images/vitessecours.png"), self.bouton_vitesse_lecture_size),
                                             "lent": pygame.transform.scale(pygame.image.load("./simulator/images/vitesselecture.png"), self.bouton_vitesse_lecture_size),
                                             "normal2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load("./simulator/images/vitesselecture.png"), 180), self.bouton_vitesse_lecture_size),
                                             "rapide2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load("./simulator/images/vitesselecture.png"), 180), self.bouton_vitesse_lecture_size),
                                             "lent2": pygame.transform.scale(pygame.transform.rotate(pygame.image.load("./simulator/images/vitessecours.png"), 180), self.bouton_vitesse_lecture_size)}
        # Paramètres du slider pour le zoom
        self.zoom_slider_pos = (500, 550) # Position du background du slider (le boutton est placé en conséquance)
        self.zoom_slider_size_factor = 2.5 # Facteur de taille
        self.zoom_slider_size = { # Les tailles des éléments (ne pas toucher ces valeurs, modifiez celle au-dessus)
                                'background': (120*self.zoom_slider_size_factor, 20*self.zoom_slider_size_factor),
                                'button': (4*self.zoom_slider_size_factor, 10*self.zoom_slider_size_factor)}
        self.zoom_slider_images = { # Les images utilisées pour le slider
                                    'background': pygame.transform.scale(pygame.image.load("./simulator/images/zoom_slider_bg.png"), self.zoom_slider_size['background']),
                                    'button': pygame.transform.scale(pygame.image.load("./simulator/images/zoom_slider_button.png"), self.zoom_slider_size['button'])}
        self.zoom_slider_x_range = (self.zoom_slider_pos[0]+19*self.zoom_slider_size_factor, self.zoom_slider_pos[0]+98*self.zoom_slider_size_factor) # Entre quelles coordonnées y le bouton slider peut se situer
        self.zoom_slider_current_x_pos = (self.zoom_slider_x_range[0]+self.zoom_slider_x_range[1])/2 # Possition x actuelle du bouton du slider
        self.zoom_slider_clicked = False # Permet de savoir si le curseur "tient" le bouton pour le faire slider
        self.zoom_factor = 1 # Facteur de zoom de la simulation

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
        pygame.draw.line(screen, WHITE, (499, 551), (1080, 551), 3)#ligne de séparation
        pygame.draw.line(screen, WHITE, (499, 550), (499, 600), 3)#ligne de séparation
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
        if pygame.mouse.get_pressed()[0] and self.zoom_slider_current_x_pos <= mouse[0] <= self.zoom_slider_current_x_pos+4*self.zoom_slider_size_factor and self.zoom_slider_pos[1]+5*self.zoom_slider_size_factor <= mouse[1] <= self.zoom_slider_pos[1]+15*self.zoom_slider_size_factor and not self.zoom_slider_clicked:
            self.zoom_slider_clicked = True
        # Si l'utilisateur arrète de cliquer (donc "lache" le bouton) :
        elif not pygame.mouse.get_pressed()[0]:
            self.zoom_slider_clicked = False
        # PS : pygame.mouse.get_pressed() = Bouton de la souris pressés ? -> (LMB, MMB, RMB) avec dans chacun des emplacement un boolean

        '''Partie déplacement'''
        mouse_x = mouse[0] - self.zoom_slider_size_factor*2 # Ajustement automatique
        if self.zoom_slider_clicked:
            # Le bouton doit rester dans les limites du slider
            if mouse_x < self.zoom_slider_x_range[0]:
                self.zoom_slider_current_x_pos = self.zoom_slider_x_range[0]
            elif mouse_x > self.zoom_slider_x_range[1]:
                self.zoom_slider_current_x_pos = self.zoom_slider_x_range[1]
            else:
                self.zoom_slider_current_x_pos = mouse_x
        
        '''Partie affichage'''
        screen.blit(self.zoom_slider_images['background'], self.zoom_slider_pos)
        screen.blit(self.zoom_slider_images['button'], (self.zoom_slider_current_x_pos, self.zoom_slider_pos[1] + 5*self.zoom_slider_size_factor))

        '''Partie utilitaire'''
        self.zoom_factor = 3**((self.zoom_slider_current_x_pos-(self.zoom_slider_x_range[0]+self.zoom_slider_x_range[1])/2)/self.zoom_slider_size_factor/10)

    def barre_action(self) -> None:
        '''Créer une barre sur la gauche pour ajouter boutons et actions'''
        # pygame.draw.rect(screen, OR_STP, ((44, 0), (45, 600)))
        pygame.draw.rect(screen, BLEU_STP, ((0, 0), (50, 600)))
        pygame.draw.rect(screen, OR_STP, ((0, 120), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 270), (50, 50)))
        pygame.draw.rect(screen, OR_STP, ((0, 420), (50, 50)))
        pygame.draw.rect(screen, RED, ((0, 550),(50, 50)))

        """"bouton menu"""
        pygame.draw.rect(screen, GRAY, ((0, 0), (50, 50)))
        pygame.draw.line(screen, WHITE, (10, 12),(40, 12), 3)
        pygame.draw.line(screen, WHITE, (10, 25),(40, 25), 3)
        pygame.draw.line(screen, WHITE, (10, 38),(40, 38), 3)
        
        """bouton quitter"""
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

    def confirmation(self):
        """desine écran validation quitter"""
        pygame.draw.rect(screen, GRAY, ((340, 200),(400, 200)), 0, 5)
        pygame.draw.rect(screen, GREEN_CUSTOM, ((400, 300),(100, 50)), 0, 10)
        pygame.draw.rect(screen, RED, ((590, 300),(100, 50)), 0, 10)
        sur = moyfont.render("Sûr de vouloir quitter ?", 1, OR_STP)
        screen.blit(sur, (387, 233))
        quitter = moyfont.render("Oui", 1, WHITE)
        screen.blit(quitter, (425, 312))
        non = moyfont.render("Non", 1, WHITE)
        screen.blit(non, (615, 312))


# class sons():

#     def __init__(self) -> None:
#         pygame.mixer.init()
        
#     def lecture(self):
#         pygame.mixer.music.play()

#     def pause(self):
#         pygame.mixer.music.pause()

class Gestion_Planete :
    def __init__(self, mass_center) :
        self.mercury = [kp.Planete(0.3057031448888919, 0.4679396067760938, center_of_mass=mass_center), 0.7096386091312117]
        self.venus = [kp.Planete(0.7096386091312117, 0.7367989519021444, center_of_mass=mass_center), 2459617.5]

        self.planetes = [self.mercury, self.venus]

    def draw_planet(self, date, planete, zoom_factor, sun_pos) :
        time_to_calc = date - planete[1]
        pos = planete[0].calculate_point_from_time(time_to_calc)
        pygame.draw.circle(screen, WHITE, [20 * int(pos[0] + (pos[0]-sun_pos[0])*(zoom_factor-1)), 20 * int(pos[1] + (pos[1]-sun_pos[1])*(zoom_factor-1))], 15*zoom_factor)

    def draw_all_planets(self, date, zoom_factor, sun_pos) :
        for planete in self.planetes :
            self.draw_planet(date, planete, zoom_factor, sun_pos)

def main() -> None:
    
    HUD = ecran()
    data = False
    jouer = True
    validquit = False
    # SON = sons()

    sunpos = (int(width/2), int(height/2))

    moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)
    planetes = Gestion_Planete(sunpos)

    temps = 1
    vitesse = 30 # Jours par secondes
    frame_time = time() # Permet d'évaluer les fps de l'ordi afin d'adapter la vitesse
    
    camera_zoom = 1 # Facteur de zoom sur la simulation
    camera_pos = list(sunpos) # Position de la caméra

    while True:
        
        dt = clock.tick(144)
        #on creer un fond de couleur noir
        screen.fill(BLACK)

        # Actualisation du zoom
        if camera_zoom != HUD.zoom_factor:
            camera_zoom = HUD.zoom_factor
            moon.compute_orbit_path(camera_zoom, camera_pos)

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
                    vitesse = 15
                    
                if event.key == pygame.K_s:
                    vitesse = 30

                if event.key == pygame.K_d:
                    vitesse = 60

        # Actions à faire tant que la touche est pressée
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            camera_pos[1] -= 0.5/camera_zoom
            moon.compute_orbit_path(camera_zoom, camera_pos)
        if pressed[pygame.K_DOWN]:
            camera_pos[1] += 0.5/camera_zoom
            moon.compute_orbit_path(camera_zoom, camera_pos)
        if pressed[pygame.K_LEFT]:
            camera_pos[0] -= 0.5/camera_zoom
            moon.compute_orbit_path(camera_zoom, camera_pos)
        if pressed[pygame.K_RIGHT]:
            camera_pos[0] += 0.5/camera_zoom
            moon.compute_orbit_path(camera_zoom, camera_pos)


        moon_pos = moon.calculate_point_from_time(temps)

        # Formule utilisé pour le zoom :
        # pos_initialle + (pos_initiale - pos_centre_de_zoom) * facteur de zoom

        # on fait apparaitre les différents astres
        pygame.draw.circle(screen, WHITE, [int(moon_pos[0] + (moon_pos[0] - camera_pos[0]) * camera_zoom), int(moon_pos[1] + (moon_pos[1] - camera_pos[1]) * camera_zoom)], 15*camera_zoom**0.5) # Astre random sorti de mon imaginaire
        planetes.draw_all_planets(temps, camera_zoom, camera_pos)
        pygame.draw.circle(screen, YELLOW, [int(sunpos[0] + (sunpos[0] - camera_pos[0]) * camera_zoom), int(sunpos[1] + (sunpos[1] - camera_pos[1]) * camera_zoom)], 30*camera_zoom**0.5) # Soleil
        for point in moon.orbit_path :
            screen.set_at((int(point[0]), int(point[1])), WHITE)
            # print(int(point[0]), int(point[1]))

        #mise en place des éléments de l'interface
        if data == True:
            HUD.espace_donnee()
            HUD.ecriture("C")
        HUD.vitesse_lecture(vitesse)
        HUD.barre_action()
        HUD.display_bouton_pause(jouer)
        HUD.zoom_slider()
        HUD.play_pause_date()
        # SON.lecture()

        if jouer:
            temps, frame_time = update_time(temps, vitesse, frame_time) # Permet de finaliser l'acutalisation du temps
        else:
            temps, frame_time = update_time(temps, 0, frame_time) # Permet d'avoir un semblant de pause

        """recupération coordonnées souris"""
        pos_souris = pygame.mouse.get_pos()

        """permet de detecter le clic de la souris"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(100)
            """bouton vitesse lente change en fonction de la vitesse actuelle"""
            if pos_souris[0] > 800 and pos_souris[0] < 890 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == 15:
                    vitesse = 30
                else:
                    vitesse = 15
            """bouton vitesse rapide change en fonction de la vitesse actuelle"""
            if pos_souris[0] > 990 and pos_souris[0] < 1080 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if vitesse == 60:
                    vitesse = 30
                else:
                    vitesse = 60
            """bouton play/pause change en fonction du mode actuelle"""
            if pos_souris[0] > 890 and pos_souris[0] < 990 and pos_souris[1] > 502 and pos_souris[1] < 547:
                if jouer == True:
                    jouer = False
                else:
                    jouer = not jouer

        

        """pour bouton quitter"""
        """vérifie si souris sur le boton et quitte appli si clique dans la zone"""
        if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 550 and pos_souris[1] < 600:
            if event.type == pygame.MOUSEBUTTONDOWN:
                validquit = True
                

        if validquit == True:
            """permet d'afficher le message de confirmation"""
            HUD.confirmation()
            """si  quitter"""
            if pos_souris[0] > 400 and pos_souris[0] < 500 and pos_souris[1] > 300 and pos_souris[1] < 350:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
                """si annuler"""
            elif pos_souris[0] > 600 and pos_souris[0] < 700 and pos_souris[1] > 300 and pos_souris[1] < 350:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    validquit = not validquit

        """pour bouton quitter"""
        """vérifie si souris sur le boton et quitte appli si clique dans la zone"""
        if pos_souris[0] > 0 and pos_souris[0] < 50 and pos_souris[1] > 0 and pos_souris[1] < 50:
            if event.type == pygame.MOUSEBUTTONDOWN:
                launch.main()

                

        pygame.display.flip() # Affichage final

if __name__ == '__main__':
    main()