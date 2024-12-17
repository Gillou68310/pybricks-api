from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.parameters import Port, Color, Direction
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.B)

# Vous pouvez utiliser plusieurs moteurs sur différents canaux.
arm = PFMotor(sensor, 1, Color.BLUE)
wheel = PFMotor(sensor, 4, Color.RED, Direction.COUNTERCLOCKWISE)

# Accélérer les deux moteurs. Seules ces valeurs sont disponibles.
# Les autres valeurs seront arrondies à la valeur la plus proche.
for duty in [15, 30, 45, 60, 75, 90, 100]:
    arm.dc(duty)
    wheel.dc(duty)
    wait(1000)

# Pour rendre le signal plus fiable, il y a une courte
# pause entre les commandes. Ainsi, ils changent de vitesse et
# s'arrêtent à des moments légèrement différents.

# Freiner les deux moteurs.
arm.brake()
wheel.brake()
