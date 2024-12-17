# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub(observe_channels=[1])

# Initialiser les moteurs.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

while True:
    # Recevoir la diffusion de l'autre hub.

    data = hub.ble.observe(1)

    if data is None:
        # Aucune donnée n'a été reçue au cours de la dernière seconde.
        hub.light.on(Color.RED)
    else:
        # Des données ont été reçues et sont vieilles de moins d'une seconde.
        hub.light.on(Color.GREEN)

        # *data* contient les mêmes valeurs dans le même ordre
        # qui ont été passées à hub.ble.broadcast() sur l'autre hub.
        left_angle, right_angle = data

        # Faire en sorte que les moteurs de ce hub reflètent la position des
        # moteurs de l'autre hub.
        left_motor.track_target(left_angle)
        right_motor.track_target(right_angle)

    # Les diffusions ne sont envoyées que toutes les 100 millisecondes, il n'y a donc
    # aucune raison d'appeler la méthode observe() plus souvent que cela.
    wait(100)
