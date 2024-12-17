#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import DataLog, StopWatch, wait

# Créer un fichier de journal de données dans le dossier du projet sur le Brick EV3.
# * Par défaut, le nom du fichier contient la date et l'heure actuelles, par exemple :
#   log_2020_02_13_10_07_44_431260.csv
# * Vous pouvez éventuellement spécifier les titres de vos colonnes de données. Par exemple,
#   si vous souhaitez enregistrer les angles du moteur à un moment donné, vous pouvez faire :
data = DataLog("time", "angle")

# Initialiser un moteur et le faire bouger
wheel = Motor(Port.B)
wheel.run(500)

# Démarrer un chronomètre pour mesurer le temps écoulé
watch = StopWatch()

# Enregistrer l'heure et l'angle du moteur 10 fois
for i in range(10):
    # Lire l'angle et l'heure
    angle = wheel.angle()
    time = watch.time()

    # Chaque fois que vous utilisez la méthode log(), une nouvelle ligne avec des données est ajoutée au
    # fichier. Vous pouvez ajouter autant de valeurs que vous le souhaitez.
    # Dans cet exemple, nous enregistrons l'heure actuelle et l'angle du moteur :
    data.log(time, angle)

    # Attendre un peu pour que le moteur puisse bouger un peu
    wait(100)

# Vous pouvez maintenant télécharger votre fichier sur votre ordinateur
