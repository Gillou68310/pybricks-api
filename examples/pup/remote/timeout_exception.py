from pybricks.pupdevices import Remote

try:
    # Chercher une télécommande pendant 5 secondes.
    my_remote = Remote(timeout=5000)

    print("Connected!")

    # Ici, vous pouvez écrire du code qui utilise la télécommande.

except OSError:

    print("Could not find the remote.")

    # Ici, vous pouvez faire faire quelque chose à votre robot
    # sans la télécommande.
