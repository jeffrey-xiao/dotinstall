import os
import shutil


def expand_path(path):
    if path is None:  # pragma: no cover
        return None
    return os.path.abspath(expand(path))


def expand(token):  # pragma: no cover
    if token is None:
        return None
    return os.path.expanduser(os.path.expandvars(token))


def is_broken_symlink(filepath):
    return os.path.islink(filepath) and not os.path.exists(filepath)


def clean(path):
    path = expand(path)
    if not os.path.exists(path) and not os.path.islink(path):  # pragma: no cover
        return
    if os.path.isdir(path):  # pragma: no cover
        shutil.rmtree(path)
    else:
        os.remove(path)
