from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialiser un moteur sans capteurs de rotation sur le port A,
# avec la direction positive comme sens antihoraire.
example_motor = DCMotor(Port.A, Direction.COUNTERCLOCKWISE)

# Lorsque nous choisissons un cycle de service positif, le moteur tourne maintenant dans le sens antihoraire.
example_motor.dc(70)

# Ceci est utile lorsque votre moteur (de train) est monté à l'envers ou à l'envers.
# En changeant la direction positive, votre script sera plus facile à lire,
# car une valeur positive fait maintenant avancer votre train/robot.

# Attendre trois secondes.
wait(3000)
