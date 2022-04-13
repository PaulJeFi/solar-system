from math import floor

# Notes sur le temps :
#
#  - En France, le calendrier utilisé est le Grégorien.
#    Les conversions se baseront donc sur des dates Grégoriennes.
# 
#  - On trouce le nombre de jours entre deux dates du calendrier en calculant la 
#    différence entre les Jours Juliens correspondants.

def JJ (Y: int, M: int, D: float) -> float :
    '''Retourne une date Y/M/D grégorienne en temps Jour Julien.'''

    if M <= 2 :
        Y -= 1
        M += 12

    if (Y < 1582) or (Y == 1582 and M < 10) or (Y == 1582 and M == 10 and D < 15) :
        # Car le calendrier Grégorien commence le 15 oct 1582
        B = 0
    else :
        A = floor(Y/100)
        B = 2 - A + floor(A/4)

    jj = floor( 365.25 * (Y + 4_716) ) + floor( 30.6001 * (M + 1) ) + D + B - 1_524.5

    return jj

def JJ0 (Y: int) -> float :
    '''Retourne le Jour Julien JJ0 d'une année grégorienne.'''

    Y -= 1
    A = floor(Y/100)

    jj0 = floor(365.25 * Y) - A + floor(A/4) + 1_721_424.5

    return jj0

def gregorien (jj: float) -> tuple :
    '''Retourne la date grégorienne d'un Jour Julien. \n Retour (Y, M, D).'''

    jj += 0.5
    Z = floor(jj)
    F = abs(jj) - abs(Z)

    if Z < 2_299_161 :
        A = Z
    else :
        alpha = floor( (Z - 1_867_216.25) / 36_524.25 )
        A = Z + 1 + alpha - floor(alpha/4)
        
    B = A + 1_524
    C = floor( (B - 122.1) / 365.25 )
    D = floor(365.25 * C)
    E = floor( (B - D) / 30.6001 )

    D = B - D - floor(30.6001 * E) + F
    if E < 14 :
        M = E - 1
    elif (E == 14) or (E == 15) :
        M = E - 13
    if M > 2 :
        Y = C - 4_716
    elif (M == 1) or (M == 2) :
        Y = C - 4_715

    return Y, M, D

def jour_semaine (Y: int, M: int, D: float) -> int :
    '''Retourne le jour de la semainde d'un jour grégorien. 1 = lundi,
       2 = mardi, 3 = mercredi, ...'''

    jj = JJ(Y, M, floor(D))
    jj += 1.5

    return jj % 7

def siecles_juliens_epoch (jj: float) -> float :
    '''Renvoie le temps T, mesuré en siècles juliens à partir de l'Epoch'''
    T = (jj - 2_451_545) / 36_525
    return T


def calc_periphelie_aphelie(Y: float, planet: str) -> tuple :
    '''Calcule les dates de passage au périphélie et à l'aphélie d'une planète
       pour une année donnée'''
    
    planetes = {
        'mercure': (2_451_590.257,         87.969_349_63),
        'venus':   (2_451_738.223,        224.700_818_8,      -0.000_000_032_7),
        'terre':   (2_451_547.507,        365.259_635_8,       0.000_000_015_6),
        'mars':    (2_452_195.026,        686.995_785_7,      -0.000_000_118_7),
        'jupiter': (2_455_636.936,      4_332.897_065,         0.000_136_7),
        'saturne': (2_452_830.12,      10_764.216_76,          0.000_827)
    }

    k_planetes = {
        'mercure': 4.15201 * (Y - 2000.12),
        'venus':   1.62549 * (Y - 2000.53),
        'terre':   0.99997 * (Y - 2000.01),
        'mars':    0.53166 * (Y - 2001.78),
        'jupiter': 0.08430 * (Y - 2001.20),
        'saturne': 0.03393 * (Y - 2003.52)
    }

    k = floor(k_planetes[planet.lower()])
    # k entier = périphélie, k entier + 0.5 = aphélie
    
    JJ_periphelie, JJ_aphelie = 0, 0
    for exp, coef in enumerate(planetes[planet.lower()]) :
        JJ_periphelie += coef * (k         ** exp)
        JJ_aphelie    += coef * ((k + 0.5) ** exp)
    
    return JJ_periphelie, JJ_aphelie