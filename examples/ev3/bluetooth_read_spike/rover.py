#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port

from connection import SpikePrimeStreamReader

# Bip!
ev3 = EV3Brick()
ev3.speaker.beep()

# Créer la connexion. Voir README.md pour trouver l'adresse de votre hub SPIKE.
spike = SpikePrimeStreamReader("F4:84:4C:AA:C8:A4")

# Initialiser les moteurs et la base de conduite
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while True:
    # Lire l'orientation
    yaw, pitch, roll = spike.orientation()

    # Définir la vitesse et le taux de rotation en fonction de l'orientation
    robot.drive(-pitch * 6, roll * 2)
    wait(20)
