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

    
def astro_fra(Y, M, D):
    '''calcule le signe du zodiac grégorien par la date'''
    if M == 2 and 20 < D < 29 or M == 3 and 1 < D < 20:
        return "poisson"
    if M == 3 and 21 < D < 31 or M == 4 and 1 < D < 20:
        return "Bélier"
    if M == 4 and 21 < D < 30 or M == 5 and 1 < D < 21:
        return "Taureau" 
    if M == 5 and 22 < D < 31 or M == 6 and 1 < D < 21:
        return "Gémeaux"
    if M == 6 and 22 < D < 30 or M == 7 and 1 < D < 22:
        return "Cancer"
    if M == 7 and 23 < D < 31 or M == 8 and 1 < D < 22:
        return "Lion"
    if M == 8 and 23 < D < 31 or M == 9 and 1 < D < 22:
        return "Vierge"
    if M == 9 and 23 < D < 30 or M == 10 and 1 < D < 22:
        return "Balance"
    if M == 10 and 23 < D < 31 or M == 11 and 1 < D < 22:
        return "Scorpion"
    if M == 11 and 23 < D < 30 or M == 12 and 1 < D < 21:
        return "Sagittaire"
    if M == 12 and 22 < D < 31 or M == 1 and 1 < D < 20:
        return "Capricorne"
    if M == 1 and 21 < D < 31 or M == 2 and 1 < D < 19:
        return "Verseau"

    else : 
        return "Nous rencontrons actuellement un problème technique"

def astro_chn(Y, M, D):
    '''calcule le signe astrologique chinois par la date'''
    dif = (2000 - Y) % 12
    if dif < 0:
        dif = (Y - 2000) % 12
    if dif == 0:
        return "Dragon"
    if dif == 1: 
        return "Serpent"
    if dif == 2: 
        return "Cheval"
    if dif == 3: 
        return "Mouton"
    if dif == 4: 
        return "Singe"
    if dif == 5: 
        return "Coq"
    if dif == 6: 
        return "Chien"
    if dif == 7: 
        return "Porc"
    if dif == 8: 
        return "Rat"
    if dif == 9: 
        return "Boeuf"
    if dif == 10: 
        return "Tigre"
    if dif == 11: 
        return "Lièvre"

    else : 
        return "Nous rencontrons actuellement un problème technique"








#PAUL là y a problème avec tes conversions. je te laisse regarder
print(JJ(2000, 2, 6))
print(gregorien(2451578.5))