from dotinstall.util.format import Format


class Level(object):
    HEADER = Format.BOLD
    ERROR = Format.RED
    WARNING = Format.YELLOW
    SUCCESS = Format.GREEN
    INFO = Format.BLUE
    END = Format.RESET
    NORMAL = ''
