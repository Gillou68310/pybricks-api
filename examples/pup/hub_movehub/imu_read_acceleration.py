
from pybricks.hubs import MoveHub
from pybricks.tools import wait

# Initialiser le hub.
hub = MoveHub()

# Obtenir le tuple d'accélération.
print(hub.imu.acceleration())

while True:
    # Obtenir les valeurs d'accélération individuelles.
    x, y, z = hub.imu.acceleration()
    print(x, y, z)

    # Attendre pour voir ce que nous avons imprimé.
    wait(100)
