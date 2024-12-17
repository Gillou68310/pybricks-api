from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

while True:

    # Vérifier quel côté du hub est en haut.
    up_side = hub.imu.up()

    # Utiliser ce côté pour définir l'orientation de l'affichage.
    hub.display.orientation(up_side)

    # Afficher quelque chose, comme une flèche.
    hub.display.icon(Icon.UP)

    wait(10)
