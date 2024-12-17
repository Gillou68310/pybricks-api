#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Button

# Initialiser l'EV3
ev3 = EV3Brick()

# Attendre que l'un des boutons soit pressé
while not any(ev3.buttons.pressed()):
    wait(10)

# Faire quelque chose si le bouton gauche est pressé
if Button.LEFT in ev3.buttons.pressed():
    print("The left button is pressed.")

# Attendre que tous les boutons soient relâchés
while any(ev3.buttons.pressed()):
    wait(10)
