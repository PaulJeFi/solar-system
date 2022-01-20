from astropy.time import Time
from astroquery.jplhorizons import Horizons

BROWN = (200, 100, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

import pygame
pygame.init()
haut = 755
large = 1000
screen = pygame.display.set_mode((large, haut))
pygame.display.set_caption("Mercure")
screen.fill(WHITE)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()

liste = []
for year in range(2000, 2101) :
    for month in range(1, 13) :
        for day in range(1, 29) : # À cause des années bissectiles. Flemme de les gérer.
            if len(str(month)) == 1 :
                month = "0"+str(month)
            if len(str(day)) == 1 :
                day = "0"+str(day)
            liste.append(f'{year}-{month}-{day}')

def main() :
    points = []
    while True :
        for date in liste :
            dt = clock.tick(144)
            screen.fill(WHITE)
            for planet in range(1, 4) :
                obj = Horizons(id=planet, location="@sun", epochs=Time(date).jd, id_type='id').vectors()
                x, y = obj['x']*100+haut/2, obj['y']*100+haut/2
                points.append((int(x), int(y)))
                for point in points :
                    screen.set_at(point, BLACK)
                pygame.draw.circle(screen, BROWN, (int(x), int(y)), 5)
                screen.blit(myfont.render(date, False, (0, 0, 0)), (50, 50))
            pygame.draw.circle(screen, YELLOW, (large/2, haut/2), 10)
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    return None
            pygame.display.flip()

if __name__ == '__main__' :
    main()