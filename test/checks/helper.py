import os
import shutil


def expand_path(path):
    if path is None:
        return None
    return os.path.abspath(expand(path))


def expand(token):
    if token is None:
        return None
    return os.path.expanduser(os.path.expandvars(token))


def clean(path):
    path = expand(path)
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
