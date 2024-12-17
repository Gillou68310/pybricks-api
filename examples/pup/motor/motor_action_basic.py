from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Tourner à 500 deg/s puis s'arrêter en roue libre.
print("Demo of run")
example_motor.run(500)
wait(1500)
example_motor.stop()
wait(1500)

# Tourner à 70% du cycle de service ("puissance") puis s'arrêter en roue libre.
print("Demo of dc")
example_motor.dc(50)
wait(1500)
example_motor.stop()
wait(1500)

# Tourner à 500 deg/s pendant deux secondes.
print("Demo of run_time")
example_motor.run_time(500, 2000)
wait(1500)

# Tourner à 500 deg/s pendant 90 degrés.
print("Demo of run_angle")
example_motor.run_angle(500, 90)
wait(1500)

# Tourner à 500 deg/s jusqu'à l'angle 0
print("Demo of run_target to 0")
example_motor.run_target(500, 0)
wait(1500)

# Tourner à 500 deg/s jusqu'à l'angle -90
print("Demo of run_target to -90")
example_motor.run_target(500, -90)
wait(1500)

# Tourner à 500 deg/s jusqu'à ce que le moteur cale
print("Demo of run_until_stalled")
example_motor.run_until_stalled(500)
print("Done")
wait(1500)
