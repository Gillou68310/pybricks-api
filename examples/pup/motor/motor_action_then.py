from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Initialiser un moteur sur le port A.
example_motor = Motor(Port.A)

# Par défaut, le moteur maintient la position. Il continue
# de corriger l'angle si vous le déplacez.
example_motor.run_angle(500, 360)
wait(1000)

# Cela fait exactement la même chose que ci-dessus.
example_motor.run_angle(500, 360, then=Stop.HOLD)
wait(1000)

# Vous pouvez également freiner. Cela applique une certaine résistance
# mais le moteur ne revient pas en arrière si vous le déplacez.
example_motor.run_angle(500, 360, then=Stop.BRAKE)
wait(1000)

# Cela permet au moteur de rouler librement après son arrêt.
example_motor.run_angle(500, 360, then=Stop.COAST)
wait(1000)
