from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sans capteurs de rotation sur le port A.
example_motor = DCMotor(Port.A)

# Faire tourner le moteur dans le sens horaire (avant) à 70% du cycle de service ("70% de puissance").
example_motor.dc(70)

# Attendre trois secondes.
wait(3000)

# Faire tourner le moteur dans le sens antihoraire (arrière) à 70% du cycle de service.
example_motor.dc(-70)

# Attendre trois secondes.
wait(3000)
