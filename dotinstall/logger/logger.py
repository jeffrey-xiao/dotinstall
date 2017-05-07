import sys
import os
from .level import Level
from util import *


class Logger(object):
    @staticmethod
    def log(level, message):
        sys.stdout.write('{}{}{}'.format(level, message, Level.END))

    @staticmethod
    def logPipe(pipe):
        Logger.log(Level.INFO, streamToString(pipe.stdout))
        Logger.log(Level.ERROR, streamToString(pipe.stderr))

    @staticmethod
    def normal(message):
        Logger.log(Level.NORMAL, message)

    @staticmethod
    def error(message):
        Logger.log(Level.ERROR, message)

    @staticmethod
    def warning(message):
        Logger.log(Level.WARNING, message)

    @staticmethod
    def success(message):
        Logger.log(Level.SUCCESS, message)

    @staticmethod
    def info(message):
        Logger.log(Level.INFO, message)

    @staticmethod
    def header(message):
        Logger.log(Level.HEADER, message)
