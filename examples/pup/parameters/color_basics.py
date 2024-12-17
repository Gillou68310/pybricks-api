from pybricks.parameters import Color

# Vous pouvez imprimer des couleurs. Les couleurs peuvent être obtenues à partir de la classe Color, ou
# à partir de capteurs qui renvoient des mesures de couleur.
print(Color.RED)

# Vous pouvez lire les propriétés de teinte, saturation et valeur.
print(Color.RED.h, Color.RED.s, Color.RED.v)

# Vous pouvez créer vos propres couleurs. La saturation et la valeur sont de 100 par défaut.
my_green = Color(h=125)
my_dark_green = Color(h=125, s=80, v=30)

# Lorsque vous imprimez des couleurs personnalisées, vous voyez exactement comment elles ont été définies.
print(my_dark_green)

# Vous pouvez également ajouter des couleurs aux couleurs intégrées.
Color.MY_DARK_BLUE = Color(h=235, s=80, v=30)

# Lorsque vous les ajoutez de cette manière, les imprimer ne montre que leur nom. Mais vous pouvez
# toujours lire h, s, v en lisant ses attributs.
print(Color.MY_DARK_BLUE)
print(Color.MY_DARK_BLUE.h, Color.MY_DARK_BLUE.s, Color.MY_DARK_BLUE.v)
