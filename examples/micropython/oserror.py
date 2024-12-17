from pybricks.pupdevices import Motor
from pybricks.parameters import Port

from uerrno import ENODEV

try:
    # Essayez d'initialiser un moteur.
    my_motor = Motor(Port.A)

    # Si tout se passe bien, vous verrez ce message.
    print("Detected a motor.")
except OSError as ex:
    # Si une OSError a été levée, nous pouvons vérifier quel
    # type d'erreur c'était, comme ENODEV.
    if ex.errno == ENODEV:
        # ENODEV est l'abréviation de "Erreur, pas de dispositif."
        print("There is no motor this port.")
    else:
        print("Another error occurred.")
