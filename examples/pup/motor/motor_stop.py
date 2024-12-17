from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Tourner à 500 deg/s puis s'arrêter en roue libre.
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# Tourner à 500 deg/s puis s'arrêter en freinant.
example_motor.run(500)
wait(1500)
example_motor.brake()
wait(1500)

# Tourner à 500 deg/s puis s'arrêter en maintenant.
example_motor.run(500)
wait(1500)
example_motor.hold()
wait(1500)

# Tourner à 500 deg/s puis s'arrêter en tournant à 0 vitesse.
example_motor.run(500)
wait(1500)
example_motor.run(0)
wait(1500)
