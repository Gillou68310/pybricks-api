# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Powered Up motor, sensors, and lights."""

from __future__ import annotations

from typing import TYPE_CHECKING, Collection, Optional, Union, overload

from . import _common
from .parameters import Button, Color, Direction

if TYPE_CHECKING:
    from ._common import (
        MaybeAwaitable,
        MaybeAwaitableBool,
        MaybeAwaitableFloat,
        MaybeAwaitableInt,
        MaybeAwaitableTuple,
    )
    from .parameters import Number, Port


class DCMotor(_common.DCMotor):
    """Moteur LEGO® Powered Up sans capteurs de rotation."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port auquel le moteur est connecté.
            positive_direction (Direction): La direction dans laquelle le moteur doit
                tourner lorsque vous donnez une valeur de cycle de service positive.
        """


class Motor(_common.Motor):
    """Moteur LEGO® Powered Up avec capteurs de rotation."""

    # HACK: jedi can't find inherited __init__ so we have to duplicate docs
    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Port auquel le moteur est connecté.
            positive_direction (Direction): La direction dans laquelle le moteur doit
                tourner lorsque vous donnez une valeur de vitesse ou
                d'angle positive.
            gears (list):
                Liste des engrenages reliés au moteur. L'engrenage connecté
                au moteur vient en premier et l'engrenage connecté à la sortie
                vient en dernier.

                Par exemple : ``[12, 36]`` représente un train d'engrenages avec un
                engrenage de 12 dents connecté au moteur et un engrenage de 36 dents
                connecté à la sortie. Utilisez une liste de listes pour plusieurs
                trains d'engrenages, comme ``[[12, 36], [20, 16, 40]]``.

                Lorsque vous spécifiez un train d'engrenages, toutes les commandes et réglages
                du moteur sont automatiquement ajustés pour tenir compte du rapport de réduction
                résultant. La direction du moteur reste inchangée par cela.
            reset_angle (bool):
                Choisissez ``True`` pour réinitialiser la valeur du capteur de rotation à l'angle
                du marqueur absolu (entre -180 et 179).
                Choisissez ``False`` pour conserver la
                valeur actuelle, afin que votre programme sache où il s'est arrêté la dernière
                fois.
            profile (Number, deg): Profil de précision. Il s'agit de la tolérance de position
                approximative en degrés qui est acceptable dans votre application. Une valeur plus
                basse donne un mouvement plus précis mais plus erratique ; une valeur plus élevée
                donne un mouvement moins précis mais plus fluide. Si aucune valeur n'est donnée,
                un profil adapté à ce type de moteur sera sélectionné automatiquement (environ 11 degrés).
        """

    def reset_angle(self, angle: Optional[Number] = None) -> None:
        """reset_angle(angle=None)

        Définit l'angle de rotation accumulé du moteur à une valeur souhaitée.

        Si vous ne spécifiez pas d'angle, l'angle absolu
        sera utilisé si votre moteur le prend en charge.

        Arguments:
            angle (Number, deg): Valeur à laquelle l'angle doit être réinitialisé.
        """


class Remote:
    """Télécommande Bluetooth LEGO® Powered Up."""

    light = _common.ExternalColorLight()
    buttons = _common.Keypad(
        (
            Button.LEFT_MINUS,
            Button.RIGHT_MINUS,
            Button.LEFT,
            Button.CENTER,
            Button.RIGHT,
            Button.LEFT_PLUS,
            Button.RIGHT_PLUS,
        )
    )
    address: Union[str, None]

    def __init__(self, name: Optional[str] = None, timeout: int = 10000):
        """Remote(name=None, timeout=10000)

        Lorsque vous instanciez cette classe, le hub recherchera une télécommande
        et se connectera automatiquement.

        La télécommande doit être allumée et prête pour une connexion, comme indiqué par une
        lumière blanche clignotante.

        Arguments:
            name (str): Nom Bluetooth de la télécommande. Si aucun nom n'est donné,
                le hub se connecte à la première télécommande qu'il trouve.
            timeout (Number, ms): Durée de recherche de la télécommande.
        """

    @overload
    def name(self, name: str) -> None: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Définit ou obtient le nom Bluetooth de la télécommande.

        Arguments:
            name (str): Nouveau nom Bluetooth de la télécommande. Si aucun nom n'est donné,
                cette méthode retourne le nom actuel.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Déconnecte la télécommande du hub.
        """


class TiltSensor:
    """Capteur d'inclinaison LEGO® Powered Up."""

    def __init__(self, port: Port):
        """TiltSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def tilt(self) -> MaybeAwaitableTuple[int, int]:
        """tilt() -> Tuple[int, int]: deg

        Mesure l'inclinaison par rapport au plan horizontal.

        Retourne :
            Tuple des angles de tangage et de roulis.
        """


class ColorDistanceSensor(_common.CommonColorSensor):
    """Capteur de couleur et de distance LEGO® Powered Up."""

    light = _common.ExternalColorLight()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Mesure la distance relative entre le capteur et un objet
        en utilisant la lumière infrarouge.

        Retourne :
            Distance allant de 0% (le plus proche) à 100% (le plus éloigné).
        """


