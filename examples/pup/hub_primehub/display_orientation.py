from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Side

# Initialiser le hub.
hub = PrimeHub()

# Faire pivoter l'affichage. Maintenant, la droite est en haut.
hub.display.orientation(up=Side.RIGHT)

# Afficher un nombre. Cela sera affiché de côté.
hub.display.number(23)

# Attendre pour voir ce qui est affiché.
wait(10000)
