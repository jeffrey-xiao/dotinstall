import os


def expandPath(path):
    if path is None:
        return None
    return os.path.abspath(expand(path))


def expand(token):
    if token is None:
        return None
    return os.path.expanduser(os.path.expandvars(token))
