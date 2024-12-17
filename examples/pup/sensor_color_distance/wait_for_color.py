from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.A)

# Ceci est une fonction qui attend une couleur désirée.
def wait_for_color(desired_color):
    # Tant que la couleur n'est pas la couleur désirée, nous continuons à attendre.
    while sensor.color() != desired_color:
        wait(20)

# Maintenant, nous utilisons la fonction que nous venons de créer ci-dessus.
while True:

    # Ici, vous pouvez faire avancer votre train/véhicule.

    print("Waiting for red ...")
    wait_for_color(Color.RED)

    # Ici, vous pouvez faire reculer votre train/véhicule.

    print("Waiting for blue ...")
    wait_for_color(Color.BLUE)
