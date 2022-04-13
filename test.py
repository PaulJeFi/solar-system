################################################################################
#                             Fichier SandBox                                  #
################################################################################

def get_followed_planet(self, gest) -> Tuple(float, float) :
        '''Permet de récupérer la planète suivie'''
        for planete in gest.planetes:
            if planete[gest.data_index][0]:
                return planete[gest.data_index][3]
        return (0, 0) # Cas où aucune planète n'est suivie