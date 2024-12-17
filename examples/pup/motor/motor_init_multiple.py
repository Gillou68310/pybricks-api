from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser les moteurs sur les ports A et B.
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# Faire tourner les deux moteurs à 500 degrés par seconde.
track_motor.run(500)
gripper_motor.run(500)

# Attendre trois secondes.
wait(3000)
