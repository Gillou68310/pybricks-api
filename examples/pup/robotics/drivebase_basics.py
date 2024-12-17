from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialiser les deux moteurs. Dans cet exemple, le moteur sur la
# gauche doit tourner dans le sens antihoraire pour que le robot avance.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialiser la base de conduite. Dans cet exemple, le diamètre de la roue est de 56mm.
# La distance entre les deux points de contact roue-sol est de 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Optionnellement, décommentez la ligne ci-dessous pour utiliser le gyroscope pour une meilleure précision.
# drive_base.use_gyro(True)

# Conduire en avant de 500mm (un demi-mètre).
drive_base.straight(500)

# Faire demi-tour dans le sens horaire de 180 degrés.
drive_base.turn(180)

# Conduire en avant à nouveau pour revenir au point de départ.
drive_base.straight(500)

# Faire demi-tour dans le sens antihoraire.
drive_base.turn(-180)
