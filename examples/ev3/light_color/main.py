#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.parameters import Color

# Initialiser l'EV3
ev3 = EV3Brick()

# Allumer une lumière rouge
ev3.light.on(Color.RED)

# Attendre
wait(1000)

# Éteindre la lumière
ev3.light.off()
