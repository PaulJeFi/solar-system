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


    
# def phase_lune(self, Y, M, D):
#     '''phase de la lune'''
#     '''durée lunaison = 29,53 j'''
#     '''calcule la phase de la lune par la date'''
#     date = int(JJ(Y, M, D))
#     datetest =  int(2459580.5)
#     tmps = 432
#     a = datetest - date
#     if a < 0:
#         a = date - datetest
#     print(a)
#     b = a / tmps
#     print(b)
#     c  = b // 4
#     print(c)
#     if a != 0:
#         if a / tmps >= 6 and a / tmps <= 9:
#             print("nouvelle lune") 
#         elif a / tmps >= 9.0 and a / tmps <= 14.0:    
#             print("1er croissant")
#         elif a / tmps >= 4.5 and a / tmps <= 6:
#             print("pleine lune")
#         elif a / tmps >= 0.1 and a / tmps <= 4.5:
#             print("2er croissant")

#     elif Y == 18 and M == 1 and D == 18: 
#         return "pleine lune"
#     else : 
#         print("erreur")


# # print(JJ(2022, 1, 1))
# print(phase_lune(0, 2005, 2, 14))