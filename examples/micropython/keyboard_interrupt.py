from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le moteur.
test_motor = Motor(Port.A)

# Commencer à bouger à 500 deg/s.
test_motor.run(500)

# Si vous cliquez sur la fenêtre du terminal et appuyez sur CTRL+C,
# vous pouvez continuer à déboguer dans ce terminal.
wait(5000)

# Vous pouvez également faire cela pour quitter le script et entrer dans
# le terminal. Les variables dans la portée globale sont toujours disponibles.
raise KeyboardInterrupt

# Par exemple, vous pouvez copier la ligne suivante dans le terminal
# pour obtenir l'angle, car test_motor est toujours disponible.
test_motor.angle()
