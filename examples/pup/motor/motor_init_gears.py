from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialiser un moteur sur le port A avec la direction positive comme antihoraire.
# Spécifier également un train d'engrenages avec un pignon de 12 dents et un pignon de 36 dents. Le pignon de 12 dents
# est attaché à l'axe du moteur. Le pignon de 36 dents est à l'axe de sortie.
geared_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE, [12, 36])

# Faire tourner l'axe de sortie à 100 degrés par seconde. La vitesse du moteur
# est automatiquement augmentée pour compenser les engrenages.
geared_motor.run(100)

# Attendre trois secondes.
wait(3000)
