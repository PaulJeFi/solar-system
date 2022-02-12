import temps
from table import planetes

'''
Les éléments orbitaux sont :

L = longitude moyenne de la planète          (en °)
a = demi-grand axe de l'orbite               (en UA)
e = exentricité de l'orbite
i = inclinaison sur le plan de l'écliptique  (en °)
Ω = longitude du nœud ascendant              (en °)
π = longitude du périphélie                  (en °)

M = L - π l'anomalie moyenne de la planète
ω = π - Ω
'''

def polynomial (T: float) :
    '''Retourne la fonction polynomiale des éléments orbitaux en fonction du temps donné.'''

    def element (a0: float, a1: float, a2: float, a3: float) -> float :
        return a0 + a1 * T + a2 * T**2 * a3 * T**3
    
    return element

def get_orbitals_elements (planet: str, Y: int, Month: int, D: float) -> list :
    '''Retourne les élements orbitaux (L, a, e, i, Ω, π, M, ω) de la planète choisie.'''

    elements = [0]*6 # Les éléments oribitaux
    elements_names = ["L", "a", "e", "i", "omega", "pi"]

    T = temps.siecles_juliens_epoch(temps.JJ(Y, Month, D))
    poly = polynomial(T)

    planete = planetes[planet]

    for element in range(6) : # on va itérer les éléments un à un avec le même code
        a0, a1, a2, a3 = planete[elements_names[element]]
        elements[element] = poly(a0, a1, a2, a3)

    M = elements[0] - elements[5]
    mini_omega = elements[5] - elements[4]
    elements.append(M)
    elements.append(mini_omega)

    return elements