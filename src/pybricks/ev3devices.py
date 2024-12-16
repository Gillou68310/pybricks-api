# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""LEGO® MINDSTORMS® EV3 motors and sensors."""

from typing import Optional, Tuple, List

from . import _common
from .parameters import (
    Button as _Button,
    Color as _Color,
    Direction as _Direction,
    Port as _Port,
)


class Motor(_common.Motor):
    """Moteur LEGO® MINDSTORMS® EV3."""


class TouchSensor:
    """Capteur tactile LEGO® MINDSTORMS® EV3."""

    def __init__(self, port: _Port):
        """TouchSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def pressed(self) -> bool:
        """pressed() -> bool

        Vérifie si le capteur est pressé.

        Returns:
            ``True`` si le capteur est pressé, ``False`` s'il ne l'est pas.
        """


class ColorSensor:
    """Capteur de couleur LEGO® MINDSTORMS® EV3."""

    def __init__(self, port: _Port):
        """ColorSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def color(self) -> Optional[_Color]:
        """color() -> Color

        Mesure la couleur d'une surface.

        Returns:
            ``Color.BLACK``, ``Color.BLUE``, ``Color.GREEN``,
            ``Color.YELLOW``, ``Color.RED``, ``Color.WHITE``, ``Color.BROWN``,
            ou ``None`` si aucune couleur n'est détectée.
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Mesure l'intensité de la lumière ambiante.

        Returns:
            Intensité de la lumière ambiante, allant de 0% (sombre)
            à 100% (lumineux).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Mesure la réflexion d'une surface en utilisant une lumière rouge.

        Returns:
            Réflexion, allant de 0% (aucune réflexion) à
            100% (haute réflexion).
        """

    def rgb(self) -> Tuple[int, int, int]:
        """rgb() -> Tuple[int, int, int]

        Mesure la réflexion d'une surface en utilisant une lumière rouge, verte, puis
        bleue.

        Returns:
            Tuple de réflexions pour la lumière rouge, verte et bleue, chacune
            allant de 0,0% (aucune réflexion) à 100,0% (haute réflexion).
        """


class InfraredSensor:
    """Capteur infrarouge et balise LEGO® MINDSTORMS® EV3."""

    def __init__(self, port: _Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def distance(self) -> int:
        """distance() -> int: %

        Mesure la distance relative entre le capteur et un objet en utilisant
        la lumière infrarouge.

        Returns:
            Distance relative allant de 0% (plus proche)
            à 100% (plus éloigné).
        """

    def beacon(self, channel: int) -> Tuple[Optional[int], Optional[int]]:
        """
        beacon(channel) -> Tuple[int, int]
        beacon(channel) -> Tuple[None, None]

        Mesure la distance et l'angle relatifs entre la télécommande et le
        capteur infrarouge.

        Arguments:
            channel (int): Numéro de canal de la télécommande.

        Returns:
            Tuple de distance relative (0% à 100%) et angle approximatif
            (-75 à 75 degrés) entre la télécommande et le capteur infrarouge ou
            un tuple de (``None``, ``None``) si aucune télécommande n'est détectée.
        """

    def buttons(self, channel: int) -> List[_Button]:
        """buttons(channel) -> List[Button]

        Vérifie quels boutons de la télécommande infrarouge sont pressés.

        Cette méthode peut détecter jusqu'à deux boutons à la fois. Si vous appuyez
        sur plus de boutons, vous obtiendrez toujours seulement deux boutons.

        Arguments:
            channel (int): Numéro de canal de la télécommande.

        Returns:
            Liste des boutons pressés sur la télécommande sur le canal sélectionné.
        """

    def keypad(self) -> List[_Button]:
        """keypad() -> List[Button]

        Vérifie quels boutons de la télécommande infrarouge sont pressés.

        Cette méthode peut détecter indépendamment les 4 boutons haut/bas, mais
        elle ne peut pas détecter le bouton de la balise.

        Cette méthode ne fonctionne qu'avec la télécommande en canal 1.

        Returns:
            Liste des boutons pressés.
        """


class GyroSensor:
    """Capteur gyroscopique LEGO® MINDSTORMS® EV3."""

    def __init__(self, port: _Port, direction: _Direction = _Direction.CLOCKWISE):
        """GyroSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
            direction (Direction):
                Direction de rotation positive en regardant le point rouge sur le dessus
                du capteur.
        """

    def speed(self) -> int:
        """speed() -> int: deg/s

        Obtient la vitesse (vitesse angulaire) du capteur.

        Returns:
            Vitesse angulaire.
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Obtient l'angle accumulé du capteur.

        Returns:
            Angle de rotation.
        """

    def reset_angle(self, angle: int) -> None:
        """reset_angle(angle)

        Définit l'angle de rotation du capteur à une valeur souhaitée.

        Arguments:
            angle (Number, deg): Valeur à laquelle l'angle doit être réinitialisé.
        """


class UltrasonicSensor:
    """Capteur ultrasonique LEGO® MINDSTORMS® EV3."""

    def __init__(self, port: _Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def distance(self, silent: bool = False) -> int:
        """distance(silent=False) -> int: mm

        Mesure la distance entre le capteur et un objet en utilisant
        des ondes sonores ultrasoniques.

        Arguments:
            silent (bool): Choisissez ``True`` pour éteindre le capteur après
                           avoir mesuré la distance. Cela réduit les interférences
                           avec d'autres capteurs ultrasoniques. Si vous faites
                           cela trop fréquemment, le capteur peut se bloquer.
                           Si cela se produit, débranchez-le et rebranchez-le.

        Returns:
            Distance mesurée.
        """

    def presence(self) -> bool:
        """presence() -> bool

        Vérifie la présence d'autres capteurs ultrasoniques en détectant
        les sons ultrasoniques.

        Si l'autre capteur ultrasonique fonctionne en mode silencieux, vous pouvez
        détecter sa présence uniquement lorsqu'il prend une
        mesure.

        Returns:
            ``True`` si des sons ultrasoniques sont détectés,
            ``False`` sinon.
        """
