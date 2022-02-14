import math

orbit_resolution = 100

class Planete :
    def __init__(self, periapsis, apoapsis,  center_of_mass: list=[0, 0]) -> None :

        
        self.center_of_mass = center_of_mass
        self.periapsis = periapsis # périgée
        self.apoapsis = apoapsis # apogée

        self.compute_data()


    def compute_data(self) :

        self.semi_major_axis = (self.perigee + self.apogee) / 2
        self.linear_eccentricity = self.semi_major_axis - self.perigee # distance focale
        self.eccentricity = self.linear_eccentricity / self.semi_major_axis # exentricité
        self.semi_minor_axis = math.sqrt( (self.semi_major_axis ** 2) - (self.linear_eccentricity ** 2) )
        self.ellipse_centre_X = self.center_of_mass[0] - self.linear_eccentricity
        self.ellipse_centre_Y = self.center_of_mass[1]

    def compute_orbit_path(self) :
        self.orbit_path = []

        for i in range(orbit_resolution) :
            angle = (i / (orbit_resolution - 1)) * math.pi * 2
            px = math.cos(angle) * self.semi_major_axis + self.ellipse_centre_X
            py = math.sin(angle) * self.semi_minor_axis + self.ellipse_centre_Y # dans la vidéo, il utilise ellipse_centre_x ?
            self.orbit_path.append([px, py])

