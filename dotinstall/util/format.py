import subprocess


def get_output(cmd):
    ret = ''
    try:
        ret = subprocess.check_output(cmd.split()).decode('utf-8')
    except subprocess.CalledProcessError:  # pragma: no cover
        pass
    return ret


class Format(object):
    BOLD = get_output('tput bold')
    RESET = get_output('tput sgr0')

    BLUE = get_output('tput setaf 4')
    GREEN = get_output('tput setaf 2')
    YELLOW = get_output('tput setaf 3')
    RED = get_output('tput setaf 1')
