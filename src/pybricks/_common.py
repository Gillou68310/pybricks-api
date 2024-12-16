# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Module générique multiplateforme pour des appareils typiques comme les lumières, les écrans,
les haut-parleurs et les batteries."""

from __future__ import annotations

from typing import (
    Union,
    Iterable,
    overload,
    Optional,
    Tuple,
    Collection,
    Set,
    TYPE_CHECKING,
)

from .tools import Matrix
from .parameters import Axis, Direction, Stop, Button, Port, Color, Side

if TYPE_CHECKING:
    from typing import Any, Awaitable, TypeVar

    from .parameters import Number

    _T_co = TypeVar("_T_co", covariant=True)

    class MaybeAwaitable(None, Awaitable[None]): ...

    # HACK: Cannot subclass bool, so using Any instead.
    class MaybeAwaitableBool(Any, Awaitable[bool]): ...

    class MaybeAwaitableFloat(float, Awaitable[float]): ...

    class MaybeAwaitableInt(int, Awaitable[int]): ...

    class MaybeAwaitableTuple(Tuple[_T_co], Awaitable[Tuple[_T_co]]): ...

    class MaybeAwaitableColor(Color, Awaitable[Color]): ...


class System:
    """Actions de contrôle du système pour un hub."""

    def set_stop_button(
        self, button: Optional[Union[Button, Iterable[Button]]]
    ) -> None:
        """
        set_stop_button(button)

        Définit le bouton ou la combinaison de boutons qui arrête un script en cours d'exécution.

        Normalement, le bouton central est utilisé pour arrêter un script en cours d'exécution. Vous pouvez
        changer ou désactiver ce comportement afin d'utiliser le bouton à d'autres fins.

        Arguments:
            button (Button): Un bouton tel que
                :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>`,
                ou un tuple de plusieurs boutons. Choisissez ``None`` pour désactiver le
                bouton d'arrêt complètement. Si vous le faites, vous pouvez toujours éteindre le hub
                en maintenant le bouton central enfoncé pendant trois secondes.
        """

    def shutdown(self) -> None:
        """shutdown()

        Arrête votre programme et éteint le hub."""

    def reset_reason(self) -> int:
        """reset_reason() -> int

        Découvre comment et pourquoi le hub a (re)démarré. Cela peut être utile pour
        diagnostiquer certains problèmes.

        Returns:
            * ``0`` si le hub a été précédemment éteint
              normalement.
            * ``1`` si le hub a redémarré automatiquement, comme
              après une mise à jour du firmware.
            * ``2`` si le hub a précédemment
              planté en raison d'un dépassement de délai de surveillance, ce qui indique un problème de firmware.
        """

    def name(self) -> str:
        """name() -> str

        Obtient le nom du hub. C'est le nom que vous voyez lors de la connexion
        via Bluetooth.

        Returns:
            Le nom du hub.
        """

    @overload
    def storage(self, offset: int, *, read: int) -> bytes: ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None: ...

    def storage(self, offset, read=None, write=None):
        """
        storage(offset, write=)
        storage(offset, read=) -> bytes

        Lit ou écrit des données binaires dans le stockage persistant.

        Cela vous permet de stocker des données qui peuvent être utilisées la prochaine fois que vous exécutez le
        programme.

        Les données seront enregistrées dans la mémoire flash lorsque vous éteignez le hub
        normalement. Elles ne seront pas enregistrées si les batteries sont retirées *pendant* que le
        hub est encore en cours d'exécution.

        Une fois enregistrées, les données resteront disponibles même après avoir retiré les
        batteries.

        Args:
            offset (int): Le décalage par rapport au début de la mémoire de stockage utilisateur, en octets.
            read (int): Le nombre d'octets à lire. Omettez cet argument lors de l'écriture.
            write (bytes): Les octets à écrire. Omettez cet argument lors de la lecture.

        Returns:
            Les octets lus si en lecture, sinon ``None``.

        Raises:
            ValueError:
                Si vous essayez de lire ou d'écrire des données en dehors de la plage autorisée.
        """


class DCMotor:
    """Classe générique pour contrôler des moteurs simples sans capteurs de rotation, tels que les moteurs de train."""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Port auquel le moteur est connecté.
            positive_direction (Direction): La direction dans laquelle le moteur doit
                tourner lorsque vous donnez une valeur de cycle de service positive.
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        Fait tourner le moteur à un cycle de service donné (également connu sous le nom de "puissance").

        Arguments:
            duty (Number, %): Le cycle de service (-100.0 à 100).
        """

    def stop(self) -> None:
        """stop()

        Arrête le moteur et le laisse tourner librement.

        Le moteur s'arrête progressivement en raison de la friction."""

    def brake(self) -> None:
        """brake()

        Freine passivement le moteur.

        Le moteur s'arrête en raison de la friction, plus la tension qui
        est générée pendant que le moteur est encore en mouvement."""

    @overload
    def settings(self, max_voltage: Number) -> None: ...

    @overload
    def settings(self) -> Tuple[int]: ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> Tuple[int]

        Configure les paramètres du moteur. Si aucun argument n'est donné,
        cela renvoie les valeurs actuelles.

        Arguments:
            max_voltage (Number, mV):
                Tension maximale appliquée au moteur pendant toutes les commandes du moteur.
        """


class Control:
    """Classe pour interagir avec le contrôleur PID et les paramètres."""

    scale: int

    """
    Facteur de mise à l'échelle entre la variable entière contrôlée
    et la sortie physique. Par exemple, pour un seul
    moteur, c'est le nombre d'impulsions de l'encodeur par degré de rotation.
    """

    @overload
    def limits(
        self,
        speed: Optional[Number] = None,
        acceleration: Optional[Number] = None,
        torque: Optional[Number] = None,
    ) -> None: ...

    @overload
    def limits(self) -> Tuple[int, int, int]: ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> Tuple[int, int, int]

        Configure la vitesse maximale, l'accélération et le couple.

        Si aucun argument n'est donné, cela renvoie les valeurs actuelles.

        La nouvelle limite ``acceleration`` et ``speed`` deviendra effective
        lorsque vous donnez une nouvelle commande au moteur. Les manœuvres en cours ne sont pas affectées.

        Arguments:
            speed (Number, deg/s or Number, mm/s):
                Vitesse maximale. Toutes les commandes de vitesse seront limitées à cette valeur.
            acceleration (Number, deg/s² or Number, mm/s²):
                Pente de la courbe de vitesse lors de l'accélération ou de la décélération.
                Utilisez un tuple pour définir l'accélération et la décélération séparément.
                Si une valeur est donnée, elle est utilisée pour les deux.
            torque (:ref:`torque`):
                Couple de rétroaction maximal pendant le contrôle.
        """

    @overload
    def pid(
        self,
        kp: Optional[Number] = None,
        ki: Optional[Number] = None,
        kd: Optional[Number] = None,
        integral_deadzone: Optional[Number] = None,
        integral_rate: Optional[Number] = None,
    ) -> None: ...

    @overload
    def pid(self) -> Tuple[int, int, int, int, int]: ...

    def pid(self, *args):
        """pid(kp, ki, kd, integral_deadzone, integral_rate)
        pid() -> Tuple[int, int, int, int, int]

        Obtient ou définit les valeurs PID pour le contrôle de la position et de la vitesse.

        Si aucun argument n'est donné, cela renvoie les valeurs actuelles.

        Arguments:
            kp (int): Constante de contrôle proportionnelle de la position.
                C'est le couple de rétroaction par degré d'erreur : µNm/deg.
            ki (int): Constante de contrôle intégrale de la position. C'est le couple de rétroaction
                par degré accumulé d'erreur : µNm/(deg s).
            kd (int): Constante de contrôle dérivée de la position (ou proportionnelle à la vitesse).
                C'est le couple de rétroaction par unité de vitesse : µNm/(deg/s).
            integral_deadzone (Number, deg or Number, mm): Zone autour de
                la cible où l'intégrale de l'erreur ne s'accumule pas.
            integral_rate (Number, deg/s or Number, mm/s): Taux maximal
                auquel l'intégrale de l'erreur est autorisée à croître.
        """

    @overload
    def target_tolerances(
        self, speed: Optional[Number] = None, position: Optional[Number] = None
    ) -> None: ...

    @overload
    def target_tolerances(self) -> Tuple[int, int]: ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> Tuple[int, int]

        Obtient ou définit les tolérances qui indiquent quand une manœuvre est terminée.

        Si aucun argument n'est donné, cela renvoie les valeurs actuelles.

        Arguments:
            speed (Number, deg/s or Number, mm/s): Déviation autorisée
                par rapport à la vitesse zéro avant que le mouvement ne soit considéré comme terminé.
            position (Number, deg or :ref:`distance`): Déviation autorisée
                par rapport à la cible avant que le mouvement ne soit considéré comme terminé.
        """

    @overload
    def stall_tolerances(
        self, speed: Optional[Number] = None, time: Optional[Number] = None
    ) -> None: ...

    @overload
    def stall_tolerances(self) -> Tuple[int, int]: ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> Tuple[int, int]

        Obtient ou définit les tolérances de blocage.

        Si aucun argument n'est donné, cela renvoie les valeurs actuelles.

        Arguments:
            speed (Number, deg/s or Number, mm/s): Si le contrôleur
                ne peut pas atteindre cette vitesse pendant un certain ``temps`` même avec une action maximale,
                il est bloqué.
            time (Number, ms): Combien de temps le contrôleur doit être en dessous de cette
                vitesse minimale ``speed`` avant de dire qu'il est bloqué.
        """


class Model:
    """Classe pour interagir avec l'observateur d'état du moteur et les paramètres."""

    def state(self) -> Tuple[float, float, float, bool]:
        """state() -> Tuple[float, float, float, bool]

        Obtient l'angle estimé, la vitesse, le courant et l'état de blocage du moteur,
        en utilisant un modèle de simulation qui imite le moteur réel.
        Ces estimations sont mises à jour plus rapidement que les mesures réelles,
        ce qui peut être utile lors de la création de vos propres contrôleurs PID.

        Pour la plupart des applications, il est préférable d'utiliser les mesures *réelles*
        :meth:`angle <pybricks.pupdevices.Motor.angle>`,
        :meth:`speed <pybricks.pupdevices.Motor.speed>`,
        :meth:`load <pybricks.pupdevices.Motor.load>`, et
        :meth:`stall <pybricks.pupdevices.Motor.stalled>`.

        Returns:
            Tuple avec l'angle estimé (deg), la vitesse (deg/s), le courant (mA),
            et l'état de blocage (``True`` ou ``False``).
        """

    @overload
    def settings(self, values: tuple) -> None: ...

    @overload
    def settings(self) -> tuple: ...

    def settings(self, speed, time):
        """settings(values)
        settings() -> Tuple

        Obtient ou définit les paramètres du modèle sous forme de tuple d'entiers. Si aucun argument n'est
        donné, cela renvoie les valeurs actuelles. Cette méthode est principalement utilisée
        pour déboguer la classe du modèle de moteur. La modification de ces paramètres ne devrait pas
        être nécessaire dans les programmes utilisateur.

        .. _model settings: https://docs.pybricks.com/projects/pbio/en/latest/struct__pbio__observer__settings__t.html

        Arguments:
            values (Tuple): Tuple with `model settings`_.
        """


class Motor(DCMotor):
    """Classe générique pour contrôler les moteurs avec capteurs de rotation intégrés."""

    control = Control()
    """Les moteurs utilisent le contrôle PID pour suivre avec précision les cibles de vitesse et
    d'angle que vous spécifiez. Vous pouvez changer son comportement via l'attribut
    ``control`` du moteur. Voir :ref:`control` pour un aperçu
    des méthodes disponibles."""

    model = Model()
    """Modèle représentant l'observateur qui estime l'état du moteur."""

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
                trains d'engrenages, tels que ``[[12, 36], [20, 16, 40]]``.

                Lorsque vous spécifiez un train d'engrenages, toutes les commandes et paramètres du moteur
                sont automatiquement ajustés pour tenir compte du rapport de démultiplication résultant.
                La direction du moteur reste inchangée par cela.
            reset_angle (bool):
                Choisissez ``True`` pour réinitialiser la valeur du capteur de rotation à l'angle du
                marqueur absolu (entre -180 et 179).
                Choisissez ``False`` pour conserver la
                valeur actuelle, afin que votre programme sache où il s'est arrêté la dernière fois.
            profile (Number, deg): Profil de précision. Il s'agit de la tolérance de position approximative
                en degrés qui est acceptable dans votre application. Une valeur plus basse donne un mouvement
                plus précis mais plus erratique ; une valeur plus élevée donne un mouvement moins précis mais plus fluide.
                Si aucune valeur n'est donnée, un profil approprié pour ce type de moteur sera sélectionné automatiquement
                (environ 11 degrés).
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Obtient l'angle de rotation du moteur.

        Returns:
            Angle du moteur.
        """

    def speed(self, window: Number = 100) -> int:
        """speed(window=100) -> int: deg/s

        Obtient la vitesse du moteur.

        La vitesse est mesurée comme le changement de l'angle du moteur pendant la
        fenêtre de temps donnée. Une fenêtre courte rend la valeur de la vitesse plus
        réactive au mouvement du moteur, mais moins stable. Une fenêtre longue rend la
        valeur de la vitesse moins réactive, mais plus stable.

        Arguments:
            window (Number, ms): La fenêtre de temps utilisée pour déterminer la vitesse.

        Returns:
            Vitesse du moteur.
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Vérifie si le moteur est actuellement bloqué.

        Il est bloqué lorsqu'il ne peut pas atteindre la vitesse ou la position cible, même
        avec le signal d'action maximale.

        Returns:
            ``True`` si le moteur est bloqué, ``False`` sinon.
        """

    def load(self) -> int:
        """load() -> int: mNm

        Estime la charge qui retient le moteur lorsqu'il essaie de bouger.

        Returns:
            Le couple de charge.
        """

    def reset_angle(self, angle: Optional[Number]) -> None:
        """
        reset_angle(angle)

        Définit l'angle de rotation accumulé du moteur à une valeur souhaitée.

        Arguments:
            angle (Number, deg): Valeur à laquelle l'angle doit être réinitialisé.
        """

    def hold(self) -> None:
        """hold()

        Arrête le moteur et le maintient activement à son angle actuel."""

    def run(self, speed: Number) -> None:
        """run(speed)

        Fait tourner le moteur à une vitesse constante.

        Le moteur accélère jusqu'à la vitesse donnée et continue de tourner à cette
        vitesse jusqu'à ce que vous donniez une nouvelle commande.

        Arguments:
            speed (Number, deg/s): Vitesse du moteur.
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        Fait tourner le moteur à une vitesse constante pendant un certain temps.

        Le moteur accélère jusqu'à la vitesse donnée, continue de tourner à cette vitesse,
        puis décélère. La manœuvre totale dure exactement le temps donné.

        Arguments:
            speed (Number, deg/s): Vitesse du moteur.
            time (Number, ms): Durée de la manœuvre.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que la manœuvre soit terminée avant de continuer
                avec le reste du programme.
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        Fait tourner le moteur à une vitesse constante d'un certain angle.

        Arguments:
            speed (Number, deg/s): Vitesse du moteur.
            rotation_angle (Number, deg): Angle de rotation du moteur.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que la manœuvre soit terminée avant de continuer
                avec le reste du programme.
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        Fait tourner le moteur à une vitesse constante vers un angle cible donné.

        La direction de rotation est automatiquement sélectionnée en fonction de l'angle cible.
        Il n'importe pas si ``speed`` est positif ou négatif.

        Arguments:
            speed (Number, deg/s): Vitesse du moteur.
            target_angle (Number, deg): Angle que le moteur doit atteindre.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que le moteur atteigne la cible
                avant de continuer avec le reste du programme.
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Optional[Number] = None,
    ) -> MaybeAwaitableInt:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        Fait tourner le moteur à une vitesse constante jusqu'à ce qu'il soit bloqué.

        Arguments:
            speed (Number, deg/s): Vitesse du moteur.
            then (Stop): Que faire après l'arrêt.
            duty_limit (Number, %): Limite de cycle de service pendant cette
                commande. Cela est utile pour éviter d'appliquer le couple maximal du moteur
                à un mécanisme à engrenages ou à levier. Si c'est ``None``, la
                limite de cycle de service ne sera pas modifiée pendant cette commande.

        Returns:
            Angle auquel le moteur devient bloqué.
        """

    def done(self) -> bool:
        """done() -> bool

        Vérifie si une commande ou une manœuvre en cours est terminée.

        Returns:
            ``True`` si la commande est terminée, ``False`` sinon.
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        Suit un angle cible. Cela est similaire à :meth:`.run_target`, mais
        l'accélération habituelle est ignorée : il se déplacera vers l'angle cible
        aussi rapidement que possible. Cette méthode est utile si vous souhaitez
        changer continuellement l'angle cible.

        Arguments:
            target_angle (Number, deg): Angle cible que le moteur doit atteindre.
        """

    def close(self) -> None:
        """close()

        Ferme l'objet moteur afin que vous puissiez appeler ``Motor`` à nouveau pour initialiser
        un nouvel objet.

        Cela permet aux utilisateurs avancés de changer des propriétés telles que l'engrenage au
        milieu du programme, ce qui peut être utile pour les accessoires amovibles.
        """


class Speaker:
    """Joue des bips et des sons à l'aide d'un haut-parleur."""

    @overload
    def volume(self, volume: Number) -> None: ...

    @overload
    def volume(self) -> int: ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        Obtient ou définit le volume du haut-parleur.

        Si aucun volume n'est donné, cette méthode renvoie le volume actuel.

        Arguments:
            volume (Number, %): Volume du haut-parleur dans la plage de 0 à 100.
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> MaybeAwaitable:
        """beep(frequency=500, duration=100)

        Joue un bip/ton.

        Arguments:
            frequency (Number, Hz):
                Fréquence du bip dans la plage de 64 à 24000 Hz.
            duration (Number, ms):
                Durée du bip. Si la durée est inférieure
                à 0, alors la méthode renvoie immédiatement et la fréquence
                continue de jouer indéfiniment.
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> MaybeAwaitable:
        """play_notes(notes, tempo=120)

        Joue une séquence de notes musicales. Par exemple :
        ``["C4/4", "C4/4", "G4/4", "G4/4"]``.

        Chaque note est une chaîne de caractères avec le format suivant :

            - Le premier caractère est le nom de la note, ``A`` à ``G``
              ou ``R`` pour un silence.
            - Les noms de notes peuvent également inclure un accidentel ``#`` (dièse) ou
              ``b`` (bémol). ``B#``/``Cb`` et ``E#``/``Fb`` ne sont pas
              autorisés.
            - Le nom de la note est suivi du numéro de l'octave ``2``
              à ``8``. Par exemple, ``C4`` est le do central. L'octave change
              au numéro suivant à la note C, par exemple, ``B3`` est la
              note en dessous du do central (``C4``).
            - L'octave est suivie de ``/`` et d'un nombre qui indique
              la taille de la note. Par exemple, ``/4`` est une noire,
              ``/8`` est une croche, etc.
            - Cela peut être suivi facultativement d'un ``.`` pour faire une note pointée.
              Les notes pointées durent 1,5 fois plus longtemps que les notes sans point.
            - La note peut se terminer facultativement par un ``_`` qui est une liaison ou un
              legato. Cela fait qu'il n'y a pas de pause entre cette note et
              la note suivante.

        Arguments:
            notes (iter):
                Une séquence de notes à jouer.
            tempo (int):
                Battements par minute. Une noire est un battement.
        """


class ColorLight:
    """Contrôle une lumière multicolore."""

    def on(self, color: Color) -> None:
        """on(color)

        Allume la lumière à la couleur spécifiée.

        Arguments:
            color (Color): Couleur de la lumière.
        """

    def off(self) -> None:
        """off()

        Éteint la lumière."""

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        Fait clignoter la lumière à une couleur donnée en l'allumant et en l'éteignant pour des
        durées données.

        La lumière continue de clignoter indéfiniment pendant que le reste de votre
        programme continue de fonctionner.

        Cette méthode fournit un moyen simple de créer des motifs de base mais utiles.
        Pour des motifs plus génériques et multicolores, utilisez ``animate()``
        à la place.

        Arguments:
            color (Color): Couleur de la lumière.
            durations (list): Séquence de valeurs temporelles de la
                forme ``[on_1, off_1, on_2, off_2, ...]``.
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        Anime la lumière avec une séquence de couleurs, affichées une par
        une pour l'intervalle donné.

        L'animation se déroule en arrière-plan pendant que le reste de votre programme
        continue de fonctionner. Lorsque l'animation est terminée, elle se répète.

        Arguments:
            colors (list): Séquence de valeurs :class:`Color <.parameters.Color>`.
            interval (Number, ms): Temps entre les mises à jour des couleurs.
        """


class ExternalColorLight:
    """Contrôle une lumière multicolore."""

    def on(self, color: Color) -> MaybeAwaitable:
        """on(color)

        Allume la lumière à la couleur spécifiée.

        Arguments:
            color (Color): Couleur de la lumière.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Éteint la lumière.
        """


class LightArray3:
    """Contrôle un tableau de trois lumières monochromes."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Allume les lumières à la luminosité spécifiée.

        Arguments:
            brightness (Number or tuple, %):
                Utilisez une seule valeur pour définir la luminosité de toutes les lumières en même temps.
                Utilisez un tuple de trois valeurs pour définir la luminosité
                de chaque lumière individuellement.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Éteint toutes les lumières.
        """


class LightArray4(LightArray3):
    """Contrôle un tableau de quatre lumières monochromes."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Allume les lumières à la luminosité spécifiée.

        Arguments:
            brightness (Number or tuple, %):
                Utilisez une seule valeur pour définir la luminosité de toutes les lumières en même temps.
                Utilisez un tuple de quatre valeurs pour définir la luminosité
                de chaque lumière individuellement. L'ordre des lumières est montré
                dans l'image ci-dessus.
        """


class LightMatrix:
    """Contrôle une grille rectangulaire de lumières monochromes."""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        Initialise l'affichage de la matrice de lumières.

        Arguments:
            rows (int): Nombre de rangées dans la grille
            columns (int): Nombre de colonnes dans la grille
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        Définit l'orientation de l'affichage de la matrice de lumières.

        Seuls les nouvelles images et pixels affichés sont affectés. Le contenu de l'affichage
        existant reste inchangé.

        Arguments:
            top (Side): Quel côté de l'affichage de la matrice de lumières est "en haut" dans votre
                conception. Choisissez ``Side.TOP``, ``Side.LEFT``, ``Side.RIGHT``,
                ou ``Side.BOTTOM``.
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        Affiche une icône, représentée par une matrice de valeurs de :ref:`brightness`.

        Arguments:
            icon (Matrix): Matrice d'intensités (:ref:`brightness`). Une liste 2D est également acceptée.
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        Affiche une animation faite à l'aide d'une liste d'images.

        Chaque image a le même format que ci-dessus. Chaque image est
        affichée pendant l'intervalle donné. L'animation se répète
        indéfiniment pendant que le reste de votre programme continue de fonctionner.

        Arguments:
            matrices (iter): Séquence de
                :class:`Matrix <pybricks.tools.Matrix>` d'intensités.
            interval (Number, ms): Temps d'affichage de chaque image dans la liste.
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        Allume un pixel à la luminosité spécifiée.

        Arguments:
            row (Number): Indice de la grille verticale, commençant à 0 depuis le haut.
            column (Number): Indice de la grille horizontale, commençant à 0 depuis la gauche.
            brightness (Number :ref:`brightness`): Luminosité du pixel.
        """

    def off(self) -> None:
        """off()

        Éteint tous les pixels."""

    def number(self, number: Number) -> None:
        """number(number)

        Affiche un nombre dans la plage de -99 à 99.

        Un signe moins (``-``) est affiché comme un point faible
        au centre de l'affichage. Les nombres supérieurs à 99 sont
        affichés comme ``>``. Les nombres inférieurs à -99 sont affichés comme ``<``.

        Arguments:
            number (int): Le nombre à afficher.
        """

    def char(self, char: str) -> None:
        """char(char)

        Affiche un caractère ou un symbole sur la grille de lumières. Cela peut
        être n'importe quelle lettre (``a``--``z``), lettre majuscule (``A``--``Z``) ou l'un des
        symboles suivants : ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): Le caractère ou le symbole à afficher.
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        Affiche une chaîne de texte, un caractère à la fois, avec une pause
        entre chaque caractère. Après l'affichage du dernier caractère, toutes les lumières
        s'éteignent.

        Arguments:
            text (str): Le texte à afficher.
            on (Number, ms): Durée d'affichage d'un caractère.
            off (Number, ms): Durée d'extinction de l'affichage entre
                les caractères.
        """


class Keypad:
    """Obtient le statut des boutons sur une disposition de clavier."""

    def __init__(self, active_buttons): ...

    def pressed(self) -> Set[Button]:
        """pressed() -> Set[Button]

        Vérifie quels boutons sont actuellement enfoncés.

        Returns:
            Ensemble de boutons enfoncés.
        """


class Battery:
    """Obtient le statut d'une batterie."""

    def voltage(self) -> int:
        """voltage() -> int: mV

        Obtient la tension de la batterie.

        Returns:
            Tension de la batterie.
        """

    def current(self) -> int:
        """current() -> int: mA

        Obtient le courant fourni par la batterie.

        Returns:
            Courant de la batterie.
        """


class Charger:
    """Obtient le statut d'un chargeur de batterie."""

    def connected(self) -> bool:
        """connected() -> bool

        Vérifie si un chargeur est connecté via USB.

        Returns:
            ``True`` si un chargeur est connecté, ``False`` sinon.
        """

    def status(self) -> int:
        """status() -> int

        Obtient le statut du chargeur de batterie, représenté par l'une des
        valeurs suivantes. Cela correspond à l'indicateur lumineux de la batterie
        juste à côté du port USB.

            0. Non en charge (lumière éteinte).
            1. En charge (lumière rouge).
            2. La charge est terminée (lumière verte).
            3. Il y a un problème avec le chargeur (lumière jaune).

        Returns:
            Valeur du statut.
        """

    def current(self) -> int:
        """current() -> int: mA

        Obtient le courant de charge.

        Returns:
            Courant de charge.
        """


class SimpleAccelerometer:
    """Obtient des mesures d'un accéléromètre."""

    def acceleration(self) -> Tuple[int, int, int]:
        """acceleration() -> Tuple[int, int, int]: mm/s²

        Obtient l'accélération de l'appareil.

        Returns:
            Accélération le long des trois axes.
        """

    def up(self) -> Side:
        """up() -> Side

        Vérifie quel côté du hub est actuellement orienté vers le haut.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` ou ``Side.BACK``.
        """

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]

        Obtient les angles de tangage et de roulis. Cela est relatif à
        l'orientation neutre spécifiée par l'utilisateur :ref:`robotframe`.

        L'ordre de rotation est tangage-puis-roulis. Cela équivaut à une
        rotation positive le long de l'axe y du robot, puis à une rotation positive
        le long de l'axe x.

        Returns:
            Tuple des angles de tangage et de roulis en degrés.
        """


