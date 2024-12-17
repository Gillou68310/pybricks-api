from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser les moteurs sur les ports A et B.
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# Faire effectuer une action aux deux moteurs avec wait=False
track_motor.run_angle(500, 360, wait=False)
gripper_motor.run_angle(200, 720, wait=False)

# Tant que l'un ou l'autre des moteurs n'a pas fini,
# faire autre chose. Dans cet exemple, juste attendre.
while not track_motor.done() or not gripper_motor.done():
    wait(10)

print("Both motors are done!")
