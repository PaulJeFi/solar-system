import math

orbit_resolution = 100

# On utilise la méthode de Newton pour résoudre l'équation de Kepler.
def kepler_equation(E: float, M: float, e:float) -> float:
    return M - E + e * math.sin(E)

def solve(func: function, initial_guess: float=0, max_iterations: float=100) -> float :
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
    def __init__(self, periapsis, apoapsis,  center_of_mass: list=[0, 0]) -> None :

        
        self.center_of_mass = center_of_mass
        self.periapsis = periapsis # périgée
        self.apoapsis = apoapsis # apogée

        self.compute_data()
        self.compute_orbit_path()


    def compute_data(self) -> None :

        self.semi_major_axis = (self.perigee + self.apogee) / 2
        self.linear_eccentricity = self.semi_major_axis - self.perigee # distance focale
        self.eccentricity = self.linear_eccentricity / self.semi_major_axis # exentricité
        self.semi_minor_axis = math.sqrt( (self.semi_major_axis ** 2) - (self.linear_eccentricity ** 2) )
        self.ellipse_centre_X = self.center_of_mass[0] - self.linear_eccentricity
        self.ellipse_centre_Y = self.center_of_mass[1]

    def compute_orbit_path(self) -> None :
        self.orbit_path = []

        for i in range(orbit_resolution) :
            angle = (i / (orbit_resolution - 1)) * math.pi * 2
            px = math.cos(angle) * self.semi_major_axis + self.ellipse_centre_X
            py = math.sin(angle) * self.semi_minor_axis + self.ellipse_centre_Y # dans la vidéo, il utilise ellipse_centre_x ?
            self.orbit_path.append([px, py])

    def calculate_point_from_time(self, t: float) -> list :

        # Angle du corps si l'orbit était circulaire
        mean_anomaly = t * math.pi * 2
        # Résoudre l'anomalie eccentrique (angle du corps dans son orbite elliptique)
        eccentric_anomaly = solve_kepler(mean_anomaly, self.eccentricity)

        # Calculer les coordonnées cartésiennes
        point_x = math.cos(eccentric_anomaly) * self.semi_major_axis + self.ellipse_centre_X
        point_y = math.sin(eccentric_anomaly) * self.semi_minor_axis + self.ellipse_centre_Y

        return [point_x, point_y]
