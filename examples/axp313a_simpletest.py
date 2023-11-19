# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Bill Sideris for Feline Computers
#
# SPDX-License-Identifier: Unlicense

import board

# This is the intended way import this module
from AXP313A import *

# Use the i2c bus the axp313a is attached
pmic = AXP313A(board.CAM_I2C())

# This enables the voltages a OV2640 camera needs.
enable_camera(pmic, camera_voltages.OV2640)

# To cut power
disable_camera(pmic)
# or
pmic.disable_power()

# To set manual voltages (NOT RECOMMENDED)
pmic.set_power(1.2, 1.8)
