# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub()

while True:
    # Lire les valeurs d'inclinaison.
    pitch, roll = hub.imu.tilt()

    # Imprimer le résultat.
    print(pitch, roll)
    wait(200)
