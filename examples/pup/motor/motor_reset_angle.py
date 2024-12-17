from pybricks.pupdevices import Motor
from pybricks.parameters import Port

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Réinitialiser l'angle à 0.
example_motor.reset_angle(0)

# Réinitialiser l'angle à 1234.
example_motor.reset_angle(1234)

# Réinitialiser l'angle à l'angle absolu.
# Ceci n'est pris en charge que sur les moteurs qui ont
# un encodeur absolu. Pour les autres moteurs, cela
# lèvera une erreur.
example_motor.reset_angle()
