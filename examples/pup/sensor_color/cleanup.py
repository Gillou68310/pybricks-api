from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorSensor(Port.A)

def main():
    # Exécuter le code principal.
    while True:
        print(sensor.color())
        wait(500)

# Enveloppez le code principal dans un try/finally pour que le code de nettoyage s'exécute toujours
# lorsque le programme se termine, même si une exception a été levée.
try:
    main()
finally:
    # Le code de nettoyage va ici.
    print("Cleaning up.")
    sensor.lights.off()
