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

    if M < 2 :
        Y -= 1
        M += 12

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


    
def phase_lune(Y, M, D):
    '''durée lunaison = 29 j'''
    '''calcule la phase de la lune par la date'''
    date = JJ(Y, M, D)
    datetest =  2451578.5
    tmps = 29.5
    a = datetest - date
    if a < 0:
        a = date - datetest
    print(a)
    a = a % tmps
    print(a)
    if a >= 0 and a <= 3.687 or a > 24.687 and a < 29.5:
        return "nouvelle lune"
    elif a > 3.687 and a <= 10.687:    
        return "1er quartier"
    elif a > 10.687 and a <= 17.687:
        return "pleine lune"
    elif a > 17.687 and a <= 24.687:
        return "dernier quartier"

    else : 
        return "Nous rencontrons actuellement un problème technique"




# print(phase_lune(1995, 6, 13))



#PAUL là y a problème avec tes conversions. je te laisse regarder
print(JJ(2000, 2, 6))
print(gregorien(2451578.5))