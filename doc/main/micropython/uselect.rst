.. pybricks-requirements:: stm32-extra

:mod:`uselect` -- Attendre des événements
=========================================

.. automodule:: uselect
    :no-members:

    .. rubric:: Instance et classe Poll

    .. autofunction:: poll

    .. autoclass:: Poll
        :no-members:

        .. automethod:: register

        .. automethod:: unregister

        .. automethod:: modify

        .. automethod:: poll

        .. automethod:: ipoll

    .. rubric:: Drapeaux de masque d'événements

    .. autodata:: POLLIN

    .. autodata:: POLLOUT

    .. autodata:: POLLERR

    .. autodata:: POLLHUP

Exemples
---------------

Voir le `projects website`_ pour une démo utilisant ce module.

.. _projects website: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
