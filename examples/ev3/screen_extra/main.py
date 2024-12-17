#!/usr/bin/env pybricks-micropython

import math

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font, Image

# Initialiser l'EV3
ev3 = EV3Brick()

# ÉCRAN DIVISÉ ###############################################################

# Créer une sous-image pour la moitié gauche de l'écran
left = Image(
    ev3.screen,
    sub=True,
    x1=0,
    y1=0,
    x2=ev3.screen.width // 2 - 1,
    y2=ev3.screen.height - 1,
)

# Créer une sous-image pour la moitié droite de l'écran
right = Image(
    ev3.screen,
    sub=True,
    x1=ev3.screen.width // 2,
    y1=0,
    x2=ev3.screen.width - 1,
    y2=ev3.screen.height - 1,
)

# Utiliser une police à espacement fixe pour que le texte soit aligné verticalement lors de l'impression
right.set_font(Font(size=8, monospace=True))

# Graphique y = sin(x)
def f(x):
    return math.sin(x)

for t in range(200):
    # Graphique sur le côté gauche

    # Mettre à l'échelle t sur l'axe des x et calculer les valeurs de y
    x0 = (t - 1) * 2 * math.pi / left.width
    y0 = f(x0)
    x1 = t * 2 * math.pi / left.width
    y1 = f(x1)

    # Mettre à l'échelle les valeurs de y aux coordonnées de l'écran
    sy0 = (-y0 + 1) * left.height / 2
    sy1 = (-y1 + 1) * left.height / 2

    # Déplacer le graphique actuel vers la gauche d'un pixel
    left.draw_image(-1, 0, left)
    # Remplir la dernière colonne de blanc pour effacer le point de tracé précédent
    left.draw_line(left.width - 1, 0, left.width - 1, left.height - 1, 1, Color.WHITE)
    # Dessiner la nouvelle valeur du graphique dans la dernière colonne
    left.draw_line(left.width - 2, int(sy0), left.width - 1, int(sy1), 3)

    # Imprimer chaque 10ème valeur sur le côté droit
    if t % 10 == 0:
        right.print("{:10.2f}{:10.2f}".format(x1, y1))

    wait(100)

# ANIMATION DE SPRITE #########################################################

# Copie de l'écran pour le double tampon
buf = Image(ev3.screen)

# Charger les images à partir du fichier
bg = Image("background.png")
sprite = Image("sprite.png")

# Nombre de cellules dans chaque animation de sprite
NUM_CELLS = 8

# Chaque cellule du sprite mesure 75 x 100 pixels
CELL_WIDTH, CELL_HEIGHT = 75, 100

# Obtenir des sous-images pour chaque cellule individuelle
# C'est plus efficace que de charger des images individuelles
walk_right = [
    Image(
        sprite,
        sub=True,
        x1=x * CELL_WIDTH,
        y1=0,
        x2=(x + 1) * CELL_WIDTH - 1,
        y2=CELL_HEIGHT - 1,
    )
    for x in range(NUM_CELLS)
]
walk_left = [
    Image(
        sprite,
        sub=True,
        x1=x * CELL_WIDTH,
        y1=CELL_HEIGHT,
        x2=(x + 1) * CELL_WIDTH - 1,
        y2=2 * CELL_HEIGHT - 1,
    )
    for x in range(NUM_CELLS)
]

# Marcher de gauche à droite
for x in range(-100, 200, 2):
    # Commencer avec l'image de fond
    buf.draw_image(0, 0, bg)
    # Dessiner le sprite actuel - le violet est traité comme transparent
    buf.draw_image(x, 5, walk_right[x // 5 % NUM_CELLS], Color.PURPLE)
    # Copier le double tampon sur l'écran
    ev3.screen.draw_image(0, 0, buf)
    # 20 images par seconde
    wait(50)

# Marcher de droite à gauche
for x in range(200, -100, -2):
    buf.draw_image(0, 0, bg)
    buf.draw_image(x, 5, walk_left[x // 5 % NUM_CELLS], Color.PURPLE)
    ev3.screen.draw_image(0, 0, buf)
    wait(50)

wait(1000)
