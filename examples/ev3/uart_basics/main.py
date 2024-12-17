#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import UARTDevice
from pybricks.parameters import Port
from pybricks.media.ev3dev import SoundFile

# Initialiser l'EV3
ev3 = EV3Brick()

# Initialiser le port de capteur 2 comme un périphérique UART
ser = UARTDevice(Port.S2, baudrate=115200)

# Écrire des données
ser.write(b"\r\nHello, world!\r\n")

# Jouer un son pendant que nous attendons des données
for i in range(3):
    ev3.speaker.play_file(SoundFile.HELLO)
    ev3.speaker.play_file(SoundFile.GOOD)
    ev3.speaker.play_file(SoundFile.MORNING)
    print("Bytes waiting to be read:", ser.waiting())

# Lire toutes les données reçues pendant que le son jouait
data = ser.read_all()
print(data)
