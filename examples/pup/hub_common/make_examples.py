#!/usr/bin/env python3
"""Génère des exemples spécifiques au hub à partir d'un script modèle commun."""

import pathlib

# Créer le répertoire de construction.
dir_path = pathlib.Path(__file__).parent
build_path = dir_path / "build"
build_path.mkdir(exist_ok=True)

# Obtenir la liste des scripts à analyser.
file_paths = [f for f in dir_path.glob("*.py") if f.stem != "make_examples"]

# Parcourir tous les scripts modèles
for file_path in file_paths:

    with open(file_path) as template:

        # La première ligne contient les informations du hub
        hubs = template.readline().strip().split()[3:]

        print("Converting", template.name, "to", hubs)

        # Parcourir tous les hubs
        for hub in hubs:
            # Chemin vers le script de sortie spécifique au hub.
            gen_path = build_path / (file_path.stem + "_" + hub.lower() + ".py")

            # Réinitialiser le script source et passer l'en-tête.
            template.seek(0)
            template.readline()

            # Ouvrir le script de destination :
            with open(gen_path, "w") as dest_file:

                # Lire le script ligne par ligne.
                for line in template.readlines():

                    # Remplacer le nom du hub si présent.
                    dest_file.writelines(line.replace("ThisHub", hub))
