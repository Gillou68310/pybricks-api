from pybricks.pupdevices import TiltSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
accel = TiltSensor(Port.A)

while True:
    # Lire les angles d'inclinaison par rapport au plan horizontal.
    pitch, roll = accel.tilt()

    # Imprimer les valeurs
    print("Pitch:", pitch, "Roll:", roll)

    # Attendre un peu pour pouvoir lire ce qui est imprimé.
    wait(100)
