from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task

# Configurer tous les appareils.
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B)
gripper = Motor(Port.C)
drive_base = DriveBase(left, right, 56, 114)

# Déplacer la pince vers le haut et vers le bas.
async def move_gripper():
    await gripper.run_angle(500, -90)
    await gripper.run_angle(500, 90)

# Conduire en avant, tourner, déplacer la pince en même temps, et conduire en arrière.
async def main():
    await drive_base.straight(250)
    await multitask(drive_base.turn(90), move_gripper())
    await drive_base.straight(-250)

# Exécute le programme principal du début à la fin.
run_task(main())
