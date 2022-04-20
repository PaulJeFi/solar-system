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


    
def phase_lune(Y, M, D):
    '''calcule la phase de la lune par la date'''
    '''durée lunaison = 29 j'''
    date_saisie = JJ(Y, M, D)
    datetest =  2459583.5   # Date de référence    -->  18/01/2022
    tmps = 29.53            # Durrée d'une lunaison
    diff = (date_saisie - datetest)

    modulo = diff % tmps     # Calcule la différence 

    # Utilise cette différence pour déduire phase actuelle de la Lune 
    if modulo >= 0 and modulo <= 3.687 or modulo > 24.687 and modulo < 29.5:
        return "nouvelle lune"
    elif modulo > 3.687 and modulo <= 10.687:    
        return "1er quartier"
    elif modulo > 10.687 and modulo <= 17.687:
        return "pleine lune"
    elif modulo > 17.687 and modulo <= 24.687:
        return "dernier quartier"

    else : 
        return "Nous rencontrons actuellement un problème technique"
    


def astro_fra(Y, M, D):
    '''calcule le signe du zodiac grégorien par la date'''
    # Utilise Le numéro du mois et de l'année 

    if M == 2 and 20 < D < 29 or M == 3 and 1 < D < 20:
        return "L"
    if M == 3 and 21 < D < 31 or M == 4 and 1 < D < 20:
        return "A"
    if M == 4 and 21 < D < 30 or M == 5 and 1 < D < 21:
        return "B" 
    if M == 5 and 22 < D < 31 or M == 6 and 1 < D < 21:
        return "C"
    if M == 6 and 22 < D < 30 or M == 7 and 1 < D < 22:
        return "D"
    if M == 7 and 23 < D < 31 or M == 8 and 1 < D < 22:
        return "E"
    if M == 8 and 23 < D < 31 or M == 9 and 1 < D < 22:
        return "F"
    if M == 9 and 23 < D < 30 or M == 10 and 1 < D < 22:
        return "G"
    if M == 10 and 23 < D < 31 or M == 11 and 1 < D < 22:
        return "H"
    if M == 11 and 23 < D < 30 or M == 12 and 1 < D < 21:
        return "I"
    if M == 12 and 22 < D < 31 or M == 1 and 1 < D < 20:
        return "J"
    if M == 1 and 21 < D < 31 or M == 2 and 1 < D < 19:
        return "K"

    else : 
        return "Nous rencontrons actuellement un problème technique"

def astro_chn(Y, M, D):
    '''calcule le signe astrologique chinois par la date'''

    dif = (Y - 2000) % 12    #calcule la différence par rapport à l'année 2000 (année du dragon)

    # Utilise le numéro de l'année pour en déduire le signe astrologique
    if dif < 0:
        dif = (Y - 2000) % 12
    if dif == 0:
        return "M"  #"Dragon"
    if dif == 1: 
        return "N"  #"Serpent"
    if dif == 2: 
        return "O"  #"Cheval"
    if dif == 3: 
        return "p"  #"Mouton"
    if dif == 4: 
        return "Q"  #"Singe"
    if dif == 5: 
        return "R"  #"Coq"
    if dif == 6: 
        return "S"  #"Chien"
    if dif == 7: 
        return "T"  #"Cochon"
    if dif == 8: 
        return "U"  #"Rat"
    if dif == 9: 
        return "V"  #"Boeuf"
    if dif == 10: 
        return "W"  #"Tigre"
    if dif == 11: 
        return "X"  #"Lièvre"

    else : 
        return "Nous rencontrons actuellement un problème technique"
        