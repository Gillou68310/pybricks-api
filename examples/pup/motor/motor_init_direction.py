from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialiser un moteur sur le port A avec la direction positive comme antihoraire.
example_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

# Lorsque nous choisissons une valeur de vitesse positive, le moteur tourne maintenant dans le sens antihoraire.
example_motor.run(500)

# Cela est utile lorsque votre moteur est monté à l'envers ou à l'envers.
# En changeant la direction positive, votre script sera plus facile à lire,
# car une valeur positive fait maintenant avancer votre robot/mécanisme.

# Attendre trois secondes.
wait(3000)
