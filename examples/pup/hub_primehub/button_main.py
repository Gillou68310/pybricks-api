from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait

# Initialiser le hub.
hub = PrimeHub()

# Attendre qu'un bouton soit pressé, et enregistrer le résultat.
pressed = []
while not any(pressed):
    pressed = hub.buttons.pressed()
    wait(10)

# Afficher un cercle.
hub.display.icon(Icon.CIRCLE)

# Attendre que tous les boutons soient relâchés.
while any(hub.buttons.pressed()):
    wait(10)

# Afficher une flèche pour indiquer quel bouton a été pressé.
if Button.LEFT in pressed:
    hub.display.icon(Icon.ARROW_LEFT_DOWN)
elif Button.RIGHT in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_DOWN)
elif Button.BLUETOOTH in pressed:
    hub.display.icon(Icon.ARROW_RIGHT_UP)

wait(3000)
