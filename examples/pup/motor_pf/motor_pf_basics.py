from pybricks.pupdevices import ColorDistanceSensor, PFMotor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.B)

# Initialiser un moteur sur le canal 1, sur la sortie rouge.
motor = PFMotor(sensor, 1, Color.RED)

# Tourner puis s'arrêter.
motor.dc(100)
wait(1000)
motor.stop()
wait(1000)

# Tourner dans l'autre sens à mi-vitesse, puis s'arrêter.
motor.dc(-50)
wait(1000)
motor.stop()
