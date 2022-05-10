import math

# G = 6.674_30 × 10**-(11) # m3 kg−1 s−2
# On veut convertir G pour que son unité de temps soit le jour, et son unité de distance l'UA.
G = 1.4818517 * 10 ** (-34) # kg^-1 • AU^3 • jour^(-2)

orbit_resolution = 100

# On utilise la méthode de Newton pour résoudre l'équation de Kepler.
def kepler_equation(E: float, M: float, e:float) -> float:
    return M - E + e * math.sin(E)

def solve(func, initial_guess: float=0, max_iterations: float=100) -> float :
    '''Thanks Newton !'''
    h = 0.0001 # taille du pas de l'analyse de la dérivée
    acceptable_error  = 0.00000001
    guess = initial_guess

    for i in range(max_iterations) :
        y = func(guess)
        if abs(y) < acceptable_error : # sortir si on est assez proche de 0
            break
        slope = (func(guess + h) - y) / h
        step = y / slope
        guess -= step
    
    return guess

def solve_kepler(mean_anomaly: float, eccentricity: float, max_iterations: float=100) -> float :
    kep = lambda x : kepler_equation(x, mean_anomaly, eccentricity)
    return solve(kep, initial_guess=mean_anomaly)

class Planete :
    def __init__(self, periapsis, apoapsis,  center_of_mass: list=[0, 0], sum_mass=None, angle=0) -> None :

        
        self.center_of_mass = center_of_mass
        self.periapsis = periapsis # périgée
        self.apoapsis = apoapsis # apogée
        self.angle = angle # angle de périgée formé avec Mercure

        self.compute_data(sum_mass)
        self.compute_orbit_path()


    def compute_data(self, sum_mass) -> None :

        self.semi_major_axis = (self.periapsis + self.apoapsis) / 2
        self.linear_eccentricity = self.semi_major_axis - self.periapsis # distance focale
        self.eccentricity = self.linear_eccentricity / self.semi_major_axis # exentricité
        self.semi_minor_axis = math.sqrt( (self.semi_major_axis ** 2) - (self.linear_eccentricity ** 2) )
        self.ellipse_centre_X = self.center_of_mass[0] - self.linear_eccentricity
        self.ellipse_centre_Y = self.center_of_mass[1]

        # Calcul de la période orbitale
        if sum_mass != None :
            self.orbital_period = math.sqrt( (4 * math.pi * (self.semi_major_axis ** 3)) / (G * sum_mass)) # En jours
        else :
            self.orbital_period = None

    def compute_orbit_path(self, camera_zoom: float=1, camera_pos: tuple=(540, 310), sunpos: tuple=(540, 310)) -> None :
        self.orbit_path = []

        for i in range(orbit_resolution) :
            angle = (i / (orbit_resolution - 1)) * math.pi * 2
            px = math.cos(angle) * self.semi_major_axis + self.ellipse_centre_X
            py = math.sin(angle) * self.semi_minor_axis + self.ellipse_centre_Y # dans la vidéo, il utilise ellipse_centre_x ?
            px = int(sunpos[0] + (px - camera_pos[0]) * camera_zoom) # Ajustements pour le zoom
            py = int(sunpos[1] + (py - camera_pos[1]) * camera_zoom) # Ajustements pour le zoom
            self.orbit_path.append([px, py])

    def calculate_point_from_time(self, t: float) -> list :

        # Il faut modifier le temps !!!
        if self.orbital_period != None :
            t /= self.orbital_period

        # Angle du corps si l'orbit était circulaire
        mean_anomaly = t * math.pi * 2
        # Résoudre l'anomalie eccentrique (angle du corps dans son orbite elliptique)
        eccentric_anomaly = -solve_kepler(mean_anomaly, self.eccentricity)

        # Ajour du décalage
        eccentric_anomaly -= self.angle

        # Calculer les coordonnées cartésiennes
        point_x = math.cos(eccentric_anomaly) * self.semi_major_axis + self.ellipse_centre_X
        point_y = math.sin(eccentric_anomaly) * self.semi_minor_axis + self.ellipse_centre_Y

        return [point_x, point_y]
