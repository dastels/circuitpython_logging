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

import time

levels = [(0,  'NOTSET'),
          (10, 'DEBUG'),
          (20, 'INFO'),
          (30, 'WARNING'),
          (40, 'ERROR'),
          (50, 'CRITICAL')]

for value, name in levels:
    globals()[name] = value

def level_for(value):
    for i in range(len(levels)):
        if value < levels[i][0]:
            return levels[i-1][1]
    return levels[0][1]

class LoggingHandler(object):

    def format(self, level, msg):
        now = time.localtime()
        time_vals = (now.tm_year, now.tm_mon, now.tm_mday,
                     now.tm_hour, now.tm_min, now.tm_sec)
        timestamp = '%4d/%02d/%02d %02d:%02d:%02d' % time_vals
        return '{0}: {1} - {2}'.format(timestamp, level_for(level), msg)

    def emit(self, level, msg):
        raise NotImplementedError()

class PrintHandler(LoggingHandler):

    def emit(self, level, msg):
        print(self.format(level, msg))

# class FileHandler(LoggingHandler):

#     def __init__(self, filename):
#         self._file = open(filename, 'a+')

#     def emit(self, level, msg):
#         self._file.write(self.format(level, msg))
#         self._file.write('\n')

class Logger(object):

    def __init__(self, handler=None):
        self._level = NOTSET
        if handler is None:
            self._handler = PrintHandler()
        else:
            self._handler = handler

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def log(self, level, format_string, *args):
        if self._level != NOTSET and level >= self._level:
            self._handler.emit(level, format_string.format(*args))

    def debug(self, format_string, *args):
        self.log(DEBUG, format_string, *args)

    def info(self, format_string, *args):
        self.log(INFO, format_string, *args)

    def warning(self, format_string, *args):
        self.log(WARNING, format_string, *args)

    def error(self, format_string, *args):
        self.log(ERROR, format_string, *args)

    def critical(self, format_string, *args):
        self.log(CRITICAL, format_string, *args)
