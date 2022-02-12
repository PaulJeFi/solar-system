'''
Script de :
BLANDIN Anatole
DE SAINT LEGER Térence
JEROME--FILIO Paul
'''


# Les imports
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from itertools import count, cycle
import math


# Définition de l'écran
screen_x, screen_y = 1000, 600
center = (screen_x/2, screen_y/2)
screen = tk.Tk()
canvas = tk.Canvas(screen, width=screen_x, height=screen_y)
canvas.pack()
canvas.configure(bg='black')


'''
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
'''

'''
#demo :
root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('soleil.gif')
root.mainloop()
'''

def creer_point(pos, rayon, couleur):
    '''Fonction permettant de créer un point'''
    return canvas.create_oval((pos[0]-rayon,pos[1]-rayon,pos[0]+rayon,pos[1]+rayon), fill=couleur)

def move_point(old_pos, new_pos):
    return new_pos[0]-old_pos[0], new_pos[1]-old_pos[1] 

def get_screen_center():
    return screen.winfo_width()/2, screen.winfo_height()/2


def JJ (Y: int, M: int, D: float) -> float :
    '''Retourne une date Y/M/D grégorienne en temps Jour Julien.'''

    if M < 2 :
        Y -= 1
        M += 12

    A = math.floor(Y/100)
    B = 2 - A + math.floor(A/4)

    jj = math.floor( 365.25 * (Y + 4_716) ) + math.floor( 30.6001 * (M + 1) ) + D + B - 1_524.5

    return jj

def gregorien (jj: float) -> tuple :
    '''Retourne la date grégorienne d'un Jour Julien. \n Retour (Y, M, D).'''

    jj += 0.5
    Z = math.floor(jj)
    F = abs(jj) - abs(Z)

    if Z < 2_299_161 :
        A = Z
    else :
        alpha = math.floor( (Z - 1_867_216.25) / 36_524.25 )
        A = Z + 1 + alpha - math.floor(alpha/4)
        
    B = A + 1_524
    C = math.floor( (B - 122.1) / 365.25 )
    D = math.floor(365.25 * C)
    E = math.floor( (B - D) / 30.6001 )

    D = B - D - math.floor(30.6001 * E) + F
    if E < 14 :
        M = E - 1
    elif (E == 14) or (E == 15) :
        M = E - 13
    if M > 2 :
        Y = C - 4_716
    elif (M == 1) or (M == 2) :
        Y = C - 4_715

    return Y, M, D

'''
def coords(T) :
    return 2 * math.cos(T), 3 * math.sin(T)


def get_coords_from_date(Y, M, D) :
    jj = JJ(Y, M, D)
    coord = coords(jj)
    return coord
'''

'''
class planete :
    def __init__(self, Y, M, D) :
        self.date = (Y, M, D)
        self.coords = get_coords_from_date(*self.date)
        self.coords = (self.coords[0]*100+center[0], self.coords[1]*100+center[1])
        self.old_coords = self.coords
        self.image = creer_point(self.coords, 10, 'white')
    
    def increment(self) :
        self.date = gregorien(JJ(*self.date)+1)
        self.update()
        
    def update(self) :
        self.coords = get_coords_from_date(*self.date)
        self.coords = (self.coords[0]*100+center[0], self.coords[1]*100+center[1])
        self.move()
        self.old_coords = self.coords
        
    def move(self) :
        canvas.move(self.image, *move_point(self.old_coords, self.coords))
        
    def set_date(self, Y, M, D) :
        self.date = (Y, M, D)
        self.update
'''


def Kepler (e: float, M: float) -> float :
    '''Résout l'équation de Kepler.'''
    E = M
    for i in range(30) : # L'itération peut être modifiée. Plus elle est grande, plus on converge vers la solution.
        E = E + (M + e * math.sin(E) - E) / (1 - e * math.cos(E))
    return E


def cartesien(rho: float, theta: float) -> tuple :
    return (rho * math.cos(theta), rho * math.sin(theta))

class Planete :
    def __init__(self, a: float, e: float) -> None :
        '''Créé une planète à partir de son demi-grand axe ```a``` en UA, et de
        ```e```, son exentricité.'''
        assert 0 <= e <= 1 , "L'exentricité doit être comprise entre 0 et 1."
        self.a = a # Demi_grand axe
        self.e = e # Exentricité

        # Calcul de la distance foyer-centre et du demi-petit axe.
        self.c = self.a * self.e # Distance focale
        self.b = self.a * ( (1 - self.e**2) ** (1/2) ) # Demi-petit axe

        # Calcul de la période (en jours).
        self.T = ( (self.a**3) ** (1/2) ) * 365.25 # Période
        
        temp_coord = cartesien(*self.get_polar_cords(1))
        self.old_coords = (temp_coord[0]+self.c - self.a, temp_coord[1])
        self.coords = (1, 4) # Pour les noobs !
        self.image = creer_point(self.coords, 10, 'white')

    def get_polar_cords(self, tps: float) -> list :
        '''Retourne les coordonnées polaires de la planète au temps ```tps``` en
        jours.'''

        # Calcul de l'anomalie moyenne
        M = math.pi/self.T * tps

        # Calcul de l'anomalie exentrique et de l'angle de la position de la planète sur son orbite.
        u = Kepler(self.e, M)
        theta = 2 * math.atan( math.tan(u/2) * math.sqrt((1 + self.e)/(1 - self.e)) )

        # Longueur du rayon vecteur
        rho = self.a * (1 - self.e**2) / (1 + self.e * math.cos(theta))

        return [rho, theta]
    
    def move(self) :
        canvas.move(self.image, *move_point(self.old_coords, self.coords))
    
    def update(self, time_interval: float) -> tuple :
        self.move()
        self.old_coords = self.coords
        self.coords = cartesien(*self.get_polar_cords(time_interval))
        self.coords = [self.coords[0]+center[0]+self.c, self.coords[1]+center[1]]
        return self.coords


exentricite =  0.9
demi_grand_axe = 200
pla = Planete(demi_grand_axe, exentricite)


# Création des points
soleil = creer_point(center, 30, 'yellow')

start_time = 0
# Boucle principale
while True:
    start_time += 10
    # Affichage final
    canvas.update()
    pla.update(start_time)
    center = get_screen_center()