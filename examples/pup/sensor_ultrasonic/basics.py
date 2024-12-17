from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
eyes = UltrasonicSensor(Port.A)

while True:
    # Imprimer la distance mesurée.
    print(eyes.distance())

    # Si un objet est détecté à moins de 500mm :
    if eyes.distance() < 500:
        # Allumer les lumières.
        eyes.lights.on(100)
    else:
        # Éteindre les lumières.
        eyes.lights.off()

    # Attendre un certain temps pour pouvoir lire ce qui est imprimé.
    wait(100)
