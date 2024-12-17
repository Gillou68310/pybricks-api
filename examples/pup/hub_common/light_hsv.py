# ThisHub = CityHub TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialiser le hub.
hub = ThisHub()

# Afficher la couleur à 30% de luminosité.
hub.light.on(Color.RED * 0.3)

wait(2000)

# Utiliser votre propre couleur personnalisée.
hub.light.on(Color(h=30, s=100, v=50))

wait(2000)

# Parcourir toutes les couleurs.
for hue in range(360):
    hub.light.on(Color(hue))
    wait(10)
