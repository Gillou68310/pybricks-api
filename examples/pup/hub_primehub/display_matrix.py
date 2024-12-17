from pybricks.hubs import PrimeHub
from pybricks.tools import wait, Matrix

# Initialiser le hub.
hub = PrimeHub()

# Faire un carré lumineux à l'extérieur et faible au milieu.
SQUARE = Matrix(
    [
        [100, 100, 100, 100, 100],
        [100, 50, 50, 50, 100],
        [100, 50, 0, 50, 100],
        [100, 50, 50, 50, 100],
        [100, 100, 100, 100, 100],
    ]
)

# Afficher le carré.
hub.display.icon(SQUARE)
wait(3000)

# Créer une image en utilisant une compréhension de liste Python. Dans cette image,
# la luminosité de chaque pixel est la somme de l'index de la ligne et de la colonne.
# Ainsi, la lumière est faible en haut à gauche et brillante en bas à droite.
GRADIENT = Matrix([[(r + c) for c in range(5)] for r in range(5)]) * 12.5

# Afficher le gradient généré.
hub.display.icon(GRADIENT)
wait(3000)
