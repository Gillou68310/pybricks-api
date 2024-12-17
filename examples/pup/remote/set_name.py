from pybricks.pupdevices import Remote

# Se connecter à n'importe quelle télécommande.
my_remote = Remote()

# Imprimer le nom actuel de la télécommande.
print(my_remote.name())

# Choisir un nouveau nom.
my_remote.name("truck2")

print("Done!")
