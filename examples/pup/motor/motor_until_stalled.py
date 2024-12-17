from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Nous utiliserons une vitesse de 200 deg/s dans toutes nos commandes.
speed = 200

# Faire tourner le moteur en sens inverse jusqu'à ce qu'il atteigne une butée mécanique.
# Le paramètre duty_limit=30 signifie qu'il n'appliquera que 30%
# du couple maximum contre la butée mécanique. De cette façon,
# vous ne poussez pas contre elle avec trop de force.
example_motor.run_until_stalled(-speed, duty_limit=30)

# Réinitialiser l'angle à 0. Désormais, chaque fois que l'angle est de 0, vous savez
# qu'il a atteint le point final mécanique.
example_motor.reset_angle(0)

# Maintenant, faire aller le moteur d'avant en arrière en boucle.
# Cela fonctionnera de la même manière, quel que soit
# l'angle initial du moteur, car nous commençons toujours
# à partir du point final mécanique.
for count in range(10):
    example_motor.run_target(speed, 180)
    example_motor.run_target(speed, 90)
