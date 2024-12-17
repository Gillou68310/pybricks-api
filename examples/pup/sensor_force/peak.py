from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
button = ForceSensor(Port.A)

# Cette fonction attend que le bouton soit poussé. Elle garde une trace de la force maximale
# détectée jusqu'à ce que le bouton soit relâché. Ensuite, elle retourne le maximum.
def wait_for_force():

    # Attendre une force, en ne faisant rien tant que la force est presque nulle.
    print("Waiting for force.")
    while button.force() <= 0.1:
        wait(10)

    # Maintenant, nous attendons le relâchement, en attendant que la force soit à nouveau nulle.
    print("Waiting for release.")

    # Pendant que nous attendons que cela se produise, nous continuons à lire la force et à nous souvenir
    # de la force maximale. Nous faisons cela en initialisant le maximum à 0, et
    # en le mettant à jour chaque fois que nous détectons une force plus grande.
    maximum = 0
    force = 10
    while force > 0.1:
        # Lire la force.
        force = button.force()

        # Mettre à jour le maximum si la force mesurée est plus grande.
        if force > maximum:
            maximum = force

        # Attendre puis mesurer à nouveau.
        wait(10)

    # Retourner la force maximale.
    return maximum

# Continuer à attendre que le bouton du capteur soit poussé. Lorsqu'il l'est, afficher
# la force maximale et répéter.
while True:
    peak = wait_for_force()
    print("Released. Peak force: {0} N\n".format(peak))
