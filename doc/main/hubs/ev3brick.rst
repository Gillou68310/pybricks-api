MINDSTORMS EV3 Brick
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/ev3device-ev3.png
    :width: 50%

.. autoclass:: pybricks.hubs.EV3Brick
    :no-members:

    .. rubric:: Utilisation des boutons

    .. automethod:: pybricks.hubs::EV3Brick.buttons.pressed

    .. rubric:: Utilisation de la lumière d'état du brick

    .. automethod:: pybricks.hubs::EV3Brick.light.on

    .. automethod:: pybricks.hubs::EV3Brick.light.off

    .. rubric:: Utilisation du haut-parleur

    .. automethod:: pybricks.hubs::EV3Brick.speaker.beep

    .. automethod:: pybricks.hubs::EV3Brick.speaker.play_notes

    .. automethod:: pybricks.hubs::EV3Brick.speaker.play_file

    .. automethod:: pybricks.hubs::EV3Brick.speaker.say

    .. automethod:: pybricks.hubs::EV3Brick.speaker.set_speech_options

    .. automethod:: pybricks.hubs::EV3Brick.speaker.set_volume

    .. rubric:: Utilisation de l'écran

    .. |this image| replace:: l'écran

    .. automethod:: pybricks.hubs::EV3Brick.screen.clear

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_text
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.print
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.set_font
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.load_image

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_image
        :noindex:

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_pixel

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_line

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_box

    .. automethod:: pybricks.hubs::EV3Brick.screen.draw_circle

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.width

    .. autoattribute:: pybricks.hubs::EV3Brick.screen.height

    .. automethod:: pybricks.hubs::EV3Brick.screen.save

    .. rubric:: Utilisation de la batterie

    .. automethod:: pybricks.hubs::EV3Brick.battery.voltage

    .. automethod:: pybricks.hubs::EV3Brick.battery.current

Exemples de lumière d'état
--------------------------

Allumer la lumière et changer la couleur
****************************************

.. literalinclude::
    ../../../examples/ev3/light_color/main.py

Exemples d'écran
----------------

Afficher une image sur l'écran
******************************

.. literalinclude::
    ../../../examples/ev3/screen_image/main.py

Dessiner des formes sur l'écran
*******************************

.. literalinclude::
    ../../../examples/ev3/screen_draw/main.py

Utiliser différentes polices
****************************

.. raw:: latex

    \begin{CJK}{UTF8}{gbsn}

.. literalinclude::
    ../../../examples/ev3/screen_print/main.py

.. raw:: latex

    \end{CJK}

.. rubric:: Langues et voix disponibles pour la parole

.. [#espeak_lang]

    Vous pouvez choisir les langues suivantes :

    - ``'af'``: Afrikaans
    - ``'an'``: Aragonais
    - ``'bg'``: Bulgare
    - ``'bs'``: Bosniaque
    - ``'ca'``: Catalan
    - ``'cs'``: Tchèque
    - ``'cy'``: Gallois
    - ``'da'``: Danois
    - ``'de'``: Allemand
    - ``'el'``: Grec
    - ``'en'``: Anglais (par défaut)
    - ``'en-gb'``: Anglais (Royaume-Uni)
    - ``'en-sc'``: Anglais (Écosse)
    - ``'en-uk-north'``: Anglais (Royaume-Uni, Nord)
    - ``'en-uk-rp'``: Anglais (Royaume-Uni, Prononciation Reçue)
    - ``'en-uk-wmids'``: Anglais (Royaume-Uni, Midlands de l'Ouest)
    - ``'en-us'``: Anglais (États-Unis)
    - ``'en-wi'``: Anglais (Antilles)
    - ``'eo'``: Espéranto
    - ``'es'``: Espagnol
    - ``'es-la'``: Espagnol (Amérique Latine)
    - ``'et'``: Estonien
    - ``'fa'``: Persan
    - ``'fa-pin'``: Persan
    - ``'fi'``: Finnois
    - ``'fr-be'``: Français (Belgique)
    - ``'fr-fr'``: Français (France)
    - ``'ga'``: Irlandais
    - ``'grc'``: Grec
    - ``'hi'``: Hindi
    - ``'hr'``: Croate
    - ``'hu'``: Hongrois
    - ``'hy'``: Arménien
    - ``'hy-west'``: Arménien (Occidental)
    - ``'id'``: Indonésien
    - ``'is'``: Islandais
    - ``'it'``: Italien
    - ``'jbo'``: Lojban
    - ``'ka'``: Géorgien
    - ``'kn'``: Kannada
    - ``'ku'``: Kurde
    - ``'la'``: Latin
    - ``'lfn'``: Lingua Franca Nova
    - ``'lt'``: Lituanien
    - ``'lv'``: Letton
    - ``'mk'``: Macédonien
    - ``'ml'``: Malayalam
    - ``'ms'``: Malais
    - ``'ne'``: Népali
    - ``'nl'``: Néerlandais
    - ``'no'``: Norvégien
    - ``'pa'``: Pendjabi
    - ``'pl'``: Polonais
    - ``'pt-br'``: Portugais (Brésil)
    - ``'pt-pt'``: Portugais (Portugal)
    - ``'ro'``: Roumain
    - ``'ru'``: Russe
    - ``'sk'``: Slovaque
    - ``'sq'``: Albanais
    - ``'sr'``: Serbe
    - ``'sv'``: Suédois
    - ``'sw'``: Swahili
    - ``'ta'``: Tamoul
    - ``'tr'``: Turc
    - ``'vi'``: Vietnamien
    - ``'vi-hue'``: Vietnamien (Hue)
    - ``'vi-sgn'``: Vietnamien (Saigon)
    - ``'zh'``: Chinois Mandarin
    - ``'zh-yue'``: Chinois Cantonais

    Vous pouvez choisir les voix suivantes :

    - ``'f1'``: variante féminine 1
    - ``'f2'``: variante féminine 2
    - ``'f3'``: variante féminine 3
    - ``'f4'``: variante féminine 4
    - ``'f5'``: variante féminine 5
    - ``'m1'``: variante masculine 1
    - ``'m2'``: variante masculine 2
    - ``'m3'``: variante masculine 3
    - ``'m4'``: variante masculine 4
    - ``'m5'``: variante masculine 5
    - ``'m6'``: variante masculine 6
    - ``'m7'``: variante masculine 7
    - ``'croak'``: croassement
    - ``'whisper'``: chuchotement
    - ``'whisperf'``: chuchotement féminin
