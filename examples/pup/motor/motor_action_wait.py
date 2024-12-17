from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialiser les moteurs sur les ports A et B.
track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

# Faire démarrer le moteur de la chenille,
# mais ne pas attendre qu'il ait fini.
track_motor.run_angle(500, 360, wait=False)

# Maintenant, faire tourner le moteur de la pince. Cela
# signifie qu'ils bougent en même temps.
gripper_motor.run_angle(200, 720)
