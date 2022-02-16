import kepler as kp
import pygame
import sys
from time import time

BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

width, height = 1080, 600 # dimensions de l'écran, en pixels 1080, 720
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spacior")
pygame.display.set_icon(pygame.image.load('./simulator/images/logo.png'))
screen.fill(BLACK)
clock = pygame.time.Clock()

def update_time(temps, j, last_frame=time()):
    new_frame = time()
    return temps + (j/365.25)*(new_frame-last_frame), new_frame

def main():
    
    sunpos = (int(width/2), int(height/2))

    moon = kp.Planete(periapsis=100, apoapsis=450, center_of_mass=sunpos)

    temps = 1
    vitesse = 365.25 / 2
    frame_time = time()
    
    while True:
        dt = clock.tick(144)
        screen.fill(BLACK)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

        moon_pos = moon.calculate_point_from_time(temps)

        pygame.draw.circle(screen, WHITE, [int(moon_pos[0]), int(moon_pos[1])], 15) # Soleil
        pygame.draw.circle(screen, YELLOW, sunpos, 30) # Soleil
        for point in moon.orbit_path :
            screen.set_at((int(point[0]), int(point[1])), WHITE)
    
        temps, frame_time = update_time(temps, vitesse, frame_time)
        
        pygame.display.flip()

if __name__ == '__main__':
    main()