from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.A)

while True:
    # La méthode standard color() "arrondit" toujours la
    # mesure à la couleur "entière" la plus proche.
    # C'est utile pour la plupart des applications.

    # Mais vous pouvez obtenir la teinte, la saturation,
    # et la valeur originales sans "arrondi", comme suit :
    color = sensor.hsv()

    # Imprimer les résultats.
    print(color)

    # Attendre pour pouvoir lire la valeur.
    wait(500)
