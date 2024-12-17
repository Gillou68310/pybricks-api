from pybricks.hubs import PrimeHub
from pybricks.parameters import Icon, Side
from pybricks.tools import wait

from urandom import randint

# Initialiser le hub.
hub = PrimeHub()
hub.display.orientation(up=Side.RIGHT)

while True:

    # Commencer avec un sourcil gauche aléatoire : en haut ou en bas.
    if randint(0, 100) < 70:
        brows = Icon.EYE_LEFT_BROW * 0.5
    else:
        brows = Icon.EYE_LEFT_BROW_UP * 0.5

    # Ajouter un sourcil droit aléatoire : en haut ou en bas.
    if randint(0, 100) < 70:
        brows += Icon.EYE_RIGHT_BROW * 0.5
    else:
        brows += Icon.EYE_RIGHT_BROW_UP * 0.5

    for i in range(3):
        # Afficher les yeux ouverts plus les sourcils aléatoires.
        hub.display.icon(Icon.EYE_LEFT + Icon.EYE_RIGHT + brows)
        wait(2000)

        # Afficher les yeux clignotés plus les sourcils aléatoires.
        hub.display.icon(Icon.EYE_LEFT_BLINK * 0.7 + Icon.EYE_RIGHT_BLINK * 0.7 + brows)
        wait(200)
