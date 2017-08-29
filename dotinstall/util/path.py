import os


def expand_path(path):
    if path is None:
        return None
    path = os.path.expandvars(path)
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    return path


def is_broken_symlink(filepath):
    return os.path.islink(filepath) and not os.path.exists(filepath)


def clean(path):
    path = expand_path(path)
    assert is_broken_symlink(path)
    assert not os.path.isdir(path)
    os.remove(path)
