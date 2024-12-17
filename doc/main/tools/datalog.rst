Enregistrement de données
^^^^^^^^^^^^^^^^^^^^^^^^^

Pour le moment, cette classe est uniquement disponible sur EV3.

.. autoclass:: pybricks.tools.DataLog
    :no-members:

    .. automethod:: pybricks.tools.DataLog.log

    Par défaut, cette classe crée un fichier ``csv`` sur la brique EV3 avec le
    nom ``log`` et la date et l'heure actuelles. Par exemple, si vous utilisez
    cette classe le 13 février 2020 à 10:07 et 44.431260 secondes, le fichier
    s'appelle ``log_2020_02_13_10_07_44_431260.csv``.

    Voir `managing files on the EV3`_ pour apprendre comment télécharger le
    fichier journal sur votre ordinateur.

Exemples
-------------------

Enregistrement et visualisation des mesures
*******************************************

Cet exemple montre comment enregistrer l'angle d'une roue tournante au fil du
temps.

.. literalinclude:: ../../../examples/ev3/datalog/main.py

Dans cet exemple, le fichier généré contient les éléments suivants::

    time, angle
    3, 0
    108, 6
    212, 30
    316, 71
    419, 124
    523, 176
    628, 228
    734, 281
    838, 333
    942, 385

Lorsque vous téléchargez le fichier sur votre ordinateur comme indiqué
ci-dessus, vous pouvez l'ouvrir dans un éditeur de tableur. Vous pouvez
ensuite générer un graphique des données, comme montré dans
:numref:`fig_datalog_graph`.

Dans cet exemple, nous voyons que l'angle du moteur change lentement au début.
Puis l'angle commence à changer plus rapidement, et le graphique devient une
ligne droite. Cela signifie que le moteur a atteint une vitesse constante.
Vous pouvez vérifier que l'angle augmente de 500 degrés par seconde.

.. _fig_datalog_graph:

.. figure:: ../../main/images/datalog_graph.png
    :width: 100 %

    Contenu du fichier original (à gauche) et graphique généré (à droite).

Utilisation des arguments optionnels
************************************

Cet exemple montre comment enregistrer des données au-delà des simples
nombres. Il montre également comment vous pouvez utiliser les arguments
optionnels de la classe ``DataLog`` pour choisir le nom et l'extension du
fichier.

Dans cet exemple, ``timestamp=False``, ce qui signifie que la date et l'heure
ne sont pas ajoutées au nom du fichier. Cela peut être pratique car le nom du
fichier sera toujours le même. Cependant, cela signifie que le contenu de
``my_file.txt`` sera écrasé chaque fois que vous exécuterez ce script.

.. literalinclude:: ../../../examples/ev3/datalog_extra/main.py

.. _managing files on the EV3: https://pybricks.com/install/mindstorms-ev3/running-programs#managing-files-on-the-ev3-brick