class Accelerometer(SimpleAccelerometer):
    """Obtient des mesures d'un accéléromètre."""

    @overload
    def acceleration(self, axis: Axis) -> float: ...

    @overload
    def acceleration(self) -> Matrix: ...

    def acceleration(self, *args):
        """
        acceleration(axis) -> float: mm/s²
        acceleration() -> vector: mm/s²

        Obtient l'accélération de l'appareil le long d'un axe donné dans le
        :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axe le long duquel l'accélération doit être
                         mesurée.
        Returns:
            Accélération le long de l'axe spécifié. Si vous ne spécifiez aucun axe,
            cela renvoie un vecteur d'accélérations le long de tous les axes.
        """


class IMU(Accelerometer):
    def ready(self) -> bool:
        """ready() -> bool

        Vérifie si l'appareil est calibré et prêt à l'emploi.

        Cela devient ``True`` lorsque le robot est resté immobile pendant quelques
        secondes, ce qui permet à l'appareil de se recalibrer. Cela est ``False``
        si le hub vient d'être démarré, ou s'il n'a pas eu la chance de
        se calibrer pendant plus de 10 minutes.

        Returns:
            ``True`` s'il est prêt à l'emploi, ``False`` sinon.
        """

    def stationary(self) -> bool:
        """stationary() -> bool

        Vérifie si l'appareil est actuellement immobile (ne bouge pas).

        Returns:
            ``True`` s'il est immobile depuis au moins une seconde, ``False`` s'il est
            en mouvement.
        """

    @overload
    def settings(
        self,
        angular_velocity_threshold: float = None,
        acceleration_threshold: float = None,
    ) -> None: ...

    @overload
    def settings(self) -> Tuple[float, float]: ...

    def settings(self, *args):
        """
        settings(angular_velocity_threshold, acceleration_threshold)
        settings() -> Tuple[float, float]

        Configure les paramètres de l'IMU. Si aucun argument n'est donné,
        cela renvoie les valeurs actuelles.

        Les ``angular_velocity_threshold`` et ``acceleration_threshold``
        définissent quand le hub est considéré comme immobile. Si toutes les
        mesures restent en dessous de ces seuils pendant une seconde, l'IMU
        se recalibrera.

        Dans une pièce bruyante avec de fortes vibrations ambiantes (comme une
        salle de compétition), il est recommandé d'augmenter légèrement les seuils
        pour donner à votre robot la chance de se calibrer.
        Pour vérifier que vos paramètres fonctionnent comme prévu, testez que
        la méthode ``stationary()`` renvoie ``False`` si votre robot est en mouvement,
        et ``True`` s'il est immobile depuis au moins une seconde.

        Arguments:
            angular_velocity_threshold (Number, deg/s): Le seuil pour
                la vitesse angulaire. La valeur par défaut est de 1,5 deg/s.
            acceleration_threshold (Number, mm/s²): Le seuil pour la vitesse
                angulaire. La valeur par défaut est de 250 mm/s².
        """

    def heading(self) -> float:
        """heading() -> float: deg

        Obtient l'angle de cap de votre robot. Une valeur positive signifie un
        virage dans le sens des aiguilles d'une montre.

        Le cap est de 0 lorsque votre programme démarre. La valeur continue de croître
        même lorsque le robot tourne de plus de 180 degrés. Elle ne revient pas à -180
        comme c'est le cas dans certaines applications.

        .. note:: *Pour l'instant, cette méthode ne garde une trace du cap que lorsque
                  le robot est sur une surface plane.*

                  Cela signifie que la valeur n'est
                  plus correcte si vous le soulevez de la table. Pour résoudre
                  cela, vous pouvez appeler ``reset_heading`` pour réinitialiser le cap à
                  une valeur connue *après* l'avoir reposé. Par exemple, vous
                  pourriez aligner votre robot avec le côté de la table de compétition
                  et réinitialiser le cap à 90 degrés comme nouveau point de départ.

        Returns:
            Angle de cap par rapport à l'orientation de départ.
        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        Réinitialise l'angle de cap accumulé du robot.

        Arguments:
            angle (Number, deg): Valeur à laquelle le cap doit être réinitialisé.
        """

    @overload
    def angular_velocity(self, axis: Axis) -> float: ...

    @overload
    def angular_velocity(self) -> Matrix: ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis) -> float: deg/s
        angular_velocity() -> vector: deg/s

        Obtient la vitesse angulaire de l'appareil le long d'un axe donné dans
        le :ref:`robot reference frame <robotframe>`.

        Arguments:
            axis (Axis): Axe le long duquel la vitesse angulaire doit être
                         mesurée.
        Returns:
            Vitesse angulaire le long de l'axe spécifié. Si vous ne spécifiez aucun axe,
            cela renvoie un vecteur d'accélérations le long de tous les axes.
        """

    def rotation(self, axis: Axis) -> float:
        """
        rotation(axis) -> float: deg

        Obtient la rotation de l'appareil le long d'un axe donné dans
        le :ref:`robot reference frame <robotframe>`.

        Cette valeur est utile si votre robot *ne* tourne *que* le long de l'axe demandé.
        Pour un mouvement tridimensionnel général, utilisez plutôt la
        méthode ``orientation()``.

        La valeur commence à compter à partir de ``0`` lorsque vous initialisez cette classe.

        Arguments:
            axis (Axis): Axe le long duquel la rotation doit être mesurée.
        Returns:
            L'angle de rotation.
        """

    def orientation(self) -> Matrix:
        """
        orientation() -> Matrix

        Obtient l'orientation tridimensionnelle du robot dans
        le :ref:`robot reference frame <robotframe>`.

        Cela renvoie une matrice de rotation dont les colonnes représentent les axes ``X``, ``Y``,
        et ``Z`` du robot.

        .. note:: Cette méthode n'est pas encore implémentée.

        Returns:
            La matrice de rotation.
        """


class CommonColorSensor:
    """Capteur de couleur générique qui prend en charge la calibration des couleurs Pybricks."""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Port auquel le capteur est connecté.
        """

    def color(self) -> MaybeAwaitableColor:
        """color() -> Color

        Scanne la couleur d'une surface.

        Vous choisissez les couleurs détectées à l'aide de la méthode
        ``detectable_colors()``. Par défaut, il détecte
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, ou ``Color.NONE``.

        Returns:
            Couleur détectée.
        """

    def hsv(self) -> MaybeAwaitableColor:
        """hsv() -> Color

        Scanne la couleur d'une surface.

        Cette méthode est similaire à ``color()``, mais elle donne la gamme complète
        de valeurs de teinte, de saturation et de luminosité, au lieu de les arrondir à la
        couleur détectable la plus proche.

        Returns:
            Couleur mesurée. La couleur est décrite par une teinte (0--359), une
            saturation (0--100), et une valeur de luminosité (0--100).
        """

    def ambient(self) -> MaybeAwaitableInt:
        """ambient() -> int: %

        Mesure l'intensité de la lumière ambiante.

        Returns:
            Intensité de la lumière ambiante, allant de 0% (sombre)
            à 100% (lumineux).
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Mesure la quantité de lumière réfléchie par une surface émise par le
        capteur.

        Returns:
            Réflexion mesurée, allant de 0% (aucune réflexion) à
            100% (haute réflexion).
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None: ...

    @overload
    def detectable_colors(self) -> Collection[Color]: ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        Configure les couleurs que la méthode ``color()`` doit détecter.

        Spécifiez uniquement les couleurs que vous souhaitez détecter dans votre application.
        De cette façon, les mesures en couleur complète sont arrondies à la couleur souhaitée la plus proche,
        et les autres couleurs sont ignorées. Cela améliore la fiabilité.

        Si vous ne donnez aucun argument, les couleurs actuellement choisies seront renvoyées.

        Lors de la programmation avec des blocs, cela est configuré dans le bloc de configuration du capteur.

        Arguments:
            colors (list or tuple): Liste d'objets :class:`Color <.parameters.Color>` :
                les couleurs que vous souhaitez détecter. Vous pouvez choisir
                des couleurs standard telles que ``Color.MAGENTA``, ou fournir vos
                propres couleurs comme ``Color(h=348, s=96, v=40)`` pour des résultats encore
                meilleurs. Vous mesurez vos propres couleurs avec la méthode
                ``hsv()``.
        """


