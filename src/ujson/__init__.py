# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Documentation adapted from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/json.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Convertir entre les objets Python et le format de données JSON.
"""

from typing import IO, Any, Tuple


def dump(object: Any, stream: IO, separators: Tuple[str, str] = (", ", ": ")):
    """
    dump(object, stream, separators=(", ", ": "))

    Sérialise un objet en une chaîne JSON et l'écrit dans un flux.

    Arguments:
        obj: Objet à sérialiser.
        stream: Flux dans lequel écrire la sortie.
        separators (tuple): Un tuple ``(item_separator, key_separator)`` pour
            spécifier comment les éléments doivent être séparés.
    """


def dumps(object: Any, separators: Tuple[str, str] = (", ", ": ")) -> str:
    """
    dumps(object, separators=(", ", ": "))

    Sérialise un objet en JSON et le retourne sous forme de chaîne.

    Arguments:
        obj: Objet à sérialiser.
        separators (tuple): Un tuple ``(item_separator, key_separator)`` pour
            spécifier comment les éléments doivent être séparés.

    Retourne :
        La chaîne JSON.
    """


def load(stream: IO) -> Any:
    """
    load(stream)

    Analyse le flux pour interpréter et désérialiser les données JSON en un
    objet MicroPython.

    L'analyse continue jusqu'à la fin du fichier. Une ``ValueError`` est
    levée si les données dans le flux ne sont pas correctement formées.

    Arguments:
        stream: Flux à partir duquel lire la chaîne JSON.

    Retourne :
        L'objet MicroPython désérialisé.
    """


def loads(string) -> Any:
    """
    loads(string)

    Analyse la chaîne pour interpréter et désérialiser les données JSON en un
    objet MicroPython.

    Une ``ValueError`` est levée si la chaîne n'est pas correctement formée.

    Arguments:
        string (str): Chaîne JSON à décoder.

    Retourne :
        L'objet MicroPython désérialisé.
    """
