from micropython import const, opt_level, mem_info, qstr_info, stack_use

# Obtenir la pile au démarrage.
stack_start = stack_use()

# Afficher le niveau d'optimisation du compilateur REPL.
print("level", opt_level())

# Afficher l'utilisation de la mémoire.
mem_info()

# Afficher l'utilisation de la mémoire et une carte mémoire.
mem_info(True)

# Afficher les informations sur les chaînes internées.
qstr_info()

# Afficher les informations sur les chaînes internées et leurs noms.
APPLES = const(123)
_ORANGES = const(456)
qstr_info(True)

def test_stack():
    return stack_use()

# Vérifier la pile.
print("Stack diff: ", test_stack() - stack_start)
