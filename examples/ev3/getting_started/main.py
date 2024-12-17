#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Créez vos objets ici

# Initialiser le Brick EV3.
ev3 = EV3Brick()

# Initialiser un moteur au port B.
test_motor = Motor(Port.B)

# Écrivez votre programme ici

# Jouer un son.
ev3.speaker.beep()

# Faire tourner le moteur jusqu'à 500 degrés par seconde. À un angle cible de 90 degrés.
test_motor.run_target(500, 90)

# Jouer un autre bip sonore.
ev3.speaker.beep(frequency=1000, duration=500)
