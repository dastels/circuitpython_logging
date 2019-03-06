"""
Logging for CircuitPython

Adafruit invests time and resources providing this open source code.
Please support Adafruit and open source hardware by purchasing
products from Adafruit!

Written by Dave Astels for Adafruit Industries
Copyright (c) 2019 Adafruit Industries
Licensed under the MIT license.

All text above must be included in any redistribution.
"""

class Logger(object):

    def __init__(self):
        self._level = 0


    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level - value
