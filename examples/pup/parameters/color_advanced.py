
from pybricks.parameters import Color

# Deux couleurs sont égales si leurs attributs h, s et v sont égaux.
if Color.BLUE == Color(240, 100, 100):
    print("Yes, these colors are the same.")

# Vous pouvez ajuster les couleurs pour changer leur valeur de luminosité.
red_dark = Color.RED * 0.5

# Vous pouvez décaler les couleurs pour changer leur teinte.
red_shifted = Color.RED >> 30

# Les couleurs sont immuables, donc vous ne pouvez pas changer h, s ou v d'un objet existant.
try:
    Color.GREEN.h = 125
except AttributeError:
    print("Sorry, can't change the hue of an existing color object!")

# Mais vous pouvez remplacer les couleurs intégrées en définissant une toute nouvelle couleur.
Color.GREEN = Color(h=125)

# Vous pouvez accéder et stocker des couleurs en tant qu'attributs de classe, ou en tant que dictionnaire.
print(Color.BLUE)
print(Color["BLUE"])
print(Color["BLUE"] is Color.BLUE)
print(Color)
print([c for c in Color])

# Cela vous permet de mettre à jour les couleurs existantes dans une boucle.
for name in ("BLUE", "RED", "GREEN"):
    Color[name] = Color(1, 2, 3)
