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


# import board
# import busio
# from uart_handler import UartHandler
# from logging import *
#
# uart = busio.UART(board.TX, board.RX, baudrate=115200)
# logger = Logger(UartHandler(uart))
# logger.level = INFO
# logger.info('testing')

from logging import LoggingHandler

class UartHandler(LoggingHandler):

    def __init__(self, uart):
        self._uart = uart

    def format(self, level, msg):
        return super().format(level, msg) + '\r\n'

    def emit(self, level, msg):
        self._uart.write(bytes(self.format(level, msg), 'utf-8'))
