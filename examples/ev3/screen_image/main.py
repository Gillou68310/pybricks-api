#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Image, ImageFile

# Le chargement des images à partir de la carte SD prend du temps, il est donc préférable de les charger
# une seule fois au début du programme comme ceci :
ev3_img = Image(ImageFile.EV3_ICON)

# Initialiser l'EV3
ev3 = EV3Brick()

# Afficher une image
ev3.screen.load_image(ev3_img)

# Attendre un peu pour regarder l'image
wait(5000)
