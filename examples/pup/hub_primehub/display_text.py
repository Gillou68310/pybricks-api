from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

# Afficher la lettre A pendant deux secondes.
hub.display.char("A")
wait(2000)

# Afficher du texte, une lettre à la fois.
hub.display.text("Hello, world!")
