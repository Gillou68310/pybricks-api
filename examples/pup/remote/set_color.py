from pybricks.pupdevices import Remote
from pybricks.parameters import Button, Color


def button_to_color(buttons):

    # Retourner une couleur en fonction du bouton.
    if Button.LEFT_PLUS in buttons:
        return Color.RED
    if Button.LEFT_MINUS in buttons:
        return Color.GREEN
    if Button.LEFT in buttons:
        return Color.ORANGE
    if Button.RIGHT_PLUS in buttons:
        return Color.BLUE
    if Button.RIGHT_MINUS in buttons:
        return Color.YELLOW
    if Button.RIGHT in buttons:
        return Color.CYAN
    if Button.CENTER in buttons:
        return Color.VIOLET

    # Retourner aucune couleur par défaut.
    return Color.NONE


# Se connecter à la télécommande.
remote = Remote()

while True:
    # Attendre qu'un bouton soit pressé.
    pressed = ()
    while not pressed:
        pressed = remote.buttons.pressed()

    # Convertir le code du bouton en couleur.
    color = button_to_color(pressed)

    # Définir la couleur de la lumière de la télécommande.
    remote.light.on(color)

    # Attendre que tous les boutons soient relâchés.
    while pressed:
        pressed = remote.buttons.pressed()
