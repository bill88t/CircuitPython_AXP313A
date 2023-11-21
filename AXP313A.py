# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Bill Sideris
#
# SPDX-License-Identifier: MIT
"""
`AXP313A`
================================================================================

A CircuitPython module for managing the AXP313A pmic over I2C, along with the common voltages to power cameras with it.


* Author(s): Bill Sideris

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/bill88t/CircuitPython_AXP313A.git"

from time import sleep


class camera_voltages:
    """
    Contains preset values for specific camera sensors.\n
    Currently, the supported cameras are: ``OV2640`` and ``OV7725``.
    """

    OV2640 = [1.2, 2.8]
    OV7725 = [1.8, 3.3]


class AXP313A:
    """
    The main class. Create an object by passing an i2c bus.\n
    The bus does not need to be locked or ready at the time of creation.
    """

    def __init__(self, i2c):
        self.i2c = i2c

    def begin(self) -> bool:
        """
        Check if the chip is ready and available.\n
        Returns bool.
        """
        if not self.i2c.try_lock():
            return False
        scan = self.i2c.scan()
        self.i2c.unlock()
        return 0x36 in scan

    def set_power(self, DVDD: float, AVDDorDOVDD: float) -> bool:
        """
        Sets the power to the specified voltages.
        If an incorrect voltage is set, you got a firework in your hands.
        """
        if not self.begin():
            return False
        state = 0x19
        ALDOData = 0
        DLDOData = 0
        if (DVDD < 0.5) or (AVDDorDOVDD < 0.5):
            ALDOData = 0
            DLDOData = 0
        elif (DVDD > 3.5) or (AVDDorDOVDD > 3.5):
            ALDOData = 31
            DLDOData = 31
        else:
            ALDOData = (DVDD - 0.5) * 10
            DLDOData = (AVDDorDOVDD - 0.5) * 10
        self._writeb(0x10, state)
        sleep(0.01)
        self._writeb(0x16, int(ALDOData))
        sleep(0.01)
        self._writeb(0x17, int(DLDOData))
        sleep(0.01)
        return True

    def set_shutdown_key_level_time(self, offLevelTime: int) -> None:
        """
        An undocumented & unused function that was carried off
        from the dfrobot arduino / micropython modules.\n
        Seems to affect button press time.
        """
        data = offLevelTime << 1
        self._writeb(0x1E, data)
        sleep(0.01)

    def disable_power(self) -> None:
        """
        Set all the voltages to 0.
        """
        data = 0x01
        self._writeb(0x10, data)
        sleep(0.01)

    def _writeb(self, reg, data) -> None:
        buf = bytearray(1)
        buf[0] = reg
        buf.extend(bytearray([data]))
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(0x36, buf)
        finally:
            self.i2c.unlock()


def enable_camera(axpobject, camera: list) -> bool:
    """
    Quick function to enable power for a specific camera sensors.

    Call like: ``enable_camera(my_axp, camera_voltages.OV2640)``
    """
    return axpobject.set_power(camera[0], camera[1])


def disable_camera(axpobject) -> None:
    """
    An alias for disable_power.
    """
    axpobject.disable_power()
