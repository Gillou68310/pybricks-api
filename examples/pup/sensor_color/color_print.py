from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorSensor(Port.A)

while True:
    # Lire la couleur et la réflexion
    color = sensor.color()
    reflection = sensor.reflection()

    # Imprimer la couleur mesurée et la réflexion.
    print(color, reflection)

    # Déplacez le capteur et voyez comment
    # bien vous pouvez détecter les couleurs.

    # Attendre pour pouvoir lire la valeur.
    wait(100)
