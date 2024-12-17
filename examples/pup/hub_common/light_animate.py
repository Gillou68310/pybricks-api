# ThisHub = CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait
from umath import sin, pi

# Initialiser le hub.
hub = ThisHub()

# Faire une animation avec plusieurs couleurs.
hub.light.animate([Color.RED, Color.GREEN, Color.NONE], interval=500)

wait(10000)

# Faire en sorte que la couleur ROUGE devienne faible et brillante en utilisant un motif sinusoïdal.
hub.light.animate([Color.RED * (0.5 * sin(i / 15 * pi) + 0.5) for i in range(30)], 40)

wait(10000)

# Parcourir un arc-en-ciel de couleurs.
hub.light.animate([Color(h=i * 8) for i in range(45)], interval=40)

wait(10000)
