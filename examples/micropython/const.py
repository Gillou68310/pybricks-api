from micropython import const

# Cette valeur peut être utilisée ici. D'autres fichiers peuvent l'importer aussi.
APPLES = const(123)

# Ces valeurs ne peuvent être utilisées que dans ce fichier.
_ORANGES = const(1 << 8)
_BANANAS = const(789 + _ORANGES)

# Vous pouvez lire les constantes comme des valeurs normales. Le compilateur
# insérera simplement les valeurs numériques pour vous.
fruit = APPLES + _ORANGES + _BANANAS
print(fruit)