class AmbientColorSensor(CommonColorSensor):
    """Comme CommonColorSensor, mais détecte également les couleurs ambiantes lorsque la lumière du capteur
    est éteinte"""

    def color(self, surface: bool = True) -> MaybeAwaitableColor:
        """color(surface=True) -> Color

        Scanne la couleur d'une surface ou d'une source lumineuse externe.

        Vous choisissez les couleurs détectées à l'aide de la méthode
        ``detectable_colors()``. Par défaut, il détecte
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, ou ``Color.NONE``.

        Arguments:
            surface (bool): Choisissez ``true`` pour scanner la couleur des objets
                et des surfaces. Choisissez ``false`` pour scanner la couleur des
                écrans et autres sources lumineuses externes.

        Returns:
            Couleur détectée.
        """

    def hsv(self, surface: bool = True) -> MaybeAwaitableColor:
        """hsv(surface=True) -> Color

        Scanne la couleur d'une surface ou d'une source lumineuse externe.

        Cette méthode est similaire à ``color()``, mais elle donne la gamme complète
        de valeurs de teinte, de saturation et de luminosité, au lieu de les arrondir à la
        couleur détectable la plus proche.

        Arguments:
            surface (bool): Choisissez ``true`` pour scanner la couleur des objets
                et des surfaces. Choisissez ``false`` pour scanner la couleur des
                écrans et autres sources lumineuses externes.

        Returns:
            Couleur mesurée. La couleur est décrite par une teinte (0--359), une
            saturation (0--100), et une valeur de luminosité (0--100).
        """


