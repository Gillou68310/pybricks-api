# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Appareils d'entrée/sortie génériques."""

from __future__ import annotations

from typing import Dict, Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Port as _Port

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


class PUPDevice:
    """Moteur ou capteur Powered Up."""

    def __init__(self, port: _Port):
        """PUPDevice(port)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
        """

    def info(self) -> Dict[str, str]:
        """info() -> Dict

        Obtient des informations sur l'appareil.

        Returns:
            Dictionnaire avec des informations, telles que l'``id`` de l'appareil.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lit les valeurs d'un mode donné.

        Arguments:
            mode (int): Mode de l'appareil.

        Returns:
            Valeurs lues du capteur.
        """

    def write(self, mode: int, data: Tuple) -> MaybeAwaitable:
        """write(mode, data)

        Écrit des valeurs dans le capteur. Seuls certains capteurs et modes prennent en charge
        cela.

        Arguments:
            mode (int): Mode de l'appareil.
            data (tuple): Valeurs à écrire.
        """


class LUMPDevice:
    """Appareils utilisant le protocole de messagerie LEGO UART."""

    def __init__(self, port: _Port):
        """LUMPDevice(port)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lit les valeurs d'un mode donné.

        Arguments:
            mode (int): Mode de l'appareil.

        Returns:
            Valeurs lues du capteur.
        """


class DCMotor(_common.DCMotor):
    """Moteur DC pour LEGO® MINDSTORMS EV3."""


