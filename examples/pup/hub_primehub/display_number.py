from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

# Compter de 0 à 99.
for i in range(100):
    hub.display.number(i)
    wait(200)
