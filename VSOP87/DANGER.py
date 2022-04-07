import math
import temps
import position_planetes

def get_coords(L, B, R) :
    '''Convertir des coordonnées écliptiques en coordonnées rectangulaires.'''
    # https://en.wikipedia.org/wiki/Ecliptic_coordinate_system#Rectangular_coordinates
    return [ R * math.cos(B) * math.cos(L), R * math.cos(B) * math.sin(L), R * math.sin(B) ]

def get_distance(plan, sun) :
    # Simple Pythagore pour obtenir la distance entre deux points.
    return math.sqrt((plan[0] - sun[0])**2 + (plan[1] - sun[1])**2 + (plan[2] - sun[2])**2)


def get(Y, M, D) :
    '''Permet de calculer, pour chaque planète, les distance et dates d'apogée et périgée.'''
    temps_acutel = temps.JJ(Y, M, D)

    mercure_info = [[],[]] # [[distances], [dates]]
    venus_info = [[],[]]
    terre_info = [[],[]]
    mars_info = [[],[]]
    jupiter_info = [[],[]]
    saturne_info = [[],[]]
    uranus_info = [[],[]]
    neptune_info = [[],[]]

    for day in range(88) : # Période orbitale de Mercure, en jours
        mercure_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('mercure', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        mercure_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_mercure = max(mercure_info[0]) # La distance de l'apogée est la distance maximale au Soleil
    date_apogee_mercure = mercure_info[1][mercure_info[0].index(apogee_mercure)] # On récupère la date en JJ qui correspond à cette distance
    print(f"Apogée de Mercure le \n{date_apogee_mercure}\nÀ une distance (en UA) :\n{apogee_mercure}\n") # Affichage
    print()
    perigee_mercure = min(mercure_info[0]) # La distance du périgée est la distance minimale au Soleil
    date_perigee_mercure = mercure_info[1][mercure_info[0].index(perigee_mercure)] # # On récupère la date en JJ qui correspond à cette distance
    print(f"Périgée de Mercure le \n{date_perigee_mercure}\nÀ une distance (en UA) :\n{perigee_mercure}\n") # Affichage
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(225) : # Période orbitale de Venus, en jours
        venus_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('venus', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        venus_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_venus = max(venus_info[0])
    date_apogee_venus = venus_info[1][venus_info[0].index(apogee_venus)]
    print(f"Apogée de Venus le \n{date_apogee_venus}\nÀ une distance (en UA) :\n{apogee_venus}\n")
    print()
    perigee_venus = min(venus_info[0])
    date_perigee_venus = venus_info[1][venus_info[0].index(perigee_venus)]
    print(f"Périgée de Venus le \n{date_perigee_venus}\nÀ une distance (en UA) :\n{perigee_venus}\n")
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(365) : # Période orbitale de Terre, en jours
        terre_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('terre', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        terre_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_terre = max(terre_info[0])
    date_apogee_terre = terre_info[1][terre_info[0].index(apogee_terre)]
    print(f"Apogée de Terre le \n{date_apogee_terre}\nÀ une distance (en UA) :\n{apogee_terre}\n")
    print()
    perigee_terre = min(terre_info[0])
    date_perigee_terre = terre_info[1][terre_info[0].index(perigee_terre)]
    print(f"Périgée de Terre le \n{date_perigee_terre}\nÀ une distance (en UA) :\n{perigee_terre}\n")
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(687) : # Période orbitale de Mars, en jours
        mars_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('mars', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        mars_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_mars = max(mars_info[0])
    date_apogee_mars = mars_info[1][mars_info[0].index(apogee_mars)]
    print(f"Apogée de Mars le \n{date_apogee_mars}\nÀ une distance (en UA) :\n{apogee_mars}\n")
    print()
    perigee_mars = min(mars_info[0])
    date_perigee_mars = mars_info[1][mars_info[0].index(perigee_mars)]
    print(f"Périgée de Mars le \n{date_perigee_mars}\nÀ une distance (en UA) :\n{perigee_mars}\n")
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(4380) : # Période orbitale de Jupiter, en jours
        jupiter_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('jupiter', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        jupiter_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_jupiter = max(jupiter_info[0])
    date_apogee_jupiter = jupiter_info[1][jupiter_info[0].index(apogee_jupiter)]
    print(f"Apogée de Jupiter le \n{date_apogee_jupiter}\nÀ une distance (en UA) :\n{apogee_jupiter}\n")
    print()
    perigee_jupiter = min(jupiter_info[0])
    date_perigee_jupiter = jupiter_info[1][jupiter_info[0].index(perigee_jupiter)]
    print(f"Périgée de Jupiter le \n{date_perigee_jupiter}\nÀ une distance (en UA) :\n{perigee_jupiter}\n")
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(10585) : # Période orbitale de Saturne, en jours
        saturne_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('saturne', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        saturne_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_saturne = max(saturne_info[0])
    date_apogee_saturne = saturne_info[1][saturne_info[0].index(apogee_saturne)]
    print(f"Apogée de Saturne le \n{date_apogee_saturne}\nÀ une distance (en UA) :\n{apogee_saturne}\n")
    print()
    perigee_saturne = min(saturne_info[0])
    date_perigee_saturne = saturne_info[1][saturne_info[0].index(perigee_saturne)]
    print(f"Périgée de Saturne le \n{date_perigee_saturne}\nÀ une distance (en UA) :\n{perigee_saturne}\n")
    print()

    temps_acutel = temps.JJ(Y, M, D)

    for day in range(84) : # Période orbitale de Uranus, en jours
        uranus_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('uranus', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        uranus_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_uranus = max(uranus_info[0])
    date_apogee_uranus = uranus_info[1][uranus_info[0].index(apogee_uranus)]
    print(f"Apogée de Uranus le \n{date_apogee_uranus}\nÀ une distance (en UA) :\n{apogee_uranus}\n")
    print()
    perigee_uranus = min(uranus_info[0])
    date_perigee_uranus = uranus_info[1][uranus_info[0].index(perigee_uranus)]
    print(f"Périgée de Uranus le \n{date_perigee_uranus}\nÀ une distance (en UA) :\n{perigee_uranus}\n")
    print()


    temps_acutel = temps.JJ(Y, M, D)

    for day in range(60225) : # Période orbitale de Naptune, en jours terrestres
        uranus_info[0].append(get_distance(get_coords(*position_planetes.get_by_VSOP87('uranus', *temps.gregorien(temps_acutel))), position_planetes.get_sun(*temps.gregorien(temps_acutel))))
        uranus_info[1].append(temps_acutel)
        temps_acutel += 1

    apogee_neptune = max(neptune_info[0])
    date_apogee_neptune = neptune_info[1][neptune_info[0].index(apogee_neptune)]
    print(f"Apogée de Neptune le \n{date_apogee_neptune}\nÀ une distance (en UA) :\n{apogee_neptune}\n")
    print()
    perigee_neptune = min(neptune_info[0])
    date_perigee_neptune = neptune_info[1][neptune_info[0].index(perigee_neptune)]
    print(f"Périgée de Neptune le \n{date_perigee_neptune}\nÀ une distance (en UA) :\n{perigee_neptune}\n")
    print()

def get_angle(A, B, C) :
    '''Détermine l'angle (point1, point2, point3) grâce au théorême d'Al-Kashi'''

    '''
    On a, dans le triangle ABC, d'après le théorème d'Al-Kashi :
    
                         AB ^ 2 = AC ^ 2 + CB ^ 2 - 2 AC • CB . cos(ACB)
    
    <=>  - 2 AC • CB • cos(ACB) = AB ^ 2 - (AC ^ 2 + CB ^ 2)
    <=>                cos(ABC) = (- AB ^ 2 + AC ^ 2 + CB ^ 2) / (2 AC • CB)

    <=>                     ABC = arc cos((- AB ^ 2 + AC ^ 2 + CB ^ 2) / (2 AC • CB))
    '''

    # Calcul des distances :
    AB = math.dist(A, B)
    AC = math.dist(A, C)
    CB = math.dist(C, B)

    return math.acos(
        (
            - (AB ** 2) + (AC ** 2) + (CB ** 2)
        ) / (
            2 * AC * CB
        )
    )

def calculate_angle_by_mercury() :
    '''Calcule les différences d'angle avec Mercure lors de périgées'''
    mercury = get_coords(*position_planetes.get_by_VSOP87('mercure', *temps.gregorien(2459596.5)))

    for planete, date in (  ('Venus', 2459617.5),
                            ('Terre', 2459601.5),
                            ('Mars', 2459750.5),
                            ('Jupiter', 2459969.5),
                            ('Saturne', 2463555.5)) :
        print(f"""\nAngle Mercure-Soleil-{planete} (radians) :\n {
            get_angle(mercury, position_planetes.get_sun(*temps.gregorien(date)),
            get_coords(*position_planetes.get_by_VSOP87(planete, *temps.gregorien(date))))
            }\n""")

if __name__ == '__main__' :
    #get(2022, 1, 1)
    calculate_angle_by_mercury()