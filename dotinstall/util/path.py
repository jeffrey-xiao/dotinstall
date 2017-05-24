import os
import shutil


def expandPath(path):
    if path is None:
        return None
    return os.path.abspath(expand(path))


def expand(token):
    if token is None:
        return None
    return os.path.expanduser(os.path.expandvars(token))


def isBrokenSymlink(filepath):
    return os.path.islink(filepath) and not os.path.exists(filepath)


def clean(path):
    path = expand(path)
    if not os.path.exists(path) and not os.path.islink(path):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
