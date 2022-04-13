################################################################################
#                             Fichier SandBox                                  #
################################################################################

def get_followed_planet(self, gest) -> str | Tuple(float, float) :
        '''Permet de récupérer la planète suivie'''
        for planete in gest.planetes:
            if planete[gest.data_index][0]:
                return 'Mercure Venus Terre Mars Jupiter Saturne Uranus Neptune'.split()[gest.planetes.index(planete)]
        return (0, 0) # Cas où aucune planète n'est suivie