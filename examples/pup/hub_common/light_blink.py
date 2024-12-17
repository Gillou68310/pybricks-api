# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialiser le hub
hub = ThisHub()

# Faire clignoter en rouge allumé et éteint.
hub.light.blink(Color.RED, [500, 500])

wait(10000)

# Faire clignoter en vert lentement puis rapidement.
hub.light.blink(Color.GREEN, [500, 500, 50, 900])

wait(10000)
