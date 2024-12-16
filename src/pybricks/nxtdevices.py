# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Utilisez les moteurs et capteurs LEGO® MINDSTORMS® NXT avec le brique EV3."""


from .parameters import Port

from ._common import ColorLight, CommonColorSensor
from .iodevices import AnalogSensor


from typing import Callable, Optional, Tuple


class TouchSensor:
    """Capteur tactile LEGO® MINDSTORMS® NXT."""

    def __init__(self, port: Port):
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


class LightSensor:
    """Capteur de lumière LEGO® MINDSTORMS® NXT."""

    def __init__(self, port: Port):
        """LightSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def ambient(self) -> int:
        """ambient() -> int: %

        Mesure l'intensité de la lumière ambiante.

        Returns:
            Intensité de la lumière ambiante, allant de 0% (sombre) à 100% (lumineux).
        """

    def reflection(self) -> int:
        """reflection() -> int: %

        Mesure la réflexion d'une surface en utilisant une lumière rouge.

        Returns:
            Réflexion, allant de 0% (aucune réflexion) à 100% (haute réflexion).
        """


class ColorSensor(CommonColorSensor):
    """Capteur de couleur LEGO® MINDSTORMS® NXT."""

    light = ColorLight()

    def rgb(self) -> Tuple[int, int, int]:
        """Mesure la réflexion d'une surface en utilisant une lumière rouge, verte, puis une
        lumière bleue.

        Returns:
            Tuple de réflexions pour la lumière rouge, verte et bleue, chacune
            allant de 0,0% (aucune réflexion) à 100,0% (haute réflexion).
        """


class UltrasonicSensor:
    """Capteur ultrasonique LEGO® MINDSTORMS® NXT."""

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Mesure la distance entre le capteur et un objet en utilisant
        des ondes sonores ultrasoniques.

        Returns:
            Distance mesurée.
        """


class SoundSensor:
    """Capteur sonore LEGO® MINDSTORMS® NXT."""

    def __init__(self, port: Port):
        """SoundSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def intensity(self, audible_only: bool = True) -> int:
        """intensity(audible_only=True) -> int: %

        Mesure l'intensité sonore ambiante (volume).

        Arguments:
            audible_only (bool): Détecte uniquement les sons audibles. Cela essaie de
                filtrer les fréquences qui ne peuvent pas être entendues par l'oreille
                humaine.

        Returns:
            Intensité sonore.
        """


class TemperatureSensor:
    """Capteur de température LEGO® MINDSTORMS® NXT."""

    def __init__(self, port: Port):
        """TemperatureSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def temperature(self) -> int:
        """temperature() -> float: °C

        Mesure la température.

        Returns:
            Température mesurée.
        """


class EnergyMeter:
    """Compteur d'énergie LEGO® MINDSTORMS® Education NXT."""

    def __init__(self, port: Port):
        """EnergyMeter(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def storage(self) -> int:
        """storage() -> int: J

        Obtient l'énergie totale disponible stockée dans la batterie.

        Returns:
            Énergie stockée restante.
        """

    def input(self) -> Tuple[int, int, int]:
        """input() -> Tuple[int, int, int]

        Mesure les signaux électriques à l'entrée (côté inférieur)
        du compteur d'énergie. Il mesure la tension appliquée et le
        courant qui le traverse. Le produit de ces deux valeurs est la puissance.
        Cette valeur de puissance est le taux auquel l'énergie stockée augmente. Cette
        puissance est fournie par une source d'énergie telle que le panneau solaire fourni
        ou un moteur entraîné de manière externe.

        Returns:
            Tension (mV), courant (mA) et puissance (mW) mesurés à l'entrée
            du port.
        """

    def output(self) -> Tuple[int, int, int]:
        """output() -> Tuple[int, int, int]

        Mesure les signaux électriques à la sortie (côté supérieur)
        du compteur d'énergie. Il mesure la tension appliquée à la charge externe
        et le courant qui y passe. Le produit de ces deux valeurs
        est la puissance. Cette valeur de puissance est le taux auquel l'énergie stockée
        diminue. Cette puissance est consommée par la charge, telle qu'une lumière ou un
        moteur.

        Returns:
            Tension (mV), courant (mA) et puissance (mW) mesurés à la sortie
            du port.
        """


class VernierAdapter(AnalogSensor):
    """Adaptateur LEGO® MINDSTORMS® Education NXT/EV3 pour capteurs Vernier."""

    def __init__(self, port: Port, conversion: Optional[Callable[[int], float]] = None):
        """VernierAdapter(port, conversion=None)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
            conversion (callable): Fonction du format :meth:`.conversion`.
                Cette fonction est utilisée pour convertir la tension analogique brute en la
                valeur de sortie spécifique au capteur. Chaque capteur Vernier a sa
                propre fonction de conversion. L'exemple donné ci-dessous démontre
                la conversion pour le capteur de température de surface.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Mesure la tension brute du capteur analogique.

        Returns:
            Tension analogique.
        """

    def conversion(self, voltage: int) -> float:
        """conversion(voltage) -> float

        Convertit la tension brute (mV) en une valeur de capteur.

        Si vous n'avez pas fourni de fonction :meth:`.conversion` plus tôt, aucune
        conversion ne sera appliquée.

        Arguments:
            voltage (Number, mV): Tension du capteur analogique

        Returns:
            Valeur convertie du capteur.
        """

    def value(self) -> float:
        """value() -> float

        Mesure la :meth:`.voltage` du capteur puis
        applique votre :meth:`.conversion` pour vous donner la valeur du capteur.

        Returns:
            Valeur convertie du capteur.
        """
