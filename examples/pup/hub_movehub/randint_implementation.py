from pybricks.hubs import MoveHub

# Initialiser le hub.
hub = MoveHub()

# Initialiser la graine "aléatoire".
_rand = hub.battery.voltage() + hub.battery.current()

# Retourner un entier aléatoire N tel que a <= N <= b.
def randint(a, b):
    global _rand
    _rand = 75 * _rand % 65537  # Lehmer
    return _rand * (b - a + 1) // 65537 + a

# Générer quelques nombres d'exemple.
for i in range(5):
    print(randint(0, 1000))
