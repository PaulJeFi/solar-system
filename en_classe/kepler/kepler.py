import math

def Kepler (e: float, M: float) -> float :
    '''Résout l'équation de Kepler.'''
    E = M
    for i in range(30) : # L'itération peut être modifiée. Plus elle est grande, plus on converge vers la solution.
        E = E + (M + e * math.sin(E) - E) / (1 - e * math.cos(E))
    return E

class Planete :
    def __init__(self, a: float, e: float) -> None :
        '''Créé une planète à partir de son demi-grand axe ```a``` en UA, et de
        ```e```, son exentricité.'''
        assert 0 <= e <= 1 , "L'exentricité doit être comprise entre 0 et 1."
        self.a = a
        self.e = e

        # Calcul de la distance foyer-centre et du demi-petit axe.
        self.c = self.a * self.e
        self.b = self.a * ( (1 - self.e**2) ** (1/2) )

        # Calcul de la période (en jours).
        self.T = ( (self.a**3) ** (1/2) ) * 365.25

    def get_polar_coords(self, tps: float) -> list :
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

if __name__ == '__main__' :
    planete = Planete(2, 0.7)
    print(f'Demi-grand axe : {planete.a}\nPériode : {planete.T}\nDistance focale : {planete.c}\nDemi-petit axe : {planete.b}')
    coords = planete.get_polar_coords(1)
    print(f"\nAprès 1 jour :\n\tDistance à l'étoile : {coords[0]}\n\tAngle sur l'orbite : {coords[1]}")
    print(Kepler(0.5, 0.3))