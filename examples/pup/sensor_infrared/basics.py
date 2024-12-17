from pybricks.pupdevices import InfraredSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
ir = InfraredSensor(Port.A)

while True:
    # Lire toutes les informations que nous pouvons obtenir de ce capteur.
    dist = ir.distance()
    count = ir.count()
    ref = ir.reflection()

    # Imprimer les valeurs
    print("Distance:", dist, "Count:", count, "Reflection:", ref)

    # Déplacez le capteur et bougez vos mains devant
    # pour voir ce qui arrive aux valeurs.

    # Attendre un peu pour pouvoir lire ce qui est imprimé.
    wait(200)
