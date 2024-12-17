from pybricks.pupdevices import Remote
from pybricks.tools import wait

# Se connecter à une télécommande appelée truck2.
truck_remote = Remote("truck2", timeout=None)

print("Connected!")

wait(2000)
