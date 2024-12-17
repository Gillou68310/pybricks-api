from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

# Allumer le pixel à la ligne 1, colonne 2.
hub.display.pixel(1, 2)
wait(2000)

# Allumer le pixel à la ligne 2, colonne 4, à 50% de luminosité.
hub.display.pixel(2, 4, 50)
wait(2000)

# Éteindre le pixel à la ligne 1, colonne 2.
hub.display.pixel(1, 2, 0)
wait(2000)
