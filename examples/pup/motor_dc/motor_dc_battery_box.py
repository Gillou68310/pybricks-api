from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le moteur.
train_motor = DCMotor(Port.A)

# Choisir le niveau de "puissance" pour votre train. Négatif signifie inverse.
train_motor.dc(50)

# Continuer à ne rien faire. Le train continue simplement.
while True:
    wait(1000)
