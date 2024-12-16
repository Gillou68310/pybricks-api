# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/random.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
Ce module implémente des générateurs de nombres pseudo-aléatoires.

Toutes les fonctions de ce module doivent être utilisées avec des arguments positionnels. Les arguments
nommés ne sont pas pris en charge.
"""

from typing import Any, Optional, Sequence, overload


def seed(a: Optional[int] = None) -> None:
    """
    seed(value=None)

    Initialise le générateur de nombres aléatoires.

    Cela est appelé lorsque le module est importé, donc normalement vous n'avez
    pas besoin d'appeler cette fonction.

    Arguments:
        value: Valeur de la graine. Lors de l'utilisation de ``None``, le timer système sera utilisé.
    """


@overload
def randrange(stop: int) -> int:
    ...


@overload
def randrange(start: int, stop: int) -> int:
    ...


@overload
def randrange(start: int, stop: int, step: int) -> int:
    ...


def randrange(start, stop, step):
    """
    randrange(stop) -> int
    randrange(start, stop) -> int
    randrange(start, stop, step) -> int

    Retourne un élément sélectionné aléatoirement de ``range(start, stop, step)``.

    Par exemple, ``randrange(1, 7, 2)`` retourne des nombres aléatoires de ``1`` à
    (mais excluant) ``7``, par incréments de ``2``. En d'autres termes, cela
    retourne ``1``, ``3`` ou ``5``.

    Arguments:
        start (int): Valeur la plus basse. Par défaut ``0`` si un seul argument est donné.
        stop (int): Valeur la plus haute. Cette valeur n'est *pas* incluse dans la plage.
        step (int): Incrément entre les valeurs. Par défaut ``1`` si un seul
            ou deux arguments sont donnés.

    Retourne :
        Le nombre aléatoire.
    """


def randint(a: int, b: int) -> int:
    """
    randint(a, b) -> int

    Obtient un entier aléatoire :math:`N` satisfaisant :math:`a \\leq N \\leq b`.

    Arguments:
        a (int): Valeur la plus basse. Cette valeur *est* incluse dans la plage.
        b (int): Valeur la plus haute. Cette valeur *est* incluse dans la plage.

    Retourne :
        L'entier aléatoire.
    """


def getrandbits(k: int) -> int:
    """
    getrandbits(k) -> int

    Obtient un entier aléatoire :math:`N` satisfaisant :math:`0 \\leq N < 2^{\\text{k}}`.

    Arguments:
        k (int): Combien de bits utiliser pour le résultat.
    """


def choice(seq: Sequence[Any]) -> Any:
    """
    choice(sequence) -> Any

    Obtient un élément aléatoire d'une séquence telle qu'un tuple ou une liste.

    Arguments:
        sequence: Séquence à partir de laquelle sélectionner un élément aléatoire.

    Retourne :
        L'élément sélectionné aléatoirement.

    Lève :
        ``IndexError``: Si la séquence est vide.
    """


def random() -> float:
    """
    random() -> float

    Obtient une valeur aléatoire :math:`x` satisfaisant :math:`0 \\leq x < 1`.

    Retourne :
        La valeur aléatoire.
    """


def uniform(a: float, b: float) -> float:
    """
    uniform(a, b) -> float

    Obtient une valeur à virgule flottante aléatoire :math:`x` satisfaisant :math:`a \\leq x \\leq b`.

    Arguments:
        a (float): Valeur la plus basse.
        b (float): Valeur la plus haute.

    Retourne :
        La valeur aléatoire.
    """
