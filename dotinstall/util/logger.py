import sys

from dotinstall.util.level import Level


class Logger(object):

    @classmethod
    def log(cls, level, message):
        sys.stdout.write('{}{}{}'.format(level, message, Level.END))

    @classmethod
    def normal(cls, message):
        cls.log(Level.NORMAL, message)

    @classmethod
    def error(cls, message):
        cls.log(Level.ERROR, message)

    @classmethod
    def warning(cls, message):
        cls.log(Level.WARNING, message)

    @classmethod
    def success(cls, message):
        cls.log(Level.SUCCESS, message)

    @classmethod
    def info(cls, message):
        cls.log(Level.INFO, message)

    @classmethod
    def header(cls, message):
        cls.log(Level.HEADER, message)
