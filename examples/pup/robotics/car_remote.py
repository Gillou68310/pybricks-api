from pybricks.parameters import Direction, Port, Button
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# Configurer les moteurs.
front = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
steer = Motor(Port.C, Direction.CLOCKWISE)

# Se connecter à la télécommande.
remote = Remote()

# Configurer la voiture.
car = Car(steer, [front, rear])

# Le programme principal commence ici.
while True:
    # Lire l'état de la télécommande.
    pressed = remote.buttons.pressed()

    # Diriger en utilisant le pavé gauche. La direction est le pourcentage
    # de l'angle déterminé lors de l'initialisation.
    steering = 0
    if Button.LEFT_PLUS in pressed:
        steering += 100
    elif Button.LEFT_MINUS in pressed:
        steering -= 100
    car.steer(steering)

    # Conduire en utilisant le pavé droit.
    power = 0
    if Button.RIGHT_PLUS in pressed:
        power += 100
    elif Button.RIGHT_MINUS in pressed:
        power -= 100
    car.drive_power(power)

    # Attendre brièvement.
    wait(10)
