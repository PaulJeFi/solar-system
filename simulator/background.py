from PIL import Image
import random
import numpy as np

# Définitions des variables
screen_size = width, height = (1080, 720) # La taille finale de l'image, en px
star_percent                = 1           # Le pourcentage d'étoiles
star_median_size            = 6           # La taille moyenne des étoiles, en px
star_size_error             = 8           # La marge d'erreur de la taille, en %
color_max_randomness        = 3           # Aléatoire des couleurs, en unité.

star_colors  = [ [255, 107, 70], [219, 168, 46], [0, 154, 255], [75, 151, 255] ]  # Liste de couleurs réalistes pour une étoile. Des variations aléatoires seront effectuées.

# Initialisation de l'image
img_array = [[(0, 0, 0) for x in range(width)] for y in range(height)]

def place_etoile(x, y, color) :
    '''Place une étoile'''

    radius = star_median_size + random.randint(star_median_size - star_size_error, star_median_size + star_size_error)
    for X in range(-radius, radius) :
        for Y in range(-radius, radius) :
            if (X + x < width) and (Y + y < height) :
                if (X+1)**2 + Y**2 >= radius*star_median_size :
                    continue
                img_array[Y + y][X + x] = [color[0], color[1], color[2]]

# Itération sur l'image
x, y = 0, 0
while x * y < width * height :

    if random.randint(0, 100) > star_percent :
        continue
    
    # Selection de la couleur
    selected_color = random.choice(star_colors)
    color = [selected_color[0]+random.randint(-color_max_randomness, color_max_randomness),
             selected_color[1]+random.randint(-color_max_randomness, color_max_randomness),
             selected_color[2]+random.randint(-color_max_randomness, color_max_randomness)]

    
    place_etoile(x, y, color)


    # NE PAS OUBLIER D'AUGMENTER x ET y
    x += random.choice(list(range(1, 1 +  width//(1+star_percent)))) + random.randint(width//100, width//10)
    if x >= width :
        if y == height-1 :
            break
        x %= width
        y += random.choice(list(range(1, 1 +  height//(1+star_percent)))) + random.randint(height//100, height//10)
    if y >= height :
        y = height-1


# Enregistrement de l'image
array = np.array(img_array, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('./simulator/images/background.png')