# ThisHub = MoveHub CityHub TechnicHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.parameters import Color, Button
from pybricks.tools import wait, StopWatch

# Initialiser le hub.
hub = ThisHub()

# Désactiver le bouton d'arrêt.
hub.system.set_stop_button(None)

# Vérifier le bouton pendant 5 secondes.
watch = StopWatch()
while watch.time() < 5000:

    # Mettre la lumière en vert si pressé, sinon rouge.
    if hub.buttons.pressed():
        hub.light.on(Color.GREEN)
    else:
        hub.light.on(Color.RED)

# Réactiver le bouton d'arrêt.
hub.system.set_stop_button(Button.CENTER)

# Maintenant, vous pouvez appuyer sur le bouton d'arrêt comme d'habitude.
wait(5000)