class PFMotor:
    """Contrôler les moteurs Power Functions avec la fonctionnalité infrarouge du
    :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`."""

    def __init__(
        self,
        sensor: ColorDistanceSensor,
        channel: int,
        color: Color,
        positive_direction: Direction = Direction.CLOCKWISE,
    ):
        """PFMotor(sensor, channel, color, positive_direction=Direction.CLOCKWISE)

        Arguments:
            sensor (ColorDistanceSensor):
                Objet capteur.
            channel (int):
                Numéro de canal du récepteur : ``1``, ``2``, ``3`` ou ``4``.
            color (Color):
                Marqueur de couleur sur le récepteur :
                :class:`Color.BLUE <.parameters.Color>` ou
                :class:`Color.RED <.parameters.Color>`
            positive_direction (Direction): La direction dans laquelle le moteur doit
                tourner lorsque vous donnez une valeur de cycle de service positive.
        """

    def dc(self, duty: Number) -> MaybeAwaitable:
        """dc(duty)

        Fait tourner le moteur à un cycle de service donné (également appelé "puissance").

        Arguments:
            duty (Number, %): Le cycle de service (-100.0 à 100).
        """

    def stop(self) -> MaybeAwaitable:
        """stop()

        Arrête le moteur et le laisse tourner librement.

        Le moteur s'arrête progressivement en raison de la friction.
        """

    def brake(self) -> MaybeAwaitable:
        """brake()

        Freine passivement le moteur.

        Le moteur s'arrête en raison de la friction, plus la tension qui
        est générée pendant que le moteur est encore en mouvement.
        """


class ColorSensor(_common.AmbientColorSensor):
    """Capteur de couleur LEGO® SPIKE."""

    lights = _common.LightArray3()

    # HACK: jedi can't find inherited __init__ so docs have to be duplicated
    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """


class UltrasonicSensor:
    """Capteur de couleur LEGO® SPIKE."""

    lights = _common.LightArray4()

    def __init__(self, port: Port):
        """UltrasonicSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.

        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: mm

        Mesure la distance entre le capteur et un objet en utilisant
        des ondes sonores ultrasoniques.

        Retourne :
            Distance mesurée. Si aucune distance valide n'a été mesurée,
            il retourne 2000 mm.

        """

    def presence(self) -> MaybeAwaitableBool:
        """presence() -> bool

        Vérifie la présence d'autres capteurs ultrasoniques en détectant
        des sons ultrasoniques.

        Retourne :
            ``True`` si des sons ultrasoniques sont détectés, ``False`` sinon.
        """


class ForceSensor:
    """Capteur de force LEGO® SPIKE."""

    def __init__(self, port: Port):
        """ForceSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def force(self) -> MaybeAwaitableFloat:
        """force() -> float: N

        Mesure la force exercée sur le capteur.

        Retourne :
            Force mesurée (jusqu'à environ 10.00 N).
        """

    def distance(self) -> MaybeAwaitableFloat:
        """distance() -> float: mm

        Mesure de combien le bouton du capteur a bougé.

        Retourne :
            Mouvement jusqu'à environ 8.00 mm.
        """

    def pressed(self, force: Number = 3) -> MaybeAwaitableBool:
        """pressed(force=3) -> bool

        Vérifie si le bouton du capteur est pressé.

        Arguments:
            force (Number, N): Force minimale pour être considéré comme pressé.

        Retourne :
            ``True`` si le capteur est pressé, ``False`` sinon.
        """

    def touched(self) -> MaybeAwaitableBool:
        """touched() -> bool

        Vérifie si le capteur est touché.

        Cela est similaire à :meth:`pressed`, mais il détecte de légers mouvements du
        bouton même lorsque la force mesurée est encore considérée comme nulle.

        Retourne :
            ``True`` si le capteur est touché ou pressé, ``False``
            sinon.
        """


class ColorLightMatrix:
    """
    Matrice de lumière colorée 3x3 LEGO® SPIKE.
    """

    def __init__(self, port: Port):
        """ColorLightMatrix(port)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.

        """

    def on(self, color: Union[Color, Collection[Color]]) -> MaybeAwaitable:
        """on(colors)

        Allume les lumières.

        Arguments:
            colors (Color ou liste):
                Si une seule :class:`.Color` est donnée, alors les 9 lumières sont réglées
                à cette couleur. Si une liste de couleurs est donnée, alors chaque lumière est
                réglée à cette couleur.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Éteint toutes les lumières.
        """


class InfraredSensor:
    """Capteur infrarouge LEGO® Powered Up."""

    def __init__(self, port: Port):
        """InfraredSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Mesure la réflexion d'une surface en utilisant une lumière infrarouge.

        Retourne :
            Réflexion mesurée, allant de 0% (aucune réflexion) à
            100% (haute réflexion).
        """

    def distance(self) -> MaybeAwaitableInt:
        """distance() -> int: %

        Mesure la distance relative entre le capteur et un objet
        en utilisant la lumière infrarouge.

        Retourne :
            Distance allant de 0% (le plus proche) à 100% (le plus éloigné).
        """

    def count(self) -> MaybeAwaitableInt:
        """count() -> int

        Compte le nombre d'objets qui sont passés devant le capteur.

        Retourne :
            Nombre d'objets comptés.
        """


class Light:
    """Lumière LEGO® Powered Up."""

    def __init__(self, port: Port):
        """Light(port)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
        """

    def on(self, brightness: Number = 100) -> None:
        """on(brightness=100)

        Allume la lumière à la luminosité spécifiée.

        Arguments:
            brightness (Number, %):
                Luminosité de la lumière.
        """

    def off(self) -> None:
        """off()

        Éteint la lumière."""


# HACK: exclude from jedi
if TYPE_CHECKING:
    del Button
    del Color
    del Direction
    del MaybeAwaitable
    del MaybeAwaitableBool
    del MaybeAwaitableFloat
    del MaybeAwaitableInt
    del MaybeAwaitableTuple
    del Number
    del Port
