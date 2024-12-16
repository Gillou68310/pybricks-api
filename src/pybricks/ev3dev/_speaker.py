# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2021 The Pybricks Authors

from typing import Iterable, Union, Optional

from ..media.ev3dev import SoundFile


class Speaker:
    """Joue des bips et des sons à l'aide d'un haut-parleur."""

    def beep(self, frequency: int = 500, duration: int = 100) -> None:
        """beep(frequency=500, duration=100)

        Joue un bip/ton.

        Arguments:
            frequency (Nombre, Hz):
                Fréquence du bip. Les fréquences inférieures à 100 Hz sont traitées comme
                100 Hz.
            duration (Nombre, ms):
                Durée du bip. Si la durée est inférieure à 0, alors la
                méthode retourne immédiatement et la fréquence continue de
                jouer indéfiniment.
        """

    def play_notes(self, notes: Iterable[str], tempo: int = 120) -> None:
        """play_notes(notes, tempo=120)

        Joue une séquence de notes musicales. Par exemple :
        ``['C4/4', 'C4/4', 'G4/4', 'G4/4']``.

        Chaque note est une chaîne de caractères avec le format suivant :

            - Le premier caractère est le nom de la note, ``A`` à ``G``
              ou ``R`` pour un silence.
            - Les noms de notes peuvent également inclure un accidentel ``#`` (dièse) ou
              ``b`` (bémol). ``B#``/``Cb`` et ``E#``/``Fb`` ne sont pas
              autorisés.
            - Le nom de la note est suivi du numéro de l'octave ``2``
              à ``8``. Par exemple ``C4`` est le do central. L'octave change
              au numéro suivant à la note C, par exemple, ``B3`` est la
              note en dessous du do central (``C4``).
            - L'octave est suivie de ``/`` et d'un nombre qui indique
              la durée de la note. Par exemple ``/4`` est une noire,
              ``/8`` est une croche, etc.
            - Cela peut être suivi optionnellement d'un ``.`` pour faire une note pointée.
              Les notes pointées durent 1,5 fois plus longtemps que les notes sans point.
            - La note peut se terminer optionnellement par un ``_`` qui est une liaison ou un
              legato. Cela fait qu'il n'y a pas de pause entre cette note et
              la note suivante.

        Arguments:
            notes (iter):
                Une séquence de notes à jouer.
            tempo (int):
                Battements par minute. Une noire est un battement.
        """

    def play_file(self, file_name: Union[SoundFile, str]) -> None:
        """play_file(file_name)

        Joue un fichier audio.

        Arguments:
            file (str):
                Chemin vers le fichier audio, y compris l'extension du fichier.
        """

    def say(self, text: str) -> None:
        """say(text)

        Dit une chaîne de texte donnée.

        Vous pouvez configurer la langue et la voix du texte en utilisant
        :meth:`.set_speech_options`.

        Arguments:
            text (str): Que dire.
        """

    def set_speech_options(
        self,
        language: Optional[str] = None,
        voice: Optional[str] = None,
        speed: Optional[int] = None,
        pitch: Optional[int] = None,
    ):
        """set_speech_options(language, voice, speed, pitch)

        Configure les paramètres de la parole utilisés par la méthode :meth:`.say`.

        Toute option définie sur ``None`` ne sera pas modifiée. Si une option
        est définie sur une valeur invalide, :meth:`.say` utilisera la valeur par défaut
        à la place.

        Arguments:
            language (str):
                Langue du texte. Par exemple, vous pouvez choisir ``'en'``
                (Anglais) ou ``'de'`` (Allemand). [#espeak_lang]_
            voice (str):
                La voix à utiliser. Par exemple, vous pouvez choisir ``'f1'`` (voix féminine
                variante 1) ou ``'m3'`` (voix masculine variante 3).
                [#espeak_lang]_
            speed (int):
                Nombre de mots par minute.
            pitch (int):
                Hauteur (0 à 99). Les nombres plus élevés rendent la voix plus aiguë
                et les nombres plus bas rendent la voix plus grave.
        """

    def set_volume(self, volume: int, which: str = "_all_") -> None:
        """set_volume(volume, which="_all_")

        Définit le volume du haut-parleur.

        Arguments:
            volume (Nombre, %):
                Volume du haut-parleur.
            which (str):
                Quel volume définir. ``'Beep'`` définit le volume pour
                `beep` et `play_notes`. ``'PCM'`` définit le
                volume pour :meth:`.play_file` et :meth:`.say`. ``'_all_'``
                définit les deux en même temps.
        """