class BLE:
    """
    Bluetooth Low Energy.

    .. versionadded:: 3.3
    """

    def broadcast(self, data: Union[bool, int, float, str, bytes]) -> None:
        """broadcast(data)

        Commence à diffuser les données données sur
        le ``broadcast_channel`` que vous avez sélectionné lors de l'initialisation du hub.

        Les données peuvent être de type ``int``, ``float``, ``str``, ``bytes``,
        ``True``, ou ``False``, ou une liste de ceux-ci.

        Choisissez ``None`` pour arrêter la diffusion. Cela aide à améliorer les performances
        lorsque vous n'avez pas besoin de la fonction de diffusion, surtout lorsque vous observez
        en même temps.

        La taille totale des données est assez limitée (26 octets). ``True`` et
        ``False`` prennent chacun 1 octet. ``float`` prend 5 octets. ``int`` prend de 2 à
        5 octets selon la taille du nombre. ``str`` et ``bytes`` prennent
        le nombre d'octets dans l'objet plus un octet supplémentaire.

        Lors du multitâche, une seule tâche peut diffuser à la fois. Pour diffuser
        des informations à partir de plusieurs tâches (ou piles de blocs), vous pouvez utiliser une
        tâche séparée dédiée qui diffuse de nouvelles valeurs lorsque une ou plusieurs
        variables changent.

        Args:
            data: La valeur ou les valeurs à diffuser.

        .. versionadded:: 3.3
        """

    def observe(
        self, channel: int
    ) -> Optional[Tuple[Union[bool, int, float, str, bytes], ...]]:
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        Récupère les dernières données observées pour un canal donné.

        La réception des données est plus fiable lorsque le hub n'est pas connecté
        à un ordinateur ou à d'autres appareils en même temps.

        Args:
            channel (int): Le canal à observer (0 à 255).

        Returns:
            Les données reçues dans le même format qu'elles ont été envoyées, ou ``None``
            si aucune donnée récente n'est disponible.

        .. versionadded:: 3.3
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        Obtient la force du signal moyenne en dBm pour le canal donné.

        Cela indique à quelle distance se trouve l'appareil de diffusion. Les appareils proches
        peuvent avoir une force de signal d'environ -40 dBm, tandis que les appareils éloignés
        peuvent avoir une force de signal d'environ -70 dBm.

        Args:
            channel (int): Le numéro du canal (0 à 255).

        Returns:
            La force du signal ou ``-128`` s'il n'y a pas de données observées récentes.

        .. versionadded:: 3.3
        """

    def version(self) -> str:
        """version() -> str

        Obtient la version du firmware de la puce Bluetooth.

        .. versionadded:: 3.3
        """
