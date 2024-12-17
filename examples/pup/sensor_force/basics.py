from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
button = ForceSensor(Port.A)

while True:
    # Lire toutes les informations que nous pouvons obtenir de ce capteur.
    force = button.force()
    dist = button.distance()
    press = button.pressed()
    touch = button.touched()

    # Imprimer les valeurs
    print("Force", force, "Dist:", dist, "Pressed:", press, "Touched:", touch)

    # Poussez le bouton du capteur pour voir ce qui arrive aux valeurs.

    # Attendre un peu pour pouvoir lire ce qui est imprimé.
    wait(200)
