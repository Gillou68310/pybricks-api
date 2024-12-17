# ThisHub = TechnicHub PrimeHub MoveHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color, Side
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub()

# Définir les couleurs pour chaque côté dans un dictionnaire.
SIDE_COLORS = {
    Side.TOP: Color.RED,
    Side.BOTTOM: Color.BLUE,
    Side.LEFT: Color.GREEN,
    Side.RIGHT: Color.YELLOW,
    Side.FRONT: Color.MAGENTA,
    Side.BACK: Color.BLACK,
}

# Mettre à jour continuellement la couleur en fonction du côté détecté vers le haut.
while True:

    # Vérifier quel côté du hub est vers le haut.
    up_side = hub.imu.up()

    # Changer la couleur en fonction du côté.
    hub.light.on(SIDE_COLORS[up_side])

    # Imprimer également le résultat.
    print(up_side)
    wait(50)
