from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Initialiser le hub.
hub = PrimeHub()

# Afficher une grande flèche pointant vers le haut.
hub.display.icon(Icon.UP)

# Attendre pour voir ce qui est affiché.
wait(2000)

# Afficher un cœur à moitié de luminosité.
hub.display.icon(Icon.HEART / 2)

# Attendre pour voir ce qui est affiché.
wait(2000)
