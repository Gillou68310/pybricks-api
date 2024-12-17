def wait_for_button(ev3):
    """
    Cette fonction affiche une image des boutons sur l'écran EV3.

    Ensuite, elle attend que vous appuyiez sur un bouton.

    Elle renvoie quel bouton a été pressé.
    """

    # Afficher une image des boutons sur l'écran.
    ev3.screen.load_image("buttons.png")

    # Astuce : ajoutez du texte ou des icônes à l'image pour vous aider
    # à vous rappeler ce que chaque bouton fera dans votre programme.

    # Attendre qu'un seul bouton soit pressé et enregistrer le résultat.
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # Afficher quel bouton a été pressé
    ev3.screen.draw_text(2, 100, button)

    # Maintenant, attendez que le bouton soit relâché.
    while any(ev3.buttons.pressed()):
        pass

    # Retourner quel bouton a été pressé.
    return button
