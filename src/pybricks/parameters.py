# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Paramètres/arguments constants pour l'API Pybricks."""

from __future__ import annotations

from enum import Enum
from typing import Union, TYPE_CHECKING
import os

from .tools import Matrix as _Matrix, vector as _vector

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = Union[int, float]
    """
    Les nombres peuvent être représentés comme des entiers ou des valeurs à virgule flottante :

        * Les entiers (:class:`int <ubuiltins.int>`) sont des nombres entiers
          comme ``15`` ou ``-123``.
        * Les valeurs à virgule flottante (:class:`float <ubuiltins.float>`) sont des nombres décimaux
          comme ``3.14`` ou ``-123.45``.

    Si vous voyez :class:`Number` comme type d'argument, les deux
    :class:`int <ubuiltins.int>` et :class:`float <ubuiltins.float>` peuvent être utilisés.

    Par exemple, :func:`wait(15) <pybricks.tools.wait>` et
    :func:`wait(15.75) <pybricks.tools.wait>` sont tous deux autorisés. Dans la plupart des fonctions,
    cependant, votre valeur d'entrée sera tronquée à un nombre entier de toute façon. Dans cet
    exemple, l'une ou l'autre commande fait que le programme s'arrête pendant seulement 15 millisecondes.

    .. note::
        Le hub BOOST Move ne prend pas en charge les nombres à virgule flottante en raison
        de ressources système limitées. Seuls les entiers peuvent être utilisés sur ce hub.
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Axis:
    """Axes unitaires d'un système de coordonnées.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """

    X: _Matrix = _vector(1, 0, 0)
    Y: _Matrix = _vector(0, 1, 0)
    Z: _Matrix = _vector(0, 0, 1)


class Color:
    """Couleur de la lumière ou de la surface."""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Teinte.
            s (Number, %): Saturation.
            v (Number, %): Valeur de luminosité.
        """

        self.h = int(h) % 360
        """
        La teinte.
        """

        self.s = max(0, min(int(s), 100))
        """
        La saturation.
        """

        self.v = max(0, min(int(v), 100))
        """
        La valeur de luminosité.
        """

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool: ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """Port sur la brique programmable ou le hub."""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """Action après que le moteur s'arrête ou atteint sa cible."""

    COAST: Stop = 0
    """Laisser le moteur se déplacer librement."""

    COAST_SMART: Stop = 4
    """
    Laisser le moteur se déplacer librement. Pour la prochaine manœuvre d'angle relatif,
    prendre le dernier angle cible (au lieu de l'angle actuel) comme nouveau
    point de départ. Cela réduit les erreurs cumulatives. Cela s'appliquera uniquement si
    l'angle actuel est inférieur à deux fois la tolérance de position configurée.
    """

    BRAKE: Stop = 1
    """Résister passivement aux petites forces externes."""

    HOLD: Stop = 2
    """Continuer à contrôler le moteur pour le maintenir à l'angle commandé."""

    NONE: Stop = 3
    """
    Ne pas décélérer en approchant de la position cible. Cela peut être utilisé
    pour enchaîner plusieurs manœuvres de moteur ou de base mobile sans s'arrêter. Si
    aucune autre commande n'est donnée, le moteur continuera à fonctionner indéfiniment
    à la vitesse donnée.
    """


class Direction(_PybricksEnum):
    """Direction de rotation pour les valeurs de vitesse ou d'angle positives."""

    CLOCKWISE: Direction = 0
    """Une valeur de vitesse positive doit faire tourner le moteur dans le sens horaire."""

    COUNTERCLOCKWISE: Direction = 1
    """Une valeur de vitesse positive doit faire tourner le moteur dans le sens antihoraire."""


class Button(_PybricksEnum):
    """Boutons sur un hub ou une télécommande."""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9
    A: Button = 0
    B: Button = 0
    X: Button = 0
    Y: Button = 0
    LB: Button = 0
    RB: Button = 0
    LJ: Button = 0
    RJ: Button = 0
    P1: Button = 0
    P2: Button = 0
    P3: Button = 0
    P4: Button = 0
    GUIDE: Button = 0
    MENU: Button = 0
    UPLOAD: Button = 0
    VIEW: Button = 0


class Side(_PybricksEnum):
    """Côté d'un hub ou d'un capteur."""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    """Icônes à afficher sur une matrice lumineuse.

    Chacune des attributs suivants est une matrice. Cela signifie que vous pouvez
    redimensionner les icônes pour ajuster la luminosité ou ajouter des icônes pour créer des composites.
    """

    UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    """
    DOWN: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨🟨
    | ⬜⬜🟨⬜⬜
    """
    RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | 🟨🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT_UP: _Matrix = ...
    """
    | ⬜⬜🟨🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    | 🟨⬜⬜⬜⬜
    """
    ARROW_RIGHT_DOWN: _Matrix = ...
    """
    | 🟨⬜⬜⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨🟨🟨
    """
    ARROW_LEFT_UP: _Matrix = ...
    """
    | 🟨🟨🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | ⬜⬜⬜⬜🟨
    """
    ARROW_LEFT_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨🟨⬜⬜
    """
    ARROW_UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜🟨⬜🟨
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_DOWN: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    | 🟨⬜🟨⬜🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    HAPPY: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | 🟨⬜⬜⬜🟨
    | ⬜🟨🟨🟨⬜
    """
    SAD: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜⬜⬜🟨
    """
    EYE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW_UP: _Matrix = ...
    """
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW_UP: _Matrix = ...
    """
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    HEART: _Matrix = ...
    """
    | ⬜🟨⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    PAUSE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    EMPTY: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FULL: _Matrix = ...
    """
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    """
    SQUARE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_RIGHT: _Matrix = ...
    """
    | ⬜🟨⬜⬜⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    """
    TRIANGLE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜⬜⬜🟨⬜
    """
    TRIANGLE_UP: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    CIRCLE: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    """
    CLOCKWISE: _Matrix = ...
    """
    | 🟨🟨🟨🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    """
    COUNTERCLOCKWISE: _Matrix = ...
    """
    | ⬜🟨🟨🟨🟨
    | ⬜🟨⬜⬜🟨
    | ⬜🟨⬜⬜🟨
    | 🟨🟨🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    """
    TRUE: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FALSE: _Matrix = ...
    """
    | 🟨⬜⬜⬜🟨
    | ⬜🟨⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜🟨⬜
    | 🟨⬜⬜⬜🟨
    """
