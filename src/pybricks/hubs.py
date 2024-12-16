# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Programmable Hubs."""

from typing import Sequence

from . import _common
from .ev3dev import _speaker
from .media.ev3dev import Image as _Image
from .parameters import Button as _Button, Axis


class EV3Brick:
    """Brique LEGO® MINDSTORMS® EV3."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.UP,
            _Button.DOWN,
        ]
    )
    screen = _Image("_screen_")
    speaker = _speaker.Speaker()
    battery = _common.Battery()
    light = _common.ColorLight()


class MoveHub:
    """LEGO® BOOST Move Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.SimpleAccelerometer()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = 0, observe_channels: Sequence[int] = []
    ):
        """MoveHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[])

        Arguments:
            top_side (Axis): L'axe qui passe par le *côté supérieur* du hub.
            front_side (Axis): L'axe qui passe par le *côté avant* du hub.
            broadcast_channel:
                Une valeur de 0 à 255 indiquant quel canal ``hub.ble.broadcast()`` utilisera.
                La valeur par défaut est le canal 0.
            observe_channels:
                Une liste de canaux à écouter lorsque ``hub.ble.observe()`` est appelé.
                Écouter plus de canaux nécessite plus de mémoire.
                La valeur par défaut est une liste vide (aucun canal).

        .. versionchanged:: 3.3
            Ajout des arguments *broadcast_channel* et *observe_channels*.
        """


class CityHub:
    """LEGO® City Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self, broadcast_channel: int = 0, observe_channels: Sequence[int] = []
    ):
        """CityHub(broadcast_channel=0, observe_channels=[])

        Arguments:
            broadcast_channel:
                Une valeur de 0 à 255 indiquant quel canal ``hub.ble.broadcast()`` utilisera.
                La valeur par défaut est le canal 0.
            observe_channels:
                Une liste de canaux à écouter lorsque ``hub.ble.observe()`` est appelé.
                Écouter plus de canaux nécessite plus de mémoire.
                La valeur par défaut est une liste vide (aucun canal).

        .. versionchanged:: 3.3
            Ajout des arguments *broadcast_channel* et *observe_channels*.
        """


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = 0,
        observe_channels: Sequence[int] = [],
    ):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[])

        Initialise le hub. Facultativement, spécifiez comment le hub est
        :ref:`placé dans votre conception <robotframe>` en indiquant dans quelle
        direction le côté supérieur (avec le bouton) et le côté avant
        (avec la lumière) pointent.

        Arguments:
            top_side (Axis): L'axe qui passe par le *côté supérieur* du hub.
            front_side (Axis): L'axe qui passe par le *côté avant* du hub.
            broadcast_channel:
                Une valeur de 0 à 255 indiquant quel canal ``hub.ble.broadcast()`` utilisera.
                La valeur par défaut est le canal 0.
            observe_channels:
                Une liste de canaux à écouter lorsque ``hub.ble.observe()`` est appelé.
                Écouter plus de canaux nécessite plus de mémoire.
                La valeur par défaut est une liste vide (aucun canal).

        .. versionchanged:: 3.3
            Ajout des arguments *broadcast_channel* et *observe_channels*.
        """


class EssentialHub:
    """LEGO® SPIKE Essential Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad([_Button.CENTER])
    charger = _common.Charger()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = 0,
        observe_channels: Sequence[int] = [],
    ):
        """EssentialHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[])

        Initialise le hub. Facultativement, spécifiez comment le hub est
        :ref:`placé dans votre conception <robotframe>` en indiquant dans quelle
        direction le côté supérieur (avec le bouton) et le côté avant (avec le port USB
        et les ports I/O A et B) pointent.

        Arguments:
            top_side (Axis): L'axe qui passe par le *côté supérieur* du hub.
            front_side (Axis): L'axe qui passe par le *côté avant* du hub.
            broadcast_channel:
                Une valeur de 0 à 255 indiquant quel canal ``hub.ble.broadcast()`` utilisera.
                La valeur par défaut est le canal 0.
            observe_channels:
                Une liste de canaux à écouter lorsque ``hub.ble.observe()`` est appelé.
                Écouter plus de canaux nécessite plus de mémoire.
                La valeur par défaut est une liste vide (aucun canal).

        .. versionchanged:: 3.3
            Ajout des arguments *broadcast_channel* et *observe_channels*.
        """
        pass


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        ]
    )
    charger = _common.Charger()
    light = _common.ColorLight()
    display = _common.LightMatrix(5, 5)
    speaker = _common.Speaker()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = 0,
        observe_channels: Sequence[int] = [],
    ):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[])

        Initialise le hub. Facultativement, spécifiez comment le hub est
        :ref:`placé dans votre conception <robotframe>` en indiquant dans quelle
        direction le côté supérieur (avec les boutons) et le côté avant (avec le port USB)
        pointent.

        Arguments:
            top_side (Axis): L'axe qui passe par le *côté supérieur* du hub.
            front_side (Axis): L'axe qui passe par le *côté avant* du hub.
            broadcast_channel:
                Une valeur de 0 à 255 indiquant quel canal ``hub.ble.broadcast()`` utilisera.
                La valeur par défaut est le canal 0.
            observe_channels:
                Une liste de canaux à écouter lorsque ``hub.ble.observe()`` est appelé.
                Écouter plus de canaux nécessite plus de mémoire.
                La valeur par défaut est une liste vide (aucun canal).

        .. versionchanged:: 3.3
            Ajout des arguments *broadcast_channel* et *observe_channels*.
        """


class InventorHub(PrimeHub):
    """LEGO® MINDSTORMS Inventor Hub."""


# HACK: hide from jedi
del Axis
