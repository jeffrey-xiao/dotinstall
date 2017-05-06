import os

def expandPath (path) :
    if path == None:
        return None
    return os.path.abspath(expand(path))

def expand (token):
    if token == None:
        return None
    return os.path.expanduser(os.path.expandvars(token))