class Ev3devSensor:
    """Lire les valeurs d'un capteur compatible ev3dev."""

    sensor_index: int
    """Index de la classe ev3dev sysfs `lego-sensor`_."""

    port_index: int
    """Index de la classe ev3dev sysfs `lego-port`_."""

    def __init__(self, port: _Port):
        """Ev3devSensor(port)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
        """

    def read(self, mode: str) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lit les valeurs dans un mode donné.

        Arguments:
            mode (str): `Nom du mode`_.

        Returns:
            Valeurs lues du capteur.
        """


class AnalogSensor:
    """Capteur analogique générique ou personnalisé."""

    def __init__(self, port: _Port):
        """AnalogSensor(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Mesure la tension analogique.

        Returns:
            Tension analogique.
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        Mesure la résistance.

        Cette valeur n'a de sens que si l'appareil analogique est une charge passive
        telle qu'une résistance ou une thermistance.

        Returns:
            Résistance de l'appareil analogique.
        """

    def active(self) -> None:
        """active()

        Définit le capteur en mode actif. Cela met la broche 5 du port du capteur
        à `haut`.

        Cela est utilisé dans certains capteurs analogiques pour contrôler un interrupteur. Par exemple, si vous utilisez le capteur de lumière NXT
        comme capteur analogique personnalisé, cette méthode allumera la lumière.
        À partir de ce moment, ``voltage()`` renvoie la valeur brute de la lumière réfléchie.
        """

    def passive(self) -> None:
        """passive()

        Définit le capteur en mode passif. Cela met la broche 5 du port du capteur
        à `bas`.

        Cela est utilisé dans certains capteurs analogiques pour contrôler un interrupteur. Par exemple, si vous utilisez le capteur de lumière NXT
        comme capteur analogique personnalisé, cette méthode éteindra la lumière.
        À partir de ce moment, ``voltage()`` renvoie la valeur brute de la lumière ambiante.
        """


class I2CDevice:
    """Appareil I2C générique ou personnalisé."""

    def __init__(self, port: _Port, address: int):
        """I2CDevice(port, address)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
            address(int): Adresse I2C de l'appareil client. Voir
                :ref:`Adresses I2C <i2caddress>`.
        """

    def read(self, reg: Optional[int], length: Optional[int] = 1) -> bytes:
        """read(reg, length=1)

        Lit des octets, en commençant à un registre donné.

        Arguments:
            reg (int): Registre à partir duquel commencer
                la lecture : 0--255 ou 0x00--0xFF.
            length (int): Nombre d'octets à lire.

        Returns:
            Octets renvoyés par l'appareil.
        """

    def write(self, reg: Optional[int], data: Optional[bytes] = None) -> None:
        """write(reg, data=None)

        Écrit des octets, en commençant à un registre donné.

        Arguments:
            reg (int): Registre à partir duquel commencer
                l'écriture : 0--255 ou 0x00--0xFF.
            data (bytes): Octets à écrire.
        """


class UARTDevice:
    """Appareil UART générique."""

    def __init__(self, port: _Port, baudrate: int, timeout: Optional[int] = None):
        """UARTDevice(port, baudrate, timeout=None)

        Arguments:
            port (Port): Port auquel l'appareil est connecté.
            baudrate (int): Baudrate de l'appareil UART.
            timeout (Number, ms): Durée d'attente
                pendant ``read`` avant d'abandonner. Si vous choisissez ``None``,
                il attendra indéfiniment.
        """

    def read(self, length: int = 1) -> bytes:
        """read(length=1) -> bytes

        Lit un nombre donné d'octets du tampon.

        Votre programme attendra jusqu'à ce que le nombre d'octets demandé soit
        reçu. Si cela prend plus de temps que ``timeout``, l'exception ``ETIMEDOUT``
        est levée.

        Arguments:
            length (int): Nombre d'octets à lire.

        Returns:
            Octets renvoyés par l'appareil.
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        Lit tous les octets du tampon.

        Returns:
            Octets renvoyés par l'appareil.
        """

    def write(self, data: bytes) -> None:
        """write(data)

        Écrit des octets.

        Arguments:
            data (bytes): Octets à écrire.
        """

    def waiting(self) -> int:
        """waiting() -> int

        Obtient le nombre d'octets en attente de lecture.

        Returns:
            Nombre d'octets dans le tampon.
        """

    def clear(self) -> None:
        """clear()

        Vide le tampon."""


class LWP3Device:
    """
    Se connecte à un hub exécutant le firmware officiel LEGO en utilisant le
    `LEGO Wireless Protocol v3`_

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(self, hub_kind: int, name: str = None, timeout: int = 10000):
        """LWP3Device(hub_kind, name=None, timeout=10000)

        Arguments:
            hub_kind (int):
                L'`identifiant de type de hub`_ du hub auquel se connecter.
            name (str):
                Le nom du hub auquel se connecter ou ``None`` pour se connecter à n'importe quel
                hub.
            timeout (int):
                Le temps, en millisecondes, d'attente pour une connexion avant
                de lever une exception.


        .. _`identifiant de type de hub`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Définit ou obtient le nom Bluetooth de l'appareil.

        Arguments:
            name (str): Nouveau nom Bluetooth de l'appareil. Si aucun nom n'est donné,
                cette méthode renvoie le nom actuel.
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        Envoie un message au hub distant.

        Arguments:
            buf (bytes): Le message binaire brut à envoyer.
        """

    def read(self) -> bytes:
        """read() -> bytes

        Récupère le message le plus récent reçu du hub distant.

        Si un message n'a pas été reçu depuis la dernière lecture, la méthode
        bloquera jusqu'à ce qu'un message soit reçu.

        Returns:
            Le message binaire brut.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Déconnecte le LWP3Device distant du hub.
        """


class XboxController:
    """Utilisez la manette Microsoft® Xbox® comme capteur dans vos projets pour
    les contrôler à distance.

    Le hub recherchera la manette et s'y connectera. Il se déconnectera
    lorsque le programme se termine.

    Pour des conseils sur la connectivité et l'appairage, voir :ref:`ci-dessous <xbox-controller-pairing>`.
    """

    buttons = _common.Keypad([])

    def __init__(self):
        """"""

    def joystick_left(self) -> Tuple[int, int]:
        """joystick_left() -> Tuple

        Obtient la position du joystick gauche en pourcentages entre -100%
        et 100%. La position centrale est (0, 0).

        Returns:
            Tuple de position X (horizontale) et Y (verticale).
        """

    def joystick_right(self) -> Tuple[int, int]:
        """joystick_right() -> Tuple

        Obtient la position du joystick droit en pourcentages entre -100%
        et 100%. La position centrale est (0, 0).

        Returns:
            Tuple de position X (horizontale) et Y (verticale).
        """

    def triggers(self) -> Tuple[int, int]:
        """triggers() -> Tuple

        Obtient les positions des gâchettes gauche et droite en pourcentages entre 0%
        et 100%.

        Returns:
            Tuple des positions des gâchettes gauche et droite.
        """

    def dpad(self) -> int:
        """dpad() -> int

        Obtient la valeur du pavé directionnel. ``1`` est en haut, ``2`` est en haut à droite, ``3``
        est à droite, ``4`` est en bas à droite, ``5`` est en bas, ``6`` est en bas à gauche,
        ``7`` est à gauche, ``8`` est en haut à gauche, et ``0`` n'est pas pressé.

        Cela est essentiellement la même chose que de lire l'état des
        boutons ``Button.UP``, ``Button.RIGHT``, ``Button.DOWN``, et ``Button.LEFT``,
        mais cette méthode renvoie commodément un nombre indiquant
        une direction.

        Returns:
            Position du pavé directionnel, indiquant une direction.
        """

    def profile(self) -> int:
        """profile() -> int

        Obtient le profil actuel de la manette. Disponible uniquement sur la
        Xbox Elite Controller Series 2.

        Returns:
            Numéro de profil.
        """

    def rumble(
        self,
        power: Number | Tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        Fait vibrer les actionneurs intégrés, créant un retour de force.

        Si vous donnez une seule valeur ``power``, les actionneurs principaux gauche et droit
        vibreront tous deux avec cette puissance. Pour un contrôle plus précis, définissez
        ``power`` comme un tuple de quatre valeurs, qui contrôlent l'actionneur principal gauche,
        l'actionneur principal droit, l'actionneur de la gâchette gauche et l'actionneur de la gâchette droite,
        respectivement. Par exemple, ``power=(0, 0, 100, 0)``
        fait vibrer la gâchette gauche à pleine puissance.

        La vibration se fait en arrière-plan pendant que votre programme continue. Pour
        faire attendre votre programme, il suffit de le mettre en pause pendant une durée correspondante.
        Pour une seule vibration, cela équivaut à ``duration``. Pour plusieurs vibrations, cela
        équivaut à ``count * (duration + delay)``.

        Arguments:
            power (Number, % or tuple): Puissance de la vibration.
            duration (Number, ms): Durée de la vibration.
            count (int): Nombre de vibrations.
            delay (Number, ms): Délai avant chaque vibration. Seulement si ``count > 1``.
        """


# hide from jedi
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableTuple
    del Number
