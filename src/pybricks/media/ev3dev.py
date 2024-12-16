# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2020 The Pybricks Authors

"""Images et sons pour Pybricks sur ev3dev."""

from __future__ import annotations

from typing import Union, Literal, overload, Optional, Any

from ..parameters import Color


class Image:
    """Objet représentant une image graphique. Cela peut être une copie en mémoire
    d'une image ou l'image affichée sur un écran."""

    # Documentation note: This class is also treated as the `screen` object
    # on EV3 so we use |this image| when it would make sense to say "the screen"
    # in that context and it is automatically replaced when the documentation
    # is generated.

    @overload
    def __init__(self, /, source: Union[Image, ImageFile, str]):
        ...

    @overload
    def __init__(
        self, /, source: Image, sub: Literal[False], x1: int, y1: int, x2: int, y2: int
    ):
        ...

    def __init__(self, *args):
        """Image(source, sub=False)


        Arguments:
            source (str ou Image):
                La source de l'image.

                Si ``source`` est une chaîne de caractères, l'image sera chargée à partir
                du chemin de fichier donné par la chaîne. Seuls les fichiers ``.png`` sont
                pris en charge. Dans un cas particulier, si la chaîne est ``_screen_``,
                l'image sera configurée pour dessiner directement sur l'écran.

                Si un :class:`Image` est donné, le nouvel objet contiendra une
                copie de l'objet image ``source``.

            sub (bool):
                Si ``sub`` est ``True``, l'objet image agira comme une
                sous-image de l'image ``source`` (cela ne fonctionne que si le type
                de ``source`` est :class:`Image` et non lorsqu'il s'agit d'une ``str``).

                Des arguments supplémentaires ``x1``, ``y1``, ``x2``, ``y2`` sont
                nécessaires lorsque ``sub=True``. Ceux-ci spécifient les coordonnées
                en haut à gauche et en bas à droite dans l'image ``source`` qui seront
                utilisées comme limites pour la sous-image.
        """

    @property
    def width(self) -> int:
        """Obtient la largeur de |cette image| en pixels."""
        return 0

    @property
    def height(self) -> int:
        """Obtient la hauteur de |cette image| en pixels."""
        return 0

    def clear(self) -> None:
        """clear()

        Efface |cette image|. Tous les pixels de |cette image| seront définis sur
        :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.
        """

    def draw_pixel(self, x: int, y: int, color: Color = Color.BLACK) -> None:
        """draw_pixel(x, y, color=Color.BLACK)

        Dessine un seul pixel sur |cette image|.

        Arguments:
            x (int): La coordonnée x du pixel.
            y (int): La coordonnée y du pixel.
            color (Color): La couleur du pixel.
        """

    def draw_line(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        width: int = 1,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_line(x1, y1, x2, y2, width=1, color=Color.BLACK)

        Dessine une ligne sur |cette image|.

        Arguments:
            x1 (int): La coordonnée x du point de départ de la ligne.
            y1 (int): La coordonnée y du point de départ de la ligne.
            x2 (int): La coordonnée x du point de fin de la ligne.
            y2 (int): La coordonnée y du point de fin de la ligne.
            width (int): La largeur de la ligne en pixels.
            color (Color): La couleur de la ligne.
        """

    def draw_box(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        r: int = 0,
        fill: bool = False,
        color: Color = Color.BLACK,
    ) -> None:
        """draw_box(x1, y1, x2, y2, r=0, fill=False, color=Color.BLACK)

        Dessine une boîte sur |cette image|.

        Arguments:
            x1 (int): La coordonnée x du côté gauche de la boîte.
            y1 (int): La coordonnée y du haut de la boîte.
            x2 (int): La coordonnée x du côté droit de la boîte.
            y2 (int): La coordonnée y du bas de la boîte.
            r (int): Le rayon des coins de la boîte.
            fill (bool): Si ``True``, la boîte sera remplie avec ``color``,
                sinon seul le contour de la boîte sera dessiné.
            color (Color): La couleur de la boîte.
        """

    def draw_circle(
        self, x: int, y: int, r: int, fill: bool = False, color: Color = Color.BLACK
    ) -> None:
        """draw_circle(x, y, r, fill=False, color=Color.BLACK)

        Dessine un cercle sur |cette image|.

        Arguments:
            x (int): La coordonnée x du centre du cercle.
            y (int): La coordonnée y du centre du cercle.
            r (int): Le rayon du cercle.
            fill (bool): Si ``True``, le cercle sera rempli avec
                ``color``, sinon seule la circonférence sera dessinée.
            color (Color): La couleur du cercle.
        """

    def draw_image(
        self,
        x: int,
        y: int,
        source: Union[Image, ImageFile, str],
        transparent: Optional[Color] = None,
    ) -> None:
        """draw_image(x, y, source, transparent=None)

        Dessine l'image ``source`` sur |cette image|.

        Arguments:
            x (int):
                La valeur de l'axe x où le côté gauche de l'image commencera.
            y (int):
                La valeur de l'axe y où le haut de l'image commencera.
            source (Image ou str):
                La source :class:`Image <pybricks.media.ev3dev.Image>`. Si
                l'argument est une chaîne de caractères, l'image ``source`` est chargée
                à partir du fichier.
            transparent (Color):
                La couleur de ``image`` à traiter comme transparente ou ``None`` pour
                aucune transparence.
        """

    def load_image(self, source: Union[Image, ImageFile, str]) -> None:
        """load_image(source)

        Efface cette image, puis dessine l'image ``source`` centrée dans
        |cette image|.

        Arguments:
            source (Image ou str):
                La source :class:`Image <pybricks.media.ev3dev.Image>`. Si
                l'argument est une chaîne de caractères, l'image ``source`` est chargée
                à partir du fichier.
        """

    def draw_text(
        self,
        x: int,
        y: int,
        text: str,
        text_color: Color = Color.BLACK,
        background_color: Optional[Color] = None,
    ) -> None:
        """draw_text(x, y, text, text_color=Color.BLACK, background_color=None)

        Dessine du texte sur |cette image|.

        La police la plus récente définie à l'aide de :meth:`.set_font` sera utilisée ou
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` si aucune police
        n'a encore été définie.

        Arguments:
            x (int):
                La valeur de l'axe x où le côté gauche du texte commencera.
            y (int):
                La valeur de l'axe y où le haut du texte commencera.
            text (str):
                Le texte à dessiner.
            text_color (Color):
                La couleur utilisée pour dessiner le texte.
            background_color (Color):
                La couleur utilisée pour remplir le rectangle derrière le texte ou
                ``None`` pour un fond transparent.
        """

    def print(self, *args: Any, sep: str = " ", end: str = "\n") -> None:
        """print(*args, sep=" ", end="\\n")

        Imprime une ligne de texte sur |cette image|.

        Cette méthode fonctionne comme la fonction intégrée ``print()``, mais elle écrit
        sur |cette image| à la place.

        Vous pouvez définir la police en utilisant :meth:`.set_font`. Si aucune police n'a été définie,
        :data:`Font.DEFAULT <pybricks.media.ev3dev.Font.DEFAULT>` sera
        utilisée. Le texte est toujours imprimé en utilisant du texte noir avec un fond blanc.

        Contrairement à la fonction intégrée ``print()``, le texte ne se renvoie pas à la ligne s'il est trop
        large pour tenir sur |cette image|. Il est simplement coupé. Mais si le texte
        dépasse le bas de |cette image|, toute l'image est
        défilée vers le haut et le texte est imprimé dans la nouvelle zone vide en bas de |cette image|.

        Arguments:
            args (Any): Zéro ou plusieurs objets à imprimer.
            sep (str): Séparateur qui sera placé entre chaque objet imprimé.
            end (str): Fin de ligne qui sera imprimée après le dernier objet.
        """

    def set_font(self, font: Font) -> None:
        """set_font(font)

        Définit la police utilisée pour écrire sur |cette image|.

        La police est utilisée pour :meth:`.draw_text` et :meth:`.print`.

        Arguments:
            font (Font):
                La police à utiliser.
        """

    @staticmethod
    def empty(width: int = 178, height: int = 128) -> Image:
        """empty(width=178, height=128) -> Image

        Crée un nouvel objet :class:`Image` vide.

        Arguments:
            width (int):
                La largeur de l'image en pixels.
            height (int):
                La hauteur de l'image en pixels.

        Returns:
            Une nouvelle image avec tous les pixels définis
            sur :attr:`Color.WHITE <pybricks.parameters.Color.WHITE>`.

        Raises:
            TypeError:
                Si ``width`` ou ``height`` n'est pas un nombre.
            ValueError:
                Si ``width`` ou ``height`` est inférieur à 1.
            RuntimeError:
                S'il y a eu un problème lors de l'allocation d'une nouvelle image.
        """

    def save(self, filename: str) -> None:
        """save(filename)

        Enregistre |cette image| en tant que fichier ``.png``.

        Arguments:
            filename (str):
                Le chemin vers le fichier à enregistrer.

        Raises:
            TypeError:
                ``filename`` n'est pas une chaîne de caractères.
            OSError:
                Il y a eu un problème lors de l'enregistrement du fichier.
        """


class Font:
    """Objet représentant une police pour écrire du texte."""

    DEFAULT: Font = None  # assigned later since we can't use Font() here
    """La police par défaut."""

    def __init__(
        self,
        family: Optional[str] = None,
        size: int = 12,
        bold: bool = False,
        monospace: bool = False,
        lang: Optional[str] = None,
        script: Optional[str] = None,
    ):
        """Font(family=None, size=12, bold=False, monospace=False, lang=None, script=None)

        L'objet police sera une police qui est la "meilleure" correspondance en fonction des
        paramètres donnés et des polices disponibles installées.

        Arguments:
            family (str):
                La famille de polices préférée ou ``None`` pour utiliser la valeur par défaut.
            size (int):
                La taille de police préférée. La plupart des polices ont des tailles comprises entre 6 et 24.
                Il s'agit de la taille en "points" et non de la même chose que :attr:`height`.
            bold (bool):
                Lorsque ``True``, préférer les polices en gras.
            monospace (bool):
                Lorsque ``True``, préférer les polices à espacement fixe. Cela est utile pour
                aligner plusieurs lignes de texte.
            lang (str):
                Un code de langue, tel que ``'en'`` ou ``'zh-cn'`` ou ``None`` pour
                utiliser la langue par défaut. [#font_lang]_
            script (str):
                Un identifiant de script unicode tel que ``'Runr'`` ou ``None``.
        """

    @property
    def family(self) -> str:
        """Obtient le nom de la famille de la police."""
        return "Lucida"

    @property
    def style(self) -> str:
        """style -> str

        Obtient une chaîne décrivant le style de la police.

        Peut être "Regular" ou "Bold".
        """
        return "Regular"

    @property
    def width(self) -> int:
        """Obtient la largeur du caractère le plus large de la police."""
        return 0

    @property
    def height(self) -> int:
        """Obtient la hauteur de la police."""
        return 0

    def text_width(self, text: str) -> int:
        """text_width(text)

        Obtient la largeur du texte lorsque le texte est dessiné en utilisant cette police.

        Arguments:
            text (str):
                Le texte.

        Returns:
            int:
                La largeur en pixels.
        """
        return 0

    def text_height(self, text: str) -> int:
        """text_height(text)

        Obtient la hauteur du texte lorsque le texte est dessiné en utilisant cette police.

        Arguments:
            text (str):
                Le texte.

        Returns:
            int:
                La hauteur en pixels.
        """
        return 0


Font.DEFAULT = Font("Lucida", 12)


class SoundFile:
    """Chemins vers les sons standard EV3."""

    _BASE_PATH: str = "/usr/share/sounds/ev3dev/"
    SHOUTING: str = _BASE_PATH + "expressions/shouting.wav"
    CHEERING: str = _BASE_PATH + "expressions/cheering.wav"
    CRYING: str = _BASE_PATH + "expressions/crying.wav"
    OUCH: str = _BASE_PATH + "expressions/ouch.wav"
    LAUGHING_2: str = _BASE_PATH + "expressions/laughing_2.wav"
    SNEEZING: str = _BASE_PATH + "expressions/sneezing.wav"
    SMACK: str = _BASE_PATH + "expressions/smack.wav"
    BOING: str = _BASE_PATH + "expressions/boing.wav"
    BOO: str = _BASE_PATH + "expressions/boo.wav"
    UH_OH: str = _BASE_PATH + "expressions/uh-oh.wav"
    SNORING: str = _BASE_PATH + "expressions/snoring.wav"
    KUNG_FU: str = _BASE_PATH + "expressions/kung_fu.wav"
    FANFARE: str = _BASE_PATH + "expressions/fanfare.wav"
    CRUNCHING: str = _BASE_PATH + "expressions/crunching.wav"
    MAGIC_WAND: str = _BASE_PATH + "expressions/magic_wand.wav"
    LAUGHING_1: str = _BASE_PATH + "expressions/laughing_1.wav"
    LEFT: str = _BASE_PATH + "information/left.wav"
    BACKWARDS: str = _BASE_PATH + "information/backwards.wav"
    RIGHT: str = _BASE_PATH + "information/right.wav"
    OBJECT: str = _BASE_PATH + "information/object.wav"
    COLOR: str = _BASE_PATH + "information/color.wav"
    FLASHING: str = _BASE_PATH + "information/flashing.wav"
    ERROR: str = _BASE_PATH + "information/error.wav"
    ERROR_ALARM: str = _BASE_PATH + "information/error_alarm.wav"
    DOWN: str = _BASE_PATH + "information/down.wav"
    FORWARD: str = _BASE_PATH + "information/forward.wav"
    ACTIVATE: str = _BASE_PATH + "information/activate.wav"
    SEARCHING: str = _BASE_PATH + "information/searching.wav"
    TOUCH: str = _BASE_PATH + "information/touch.wav"
    UP: str = _BASE_PATH + "information/up.wav"
    ANALYZE: str = _BASE_PATH + "information/analyze.wav"
    STOP: str = _BASE_PATH + "information/stop.wav"
    DETECTED: str = _BASE_PATH + "information/detected.wav"
    TURN: str = _BASE_PATH + "information/turn.wav"
    START: str = _BASE_PATH + "information/start.wav"
    MORNING: str = _BASE_PATH + "communication/morning.wav"
    EV3: str = _BASE_PATH + "communication/ev3.wav"
    GO: str = _BASE_PATH + "communication/go.wav"
    GOOD_JOB: str = _BASE_PATH + "communication/good_job.wav"
    OKEY_DOKEY: str = _BASE_PATH + "communication/okey-dokey.wav"
    GOOD: str = _BASE_PATH + "communication/good.wav"
    NO: str = _BASE_PATH + "communication/no.wav"
    THANK_YOU: str = _BASE_PATH + "communication/thank_you.wav"
    YES: str = _BASE_PATH + "communication/yes.wav"
    GAME_OVER: str = _BASE_PATH + "communication/game_over.wav"
    OKAY: str = _BASE_PATH + "communication/okay.wav"
    SORRY: str = _BASE_PATH + "communication/sorry.wav"
    BRAVO: str = _BASE_PATH + "communication/bravo.wav"
    GOODBYE: str = _BASE_PATH + "communication/goodbye.wav"
    HI: str = _BASE_PATH + "communication/hi.wav"
    HELLO: str = _BASE_PATH + "communication/hello.wav"
    MINDSTORMS: str = _BASE_PATH + "communication/mindstorms.wav"
    LEGO: str = _BASE_PATH + "communication/lego.wav"
    FANTASTIC: str = _BASE_PATH + "communication/fantastic.wav"
    SPEED_IDLE: str = _BASE_PATH + "movements/speed_idle.wav"
    SPEED_DOWN: str = _BASE_PATH + "movements/speed_down.wav"
    SPEED_UP: str = _BASE_PATH + "movements/speed_up.wav"
    BROWN: str = _BASE_PATH + "colors/brown.wav"
    GREEN: str = _BASE_PATH + "colors/green.wav"
    BLACK: str = _BASE_PATH + "colors/black.wav"
    WHITE: str = _BASE_PATH + "colors/white.wav"
    RED: str = _BASE_PATH + "colors/red.wav"
    BLUE: str = _BASE_PATH + "colors/blue.wav"
    YELLOW: str = _BASE_PATH + "colors/yellow.wav"
    TICK_TACK: str = _BASE_PATH + "mechanical/tick_tack.wav"
    HORN_1: str = _BASE_PATH + "mechanical/horn_1.wav"
    BACKING_ALERT: str = _BASE_PATH + "mechanical/backing_alert.wav"
    MOTOR_IDLE: str = _BASE_PATH + "mechanical/motor_idle.wav"
    AIR_RELEASE: str = _BASE_PATH + "mechanical/air_release.wav"
    AIRBRAKE: str = _BASE_PATH + "mechanical/airbrake.wav"
    RATCHET: str = _BASE_PATH + "mechanical/ratchet.wav"
    MOTOR_STOP: str = _BASE_PATH + "mechanical/motor_stop.wav"
    HORN_2: str = _BASE_PATH + "mechanical/horn_2.wav"
    LASER: str = _BASE_PATH + "mechanical/laser.wav"
    SONAR: str = _BASE_PATH + "mechanical/sonar.wav"
    MOTOR_START: str = _BASE_PATH + "mechanical/motor_start.wav"
    INSECT_BUZZ_2: str = _BASE_PATH + "animals/insect_buzz_2.wav"
    ELEPHANT_CALL: str = _BASE_PATH + "animals/elephant_call.wav"
    SNAKE_HISS: str = _BASE_PATH + "animals/snake_hiss.wav"
    DOG_BARK_2: str = _BASE_PATH + "animals/dog_bark_2.wav"
    DOG_WHINE: str = _BASE_PATH + "animals/dog_whine.wav"
    INSECT_BUZZ_1: str = _BASE_PATH + "animals/insect_buzz_1.wav"
    DOG_SNIFF: str = _BASE_PATH + "animals/dog_sniff.wav"
    T_REX_ROAR: str = _BASE_PATH + "animals/t-rex_roar.wav"
    INSECT_CHIRP: str = _BASE_PATH + "animals/insect_chirp.wav"
    DOG_GROWL: str = _BASE_PATH + "animals/dog_growl.wav"
    SNAKE_RATTLE: str = _BASE_PATH + "animals/snake_rattle.wav"
    DOG_BARK_1: str = _BASE_PATH + "animals/dog_bark_1.wav"
    CAT_PURR: str = _BASE_PATH + "animals/cat_purr.wav"
    EIGHT: str = _BASE_PATH + "numbers/eight.wav"
    SEVEN: str = _BASE_PATH + "numbers/seven.wav"
    SIX: str = _BASE_PATH + "numbers/six.wav"
    FOUR: str = _BASE_PATH + "numbers/four.wav"
    TEN: str = _BASE_PATH + "numbers/ten.wav"
    ONE: str = _BASE_PATH + "numbers/one.wav"
    TWO: str = _BASE_PATH + "numbers/two.wav"
    THREE: str = _BASE_PATH + "numbers/three.wav"
    ZERO: str = _BASE_PATH + "numbers/zero.wav"
    FIVE: str = _BASE_PATH + "numbers/five.wav"
    NINE: str = _BASE_PATH + "numbers/nine.wav"
    READY: str = _BASE_PATH + "system/ready.wav"
    CONFIRM: str = _BASE_PATH + "system/confirm.wav"
    GENERAL_ALERT: str = _BASE_PATH + "system/general_alert.wav"
    CLICK: str = _BASE_PATH + "system/click.wav"
    OVERPOWER: str = _BASE_PATH + "system/overpower.wav"


class ImageFile:
    """Chemins vers les images standard EV3."""

    _BASE_PATH: str = "/usr/share/images/ev3dev/mono/"
    RIGHT: str = _BASE_PATH + "information/right.png"
    FORWARD: str = _BASE_PATH + "information/forward.png"
    ACCEPT: str = _BASE_PATH + "information/accept.png"
    QUESTION_MARK: str = _BASE_PATH + "information/question_mark.png"
    STOP_1: str = _BASE_PATH + "information/stop_1.png"
    LEFT: str = _BASE_PATH + "information/left.png"
    DECLINE: str = _BASE_PATH + "information/decline.png"
    THUMBS_DOWN: str = _BASE_PATH + "information/thumbs_down.png"
    BACKWARD: str = _BASE_PATH + "information/backward.png"
    NO_GO: str = _BASE_PATH + "information/no_go.png"
    WARNING: str = _BASE_PATH + "information/warning.png"
    STOP_2: str = _BASE_PATH + "information/stop_2.png"
    THUMBS_UP: str = _BASE_PATH + "information/thumbs_up.png"
    EV3: str = _BASE_PATH + "lego/ev3.png"
    EV3_ICON: str = _BASE_PATH + "lego/ev3_icon.png"
    TARGET: str = _BASE_PATH + "objects/target.png"
    BOTTOM_RIGHT: str = _BASE_PATH + "eyes/bottom_right.png"
    BOTTOM_LEFT: str = _BASE_PATH + "eyes/bottom_left.png"
    EVIL: str = _BASE_PATH + "eyes/evil.png"
    CRAZY_2: str = _BASE_PATH + "eyes/crazy_2.png"
    KNOCKED_OUT: str = _BASE_PATH + "eyes/knocked_out.png"
    PINCHED_RIGHT: str = _BASE_PATH + "eyes/pinched_right.png"
    WINKING: str = _BASE_PATH + "eyes/winking.png"
    DIZZY: str = _BASE_PATH + "eyes/dizzy.png"
    DOWN: str = _BASE_PATH + "eyes/down.png"
    TIRED_MIDDLE: str = _BASE_PATH + "eyes/tired_middle.png"
    MIDDLE_RIGHT: str = _BASE_PATH + "eyes/middle_right.png"
    SLEEPING: str = _BASE_PATH + "eyes/sleeping.png"
    MIDDLE_LEFT: str = _BASE_PATH + "eyes/middle_left.png"
    TIRED_RIGHT: str = _BASE_PATH + "eyes/tired_right.png"
    PINCHED_LEFT: str = _BASE_PATH + "eyes/pinched_left.png"
    PINCHED_MIDDLE: str = _BASE_PATH + "eyes/pinched_middle.png"
    CRAZY_1: str = _BASE_PATH + "eyes/crazy_1.png"
    NEUTRAL: str = _BASE_PATH + "eyes/neutral.png"
    AWAKE: str = _BASE_PATH + "eyes/awake.png"
    UP: str = _BASE_PATH + "eyes/up.png"
    TIRED_LEFT: str = _BASE_PATH + "eyes/tired_left.png"
    ANGRY: str = _BASE_PATH + "eyes/angry.png"
