# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of the documentation copied and adapted from:
# https://docs.python.org/3/library/math.html
# Copyright (c) 2001-2021 Python Software Foundation


"""
Fonctions mathématiques.
"""

from typing import Tuple as Tuple


e = 2.718282
"""La constante mathématique e."""


pi = 3.141593
"""La constante mathématique π."""


def sin(x: float) -> float:
    """sin(x) -> float

    Obtient le sinus d'un angle.

    Arguments:
        x (float): Angle en radians.

    Retourne :
        Sinus de ``x``.
    """


def asin(x: float) -> float:
    """asin(x) -> float

    Applique l'opération de sinus inverse.

    Arguments:
        x (float): Opposé / hypothénuse.

    Retourne :
        Arcsinus de ``x``, en radians.
    """


def cos(x: float) -> float:
    """cos(x) -> float

    Obtient le cosinus d'un angle.

    Arguments:
        x (float): Angle en radians.

    Retourne :
        Cosinus de ``x``.
    """


def acos(x: float) -> float:
    """acos(x) -> float

    Applique l'opération de cosinus inverse.

    Arguments:
        x (float): Adjacent / hypothénuse.

    Retourne :
        Arccosinus de ``x``, en radians.
    """


def tan(x: float) -> float:
    """tan(x) -> float

    Obtient la tangente d'un angle.

    Arguments:
        x (float): Angle en radians.

    Retourne :
        Tangente de ``x``.
    """


def atan(x: float) -> float:
    """atan(x) -> float

    Applique l'opération de tangente inverse.

    Arguments:
        x (float): Opposé / adjacent.

    Retourne :
        Arctangente de ``x``, en radians.
    """


def atan2(b: float, a: float) -> float:
    """atan2(b, a) -> float

    Applique l'opération de tangente inverse sur ``b / a``, et prend en compte
    les signes de ``b`` et ``a`` pour produire l'angle attendu.

    Arguments:
        b (float): Côté opposé du triangle.
        a (float): Côté adjacent du triangle.

    Retourne :
        Arctangente de ``b / a``, en radians.
    """


def degrees(x: float) -> float:
    """degrees(x) -> float

    Convertit un angle de radians en degrés.

    Arguments:
        x (float): Angle en radians.

    Retourne :
        Angle en degrés.
    """


def radians(x: float) -> float:
    """radians(x) -> float

    Convertit un angle de degrés en radians.

    Arguments:
        x (float): Angle en degrés.

    Retourne :
        Angle en radians.
    """


def pow(x: float, y: float) -> float:
    """pow(x, y) -> float

    Obtient ``x`` élevé à la puissance de ``y``.

    Arguments:
        x (float): Le nombre de base.
        y (float): L'exposant.

    Retourne :
        ``x`` élevé à la puissance de ``y``.
    """


def exp(x: float) -> float:
    """exp(x) -> float

    Obtient :attr:`e` élevé à la puissance de ``x``.

    Arguments:
        x (float): L'exposant.

    Retourne :
        :attr:`e` élevé à la puissance de ``x``.
    """


def log(x: float) -> float:
    """log(x) -> float

    Obtient le logarithme naturel.

    Arguments:
        x (float): La valeur.

    Retourne :
        Le logarithme naturel de ``x``.
    """


def sqrt(x: float) -> float:
    """sqrt(x) -> float

    Obtient la racine carrée.

    Arguments:
        x (float): La valeur ``x``.

    Retourne :
        La racine carrée de ``x``.
    """


def ceil(x: float) -> int:
    """ceil(x) -> int

    Arrondit vers le haut.

    Arguments:
        x (float): La valeur à arrondir.

    Retourne :
        Valeur arrondie vers l'infini positif.
    """


def floor(x: float) -> int:
    """floor(x) -> int

    Arrondit vers le bas.

    Arguments:
        x (float): La valeur à arrondir.

    Retourne :
        Valeur arrondie vers l'infini négatif.
    """


def trunc(x: float) -> int:
    """trunc(x) -> int

    Tronque les décimales pour obtenir la partie entière d'une valeur.

    C'est la même chose que d'arrondir vers ``0``.

    Arguments:
        x (float): La valeur à tronquer.

    Retourne :
        Partie entière de la valeur.
    """


def fmod(x: float, y: float) -> float:
    """fmod(x, y) -> float

    Obtient le reste de ``x / y``.

    Ne pas confondre avec :func:`modf`.

    Arguments:
        x (float): Le numérateur.
        y (float): Le dénominateur.

    Retourne :
        Reste après division.
    """


def fabs(x: float) -> float:
    """fabs(x) -> float

    Obtient la valeur absolue.

    Arguments:
        x (float): La valeur.

    Retourne :
        Valeur absolue de ``x``.
    """


def modf(x: float) -> Tuple[float, float]:
    """modf(x) -> Tuple[float, float]

    Obtient les parties fractionnaire et entière de ``x``, toutes deux avec le même signe
    que ``x``.

    Ne pas confondre avec :func:`fmod`.

    Arguments:
        x (float): La valeur à décomposer.

    Retourne :
        Tuple des parties fractionnaire et entière.
    """


def frexp(x: float) -> Tuple[float, int]:
    """frexp(x) -> Tuple[float, float]

    Décompose une valeur ``x`` en un
    tuple ``(m, p)``, tel que ``x == m * (2 ** p)``.

    Arguments:
        x (float): La valeur à décomposer.

    Retourne :
        Tuple de ``m`` et ``p``.
    """


def ldexp(m: float, p: int) -> float:
    """ldexp(m, p) -> float

    Calcule ``m * (2 ** p)``.

    Arguments:
        m (float): La valeur.
        p (float): L'exposant.

    Retourne :
        Résultat de ``m * (2 ** p)``.
    """


def copysign(x: float, y: float) -> float:
    """copysign(x, y) -> float

    Obtient ``x`` avec le signe de ``y``.

    Arguments:
        x (float): Détermine la magnitude de la valeur de retour.
        y (float): Détermine le signe de la valeur de retour.

    Retourne :
        ``x`` avec le signe de ``y``.
    """


def isfinite(x: float) -> bool:
    """isfinite(x) -> bool

    Vérifie si une valeur est finie.

    Arguments:
        x (float): La valeur à vérifier.

    Retourne :
        ``True`` si ``x`` est fini, sinon ``False``.
    """


def isinfinite(x: float) -> bool:
    """isinfinite(x) -> bool

    Vérifie si une valeur est infinie.

    Arguments:
        x (float): La valeur à vérifier.

    Retourne :
        ``True`` si ``x`` est infini, sinon ``False``.
    """


def isnan(x: float) -> bool:
    """isnan(x) -> bool

    Vérifie si une valeur est non numérique.

    Arguments:
        x (float): La valeur à vérifier.

    Retourne :
        ``True`` si ``x`` est non numérique, sinon ``False``.
    """
