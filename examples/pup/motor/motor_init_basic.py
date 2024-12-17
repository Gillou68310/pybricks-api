from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Faire tourner le moteur dans le sens horaire à 500 degrés par seconde.
example_motor.run(500)

# Attendre trois secondes.
wait(3000)

# Faire tourner le moteur dans le sens antihoraire à 500 degrés par seconde.
example_motor.run(-500)

# Attendre trois secondes.
wait(3000)
