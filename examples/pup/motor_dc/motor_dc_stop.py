from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sans capteurs de rotation sur le port A.
example_motor = DCMotor(Port.A)

# Démarrer et arrêter 10 fois.
for count in range(10):
    print("Counter:", count)

    example_motor.dc(70)
    wait(1000)

    example_motor.stop()
    wait(1000)
