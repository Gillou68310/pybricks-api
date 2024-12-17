from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.A)

# Tout d'abord, décidez quels objets vous voulez détecter et mesurez leurs valeurs HSV.
# Vous pouvez le faire avec la méthode hsv() comme montré dans l'exemple précédent.
#
# Utilisez vos mesures pour remplacer les couleurs par défaut, ou ajouter de nouvelles couleurs :
Color.GREEN = Color(h=132, s=94, v=26)
Color.MAGENTA = Color(h=348, s=96, v=40)
Color.BROWN = Color(h=17, s=78, v=15)
Color.RED = Color(h=359, s=97, v=39)

# Mettez vos couleurs dans une liste ou un tuple.
my_colors = (Color.GREEN, Color.MAGENTA, Color.BROWN, Color.RED, Color.NONE)

# Enregistrez vos couleurs.
sensor.detectable_colors(my_colors)

# color() fonctionne comme d'habitude, mais maintenant il retourne une de vos couleurs spécifiées.
while True:
    color = sensor.color()

    # Imprimer la couleur.
    print(color)

    # Vérifiez laquelle c'est.
    if color == Color.MAGENTA:
        print("It works!")

    # Attendre pour pouvoir la lire.
    wait(100)
