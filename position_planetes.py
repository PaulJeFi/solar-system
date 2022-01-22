import elements_orbitaux
import VSOP87
import temps
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

def get_by_VSOP87 (planet: str, Y: int, M: int, D: float) :
    '''Retourne les coordonnées héliocentriques précises d'une planète à une
    date donnée, en utilisant la théorie VSOP87.'''

    # Première étape : selection de la planète.
    planet = planet.lower()
    planete = VSOP87.planets[planet]

    # Deuxième étape, calcul de τ (tau), mesuré en milliers d'années juliennes depuis J 2000.
    jj = temps.JJ(Y, M, D)
    tau = (jj - 2_451_545.0) / 365_250

    # Troisième étape : calcul de la somme des A • cos(B + C•τ) de la liste.
    for type_liste_index in range(len(planete)) :
        for liste_index in range(len(planete[type_liste_index])) :
            for triplet_index in range(len(planete[type_liste_index][liste_index])) :
                planete[type_liste_index][liste_index][triplet_index] = planete[type_liste_index][liste_index][triplet_index][0] * math.cos(planete[type_liste_index][liste_index][triplet_index][1] + planete[type_liste_index][liste_index][triplet_index][2] * tau)

            planete[type_liste_index][liste_index] = sum(planete[type_liste_index][liste_index])
        
    # Quatrième étape : calcul de la longitude héliocentrique L, de la latitude héliocentrique B, et de la distance planète-barycentre R :
    # E (pour élément) = E0 + E1•τ + E2•τ^2 + E3•τ^3 ...
    L = 0
    B = 0
    R = 0

    # Pour L
    for l in range(len(planete[0])) :
        L += planete[0][l] * (tau ** l)
    # Pour B
    for b in range(len(planete[1])) :
        B += planete[1][b] * (tau ** b)
    # Pour R
    for r in range(len(planete[2])) :
        R += planete[2][r] * (tau ** r)
    
    # Notes de retour : L en radians, B en radians et R en UA
    return L, B, R