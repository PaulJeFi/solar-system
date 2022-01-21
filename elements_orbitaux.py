import temps
from table import planetes

'''
Les éléments orbitaux sont :

L = longitude moyenne de la planète
a = demi-grand axe de l'orbite
e = exentricité de l'orbite
i = inclinaison sur le plan de l'écliptique
Ω = longitude du nœud ascendant
π = longitude du périphélie
'''

def polynomial (T: float) :
    '''Retourne la fonction polynomiale des éléments orbitaux en fonction du temps donné.'''

    def element (a0: float, a1: float, a2: float, a3: float) -> float :
        return a0 + a1 * T + a2 * T**2 * a3 * T**3
    
    return element

def get_orbitals_elements (planet: str, Y: int, M: int, D: float) -> list :
    '''Retourne les élements orbitaux (L, a, e, i, Ω, π) de la planète choisie.'''

    # TODO :
    # - implémenter la Terre
    # Implémenter M = L - π et ω = π - Ω

    elements = [0]*6 # Les éléments oribitaux
    elements_names = ["L", "a", "e", "i", "omega", "pi"]

    T = temps.siecles_juliens_epoch(temps.JJ(Y, M, D))
    poly = polynomial(T)

    if planet == 'terre' :
        pass
    else :
        planete = planetes[planet]

        for element in range(6) : # on va itérer les éléments un à un avec le même code
            a0, a1, a2, a3 = planete[elements_names[element]]
            elements[element] = poly(a0, a1, a2, a3)

    return elements