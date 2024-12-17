from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

# Initialiser le hub.
hub = PrimeHub()

# Configurer la combinaison de boutons d'arrêt. Maintenant, votre programme s'arrête
# si vous appuyez simultanément sur les boutons central et Bluetooth.
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# Maintenant, nous pouvons utiliser le bouton central comme un bouton normal.
while True:

    # Jouer un son si le bouton central est pressé.
    if Button.CENTER in hub.buttons.pressed():
        hub.speaker.beep()
