Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/bill88t/CircuitPython_AXP313A/workflows/Build%20CI/badge.svg
    :target: https://github.com/bill88t/CircuitPython_AXP313A/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircuitPython module for managing the AXP313A pmic over I2C, along with the common voltages to power cameras with it.

Frozen Module
=============

This driver may be shipped with some CircuitPython installations.

``sys.path`` by default is ``['', '/', '.frozen', '/lib']`` which means frozen modules have higher priority than modules in the local filesystem.
To override the frozen version included in your build, you can install this driver inside your board's ``/`` or ``/lib`` and
set `sys.path` to prefer ``/lib`` and ``/`` like ``sys.path = ['', '/', '/lib', '.frozen']``.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-axp313a.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/bill88t/CircuitPython_AXP313A/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Based upon
============
https://github.com/cdjq/DFRobot_AXP313A/pull/3/files#diff-3215ea4bee1f616d66447d590a0a866c5d2dedc100061b25981a96b5ce006b39
