# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait
from pybricks.parameters import Axis

# Initialiser le hub.
hub = ThisHub()

# Obtenir l'accélération ou la vitesse angulaire le long d'un seul axe.
# Si vous avez besoin d'une seule valeur, c'est plus efficace en mémoire.
while True:

    # Lire l'accélération vers l'avant.
    forward_acceleration = hub.imu.acceleration(Axis.X)

    # Lire le taux de lacet.
    yaw_rate = hub.imu.angular_velocity(Axis.Z)

    # Imprimer le taux de lacet.
    print(yaw_rate)
    wait(100)
