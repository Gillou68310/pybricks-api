#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button

from menu import wait_for_button

# Initialiser l'EV3.
ev3 = EV3Brick()

while True:
    # Afficher le menu et attendre qu'un bouton soit sélectionné.
    button = wait_for_button(ev3)

    # Maintenant, vous pouvez faire quelque chose, en fonction du bouton pressé.

    # Dans cette démo, nous jouons simplement un son différent pour chaque bouton.
    if button == Button.LEFT:
        ev3.speaker.beep(200)
    elif button == Button.RIGHT:
        ev3.speaker.beep(400)
    elif button == Button.UP:
        ev3.speaker.beep(600)
    elif button == Button.DOWN:
        ev3.speaker.beep(800)
    elif button == Button.CENTER:
        ev3.speaker.beep(1000)
