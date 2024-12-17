from pybricks.pupdevices import Remote
from pybricks.parameters import Button
from pybricks.tools import wait

# Se connecter à la télécommande.
my_remote = Remote()

while True:
    # Vérifier quels boutons sont pressés.
    pressed = my_remote.buttons.pressed()

    # Afficher le résultat.
    print("pressed:", pressed)

    # Vérifier un bouton spécifique.
    if Button.CENTER in pressed:
        print("You pressed the center button!")

    # Attendre pour voir le résultat.
    wait(100)
