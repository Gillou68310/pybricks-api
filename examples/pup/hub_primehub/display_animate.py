from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

# Éteindre la lumière du hub (optionnel).
hub.light.off()

# Créer une liste d'intensités de 0 à 100 et retour.
brightness = list(range(0, 100, 4)) + list(range(100, 0, -4))

# Créer une animation de l'icône de cœur avec une luminosité changeante.
hub.display.animate([Icon.HEART * i / 100 for i in brightness], 30)

# L'animation se répète en arrière-plan. Ici, nous attendons simplement.
while True:
    wait(100)
