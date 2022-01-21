import elements_orbitaux
import math

def Kepler (e: float, M: float) -> float :
    '''Résout l'équation de Kepler.'''
    M = math.radians(M)
    E = M
    for i in range(30) : # L'itération peut être modifiée. Plus elle est grande, plus on converge vers la solution.
        E = E + (M + e * math.sin(E) - E) / (1 - e * math.cos(E))
    M = math.degrees(M)
    E = math.degrees(E)
    return E

def get_position (planet: str, Y: int, Month: int, D: float) :
    '''Retourne les coordonnées héliocentriques d'une planète à une date donnée.'''

    # Première étape, récupérer les éléments orbitaux de la planète.
    L, a, e, i, omega, pi, M, mini_omega = elements_orbitaux.get_orbitals_elements(planet, Y, Month, D)

    # Deuxième étape, trouver l'anomalie excentrique E en résolvant l'équation de Kepler.
    E = Kepler(e, M)

    # Troisième étape, on calcule v l'anomalie vraie et r la distance au Soleil.

    r = a * (1 - e * math.cos(math.radians(E)))