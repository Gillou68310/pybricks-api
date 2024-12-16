# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""
Classes to exchange messages between EV3 bricks.
"""

from __future__ import annotations

from typing import abstractmethod, TypeVar, Optional, Callable, Generic

T = TypeVar("T")


class Connection:
    @abstractmethod
    def read_from_mailbox(self, name: str) -> bytes:
        ...

    @abstractmethod
    def send_to_mailbox(self, name: str, data: bytes) -> None:
        ...

    @abstractmethod
    def wait_for_mailbox_update(self, name: str) -> None:
        ...


class Mailbox(Generic[T]):
    def __init__(
        self,
        name: str,
        connection: Connection,
        encode: Optional[Callable[[T], bytes]] = None,
        decode: Optional[Callable[[bytes], T]] = None,
    ):
        """Mailbox(name, connection, encode=None, decode=None)

        Objet représentant une boîte aux lettres contenant des données.

        Vous pouvez lire les données livrées par d'autres briques EV3, ou envoyer des données
        à d'autres briques qui ont la même boîte aux lettres.

        Par défaut, la boîte aux lettres lit et envoie uniquement des octets. Pour envoyer d'autres
        données, vous pouvez fournir une fonction ``encode`` qui encode votre objet Python
        en octets, et une fonction ``decode`` pour convertir les octets en
        un objet Python.

        Arguments:
            name (str):
                Le nom de cette boîte aux lettres.
            connection:
                Un objet de connexion tel que :class:`BluetoothMailboxClient`.
            encode (callable):
                Fonction qui encode un objet Python en octets.
            decode (callable):
                Fonction qui crée un nouvel objet Python à partir des octets.
        """

    def read(self) -> T:
        """read()

        Obtient la valeur actuelle de la boîte aux lettres.

        Returns:
            La valeur actuelle ou ``None`` si la boîte aux lettres est vide.
        """
        return ""

    def send(self, value: T, brick: Optional[str] = None) -> None:
        """send(value, brick=None)

        Envoie une valeur à cette boîte aux lettres sur les appareils connectés.

        Arguments:
            value:
                La valeur qui sera livrée à la boîte aux lettres.
            brick (str):
                Le nom ou l'adresse Bluetooth de la brique ou ``None`` pour
                diffuser à tous les appareils connectés.

        Raises:
            OSError:
                Il y a un problème avec la connexion.
        """

    def wait(self) -> None:
        """wait()

        Attend que la boîte aux lettres soit mise à jour par un appareil distant."""

    def wait_new(self) -> T:
        """wait_new()

        Attend qu'une nouvelle valeur soit livrée à la boîte aux lettres qui n'est pas
        égale à la valeur actuelle dans la boîte aux lettres.

        Returns:
            La nouvelle valeur.
        """
        return object()


class LogicMailbox(Mailbox[bool]):
    def __init__(self, name: str, connection: Connection):
        """LogicMailbox(name, connection)

        Objet représentant une boîte aux lettres contenant des données booléennes.

        Cela fonctionne comme une :class:`Mailbox` régulière, mais les valeurs
        doivent être ``True`` ou ``False``.

        Cela est compatible avec le type de boîte aux lettres "logique" dans EV3-G.

        Arguments:
            name (str):
                Le nom de cette boîte aux lettres.
            connection:
                Un objet de connexion tel que :class:`BluetoothMailboxClient`.
        """


class NumericMailbox(Mailbox[float]):
    def __init__(self, name: str, connection: Connection):
        """NumericMailbox(name, connection)

        Objet représentant une boîte aux lettres contenant des données numériques.

        Cela fonctionne comme une :class:`Mailbox` régulière, mais les valeurs doivent être un
        nombre, tel que ``15`` ou ``12.345``.

        Cela est compatible avec le type de boîte aux lettres "numérique" dans EV3-G.

        Arguments:
            name (str):
                Le nom de cette boîte aux lettres.
            connection:
                Un objet de connexion tel que :class:`BluetoothMailboxClient`.
        """


class TextMailbox(Mailbox[str]):
    def __init__(self, name: str, connection: Connection):
        """TextMailbox(name, connection)

        Objet représentant une boîte aux lettres contenant des données textuelles.

        Cela fonctionne comme une :class:`Mailbox` régulière, mais les données doivent être une
        chaîne de caractères, telle que ``'hello!'``.

        Cela est compatible avec le type de boîte aux lettres "texte" dans EV3-G.

        Arguments:
            name (str):
                Le nom de cette boîte aux lettres.
            connection:
                Un objet de connexion tel que :class:`BluetoothMailboxClient`.
        """


class BluetoothMailboxServer:
    """Objet représentant une connexion Bluetooth à partir d'un ou plusieurs EV3 distants.

    Les EV3 distants peuvent exécuter MicroPython ou le firmware standard EV3.

    Un "serveur" attend qu'un "client" se connecte à lui.
    """

    def __enter__(self) -> BluetoothMailboxServer:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.server_close()

    def wait_for_connection(self, count: int = 1) -> None:
        """wait_for_connection(count=1)

        Attend qu'un :class:`BluetoothMailboxClient` sur un appareil distant se
        connecte.

        Arguments:
            count (int):
                Le nombre de connexions distantes à attendre.

        Raises:
            OSError:
                Il y a eu un problème pour établir la connexion.
        """

    def server_close(self) -> None:
        """server_close()

        Ferme toutes les connexions."""


class BluetoothMailboxClient:
    """Objet représentant une connexion Bluetooth à un ou plusieurs EV3 distants.

    Les EV3 distants peuvent exécuter MicroPython ou le firmware standard EV3.

    Un "client" initie une connexion à un "serveur" en attente.
    """

    def __enter__(self) -> BluetoothMailboxClient:
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.close()

    def connect(self, brick: str) -> None:
        """connect(brick)

        Se connecte à un :class:`BluetoothMailboxServer` sur un autre appareil.

        L'appareil distant doit être appairé et en attente d'une connexion. Voir
        :meth:`BluetoothMailboxServer.wait_for_connection`.

        Arguments:
            brick (str):
                Le nom ou l'adresse Bluetooth de l'EV3 distant à connecter.

        Raises:
            OSError:
                Il y a eu un problème pour établir la connexion.
        """

    def close(self) -> None:
        """close()

        Ferme toutes les connexions."""
