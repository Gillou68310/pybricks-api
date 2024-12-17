#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

import struct

# Ce programme utilise les deux sticks PS4 pour contrôler deux moteurs servo EV3 Large
# en utilisant des commandes de type tank. Pour une carte complète de tous les boutons PS4, du pavé tactile et
# des mouvements, consultez : https://github.com/codeadamca/python-connect-ps4

# Initialiser les moteurs EV3
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_speed = 0
right_speed = 0

# Localisez le fichier d'événements auquel vous souhaitez réagir, sur mon installation, les événements des boutons du contrôleur PS4
# sont situés dans /dev/input/event4
infile_path = "/dev/input/event4"
in_file = open(infile_path, "rb")

# Définir le format des données d'événement à lire.
# https://docs.python.org/3/library/struct.html#format-characters
FORMAT = "llHHi"
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)


# Une fonction d'aide pour convertir les valeurs des sticks (0 à 255) en nombres plus utilisables
# (-100 à 100)
def scale(val, src, dst):

    result = float(val - src[0]) / (src[1] - src[0])
    result = result * (dst[1] - dst[0]) + dst[0]
    return result


# Créer une boucle pour réagir aux événements
# Cette boucle réagit à tous les événements principaux des boutons et sticks PS4. J'ai omis
# des boutons comme share et options, mais ils peuvent facilement être ajoutés en se référant
# au tableau sur : https://github.com/codeadamca/python-connect-ps4


while event:

    # Placer les données d'événement dans des variables
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)

    # Si un bouton a été pressé ou relâché
    if ev_type == 1:

        # Réagir au bouton X
        if code == 304 and value == 0:
            print("The X button was released")
        elif code == 304 and value == 1:
            print("The X button was pressed")

        # Réagir au bouton Cercle
        elif code == 305 and value == 0:
            print("The Circle button was released")
        elif code == 305 and value == 1:
            print("The Circle button was pressed")

        # Réagir au bouton Triangle
        elif code == 307 and value == 0:
            print("The Triangle button was released")
        elif code == 307 and value == 1:
            print("The Triangle button was pressed")

        # Réagir au bouton Carré
        elif code == 308 and value == 0:
            print("The Square button was released")
        elif code == 308 and value == 1:
            print("The Square button was pressed")

        # Réagir au bouton L1
        elif code == 310 and value == 0:
            print("The L1 button was released")
        elif code == 310 and value == 1:
            print("The L1 button was pressed")

        # Réagir au bouton R1
        elif code == 311 and value == 0:
            print("The R1 button was released")
        elif code == 311 and value == 1:
            print("The R1 button was pressed")

        # Réagir au bouton L2
        elif code == 312 and value == 0:
            print("The L2 button was released")
        elif code == 312 and value == 1:
            print("The L2 button was pressed")

        # Réagir au bouton R2
        elif code == 313 and value == 0:
            print("The R2 button was released")
        elif code == 313 and value == 1:
            print("The R2 button was pressed")

    elif ev_type == 3:

        # Les sticks déclenchent souvent des événements non-stop, commentez ceci si vous n'utilisez pas les sticks
        # dans votre projet, ou si cela devient difficile de lire d'autres données

        # Réagir au stick gauche vertical
        if code == 1:
            print("The left stick vertical is at ", value)
            left_speed = scale(value, (0, 255), (100, -100))

        # Réagir au stick gauche horizontal
        elif code == 0:
            print("The left stick horizontal is at ", value)

        # Réagir au stick droit vertical
        elif code == 4:
            print("The right stick vertical is at ", value)
            right_speed = scale(value, (0, 255), (100, -100))

        # Réagir au stick droit horizontal
        elif code == 3:
            print("The right stick horizontal is at ", value)

        # Réagir au pavé directionnel
        if code == 16 and value == -1:
            print("The horizontal directional pad is left")
        elif code == 16 and value == 1:
            print("The horizontal directional pad is right")
        elif code == 16 and value == 0:
            print("The horizontal directional pad is released")

        elif code == 17 and value == -1:
            print("The vertical directional pad is up")
        elif code == 17 and value == 1:
            print("The horizontal directional pad is down")
        elif code == 17 and value == 0:
            print("The horizontal directional pad is released")

    # Définir la vitesse du moteur
    left_motor.dc(left_speed)
    right_motor.dc(right_speed)

    # Lire le prochain événement
    event = in_file.read(EVENT_SIZE)

in_file.close()
