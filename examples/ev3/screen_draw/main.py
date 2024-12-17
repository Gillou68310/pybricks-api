#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait

# Initialiser l'EV3
ev3 = EV3Brick()

# Dessiner un rectangle
ev3.screen.draw_box(10, 10, 40, 40)

# Dessiner un rectangle plein
ev3.screen.draw_box(20, 20, 30, 30, fill=True)

# Dessiner un rectangle avec des coins arrondis
ev3.screen.draw_box(50, 10, 80, 40, 5)

# Dessiner un cercle
ev3.screen.draw_circle(25, 75, 20)

# Dessiner un triangle en utilisant des lignes
x1, y1 = 65, 55
x2, y2 = 50, 95
x3, y3 = 80, 95
ev3.screen.draw_line(x1, y1, x2, y2)
ev3.screen.draw_line(x2, y2, x3, y3)
ev3.screen.draw_line(x3, y3, x1, y1)

# Attendre un peu pour regarder les formes
wait(5000)
