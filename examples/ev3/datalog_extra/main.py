#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color
from pybricks.tools import DataLog

# Créer un fichier de journal de données appelé my_file.txt
data = DataLog("time", "angle", name="my_file", timestamp=False, extension="txt")

# La méthode log utilise la méthode print() pour ajouter une ligne de texte.
# Donc, vous pouvez faire bien plus que sauvegarder des nombres. Par exemple :
data.log("Temperature", 25)
data.log("Sunday", "Monday", "Tuesday")
data.log({"Kiwi": Color.GREEN}, {"Banana": Color.YELLOW})

# Vous pouvez télécharger le fichier sur votre ordinateur, mais vous pouvez aussi imprimer les données :
print(data)
