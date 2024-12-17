from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Commencer à se déplacer à 300 degrés par seconde.
example_motor.run(300)

# Afficher l'angle et la vitesse 50 fois.
for i in range(100):

    # Lire l'angle (degrés) et la vitesse (degrés par seconde).
    angle = example_motor.angle()
    speed = example_motor.speed()

    # Imprimer les valeurs.
    print(angle, speed)

    # Attendre un peu pour pouvoir lire ce qui est affiché.
    wait(200)
