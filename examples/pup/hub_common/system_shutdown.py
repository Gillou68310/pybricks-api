# ThisHub = MoveHub CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub()

# Dire au revoir et donner du temps pour l'envoyer.
print("Goodbye!")
wait(100)

# Éteindre le hub.
hub.system.shutdown()
