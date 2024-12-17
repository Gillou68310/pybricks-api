from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Veuillez d'abord consulter l'exemple précédent. Cet exemple
# trouve deux points d'extrémité, puis fait du milieu le point zéro.

# La fonction run_until_stalled nous donne l'angle auquel il s'est arrêté.
# Nous voulons connaître cette valeur pour les deux points d'extrémité.
left_end = example_motor.run_until_stalled(-200, duty_limit=30)
right_end = example_motor.run_until_stalled(200, duty_limit=30)

# Nous venons de nous déplacer jusqu'à la butée la plus à droite. Donc, nous pouvons réinitialiser
# cet angle pour qu'il soit la moitié de la distance entre les deux points d'extrémité.
# De cette façon, le milieu correspond à 0 degrés.
example_motor.reset_angle((right_end - left_end) / 2)

# Désormais, nous pouvons simplement courir vers zéro pour atteindre le milieu.
example_motor.run_target(200, 0)

wait(1000)
