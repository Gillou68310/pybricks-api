# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub()

# Obtenir le vecteur d'accélération en g.
print(hub.imu.acceleration() / 9810)

# Obtenir le vecteur de vitesse angulaire.
print(hub.imu.angular_velocity())

# Attendre pour voir ce que nous avons imprimé
wait(5000)
