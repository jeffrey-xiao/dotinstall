from level import Level
from util import *
import sys

class Logger(object):
    def log(self, level, message):
        sys.stdout.write('{}{}{}'.format(level, message, Level.END))

    def logPipe(self, pipe):
        self.log(Level.INFO, streamToString(pipe.stdout))
        self.log(Level.ERROR, streamToString(pipe.stderr))

    def normal(self, message):
        self.log(Level.NORMAL, message);

    def error(self, message):
        self.log(Level.ERROR, message)

    def warning(self, message):
        self.log(Level.WARNING, message)

    def success(self, message):
        self.log(Level.SUCCESS, message)

    def info(self, message):
        self.log(Level.INFO, message)

    def header(self, message):
        self.log(Level.HEADER, message)
