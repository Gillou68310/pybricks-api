from pybricks.tools import wait

print("Started!")

try:

    # Exécutez votre script ici comme vous le feriez normalement. Dans cet
    # exemple, nous attendons simplement indéfiniment et ne faisons rien.
    while True:
        wait(1000)

except SystemExit:
    # Ce code s'exécutera lorsque vous appuyez sur le bouton d'arrêt.
    # Cela peut être utile pour "nettoyer", comme pour ramener
    # les moteurs à leurs positions de départ.
    print("You pressed the stop button!")
