from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

while True:

    # Obtenir la valeur d'angle par défaut.
    angle = example_motor.angle()

    # Obtenir l'angle entre 0 et 360.
    absolute_angle = example_motor.angle() % 360

    # Obtenir l'angle entre -180 et 179.
    wrapped_angle = (example_motor.angle() + 180) % 360 - 180

    # Imprimer les résultats.
    print(angle, absolute_angle, wrapped_angle)
    wait(100)
