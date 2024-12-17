from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.A)

while True:
    # Lire la couleur.
    color = sensor.color()

    # Imprimer la couleur mesurée.
    print(color)

    # Déplacez le capteur et voyez comment
    # bien vous pouvez détecter les couleurs.

    # Attendre pour pouvoir lire la valeur.
    wait(100)
