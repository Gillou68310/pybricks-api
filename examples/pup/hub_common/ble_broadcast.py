# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub(broadcast_channel=1)

# Initialiser les moteurs.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # Lire les angles des moteurs à envoyer à l'autre hub.
    left_angle = left_motor.angle()
    right_angle = right_motor.angle()

    # Définir les données de diffusion et commencer à diffuser si ce n'est pas déjà fait.
    data = (left_angle, right_angle)
    hub.ble.broadcast(data)

    # Les diffusions ne sont envoyées que toutes les 100 millisecondes, il n'y a donc
    # aucune raison d'appeler la méthode broadcast() plus souvent que cela.
    wait(100)
