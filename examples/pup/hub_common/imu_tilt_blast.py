# ThisHub = TechnicHub PrimeHub EssentialHub
from pybricks.hubs import ThisHub
from pybricks.tools import wait
from pybricks.parameters import Axis

# Initialiser le hub. Dans ce cas, spécifiez que le hub est monté avec le
# côté supérieur vers l'avant et le côté avant vers la droite.
# Par exemple, c'est ainsi que le hub est monté dans BLAST dans le set 51515.
hub = ThisHub(top_side=Axis.X, front_side=-Axis.Y)

while True:
    # Lire les valeurs d'inclinaison. Maintenant, les valeurs sont 0 lorsque BLAST est debout.
    # Pencher vers l'avant donne un tangage positif. Pencher vers la droite donne un roulis positif.
    pitch, roll = hub.imu.tilt()

    # Imprimer le résultat.
    print(pitch, roll)
    wait(200)
