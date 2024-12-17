#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

from connection import SpikePrimeStreamReader

# Bip!
ev3 = EV3Brick()
ev3.speaker.beep()

# Créer la connexion. Voir README.md pour trouver l'adresse de votre hub SPIKE.
spike = SpikePrimeStreamReader("F4:84:4C:AA:C8:A4")

# Maintenant, vous pouvez simplement lire les valeurs !
for i in range(100):
    print(spike.values())
    wait(100)
