from pybricks.pupdevices import Remote
from pybricks.parameters import Color
from pybricks.tools import wait

# Se connecter à la télécommande.
remote = Remote()

while True:
    # Définir la couleur sur rouge.
    remote.light.on(Color.RED)
    wait(1000)

    # Définir la couleur sur bleu.
    remote.light.on(Color.BLUE)
    wait(1000)
