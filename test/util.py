import os
import shutil


import dotinstall.dotinstall as dotinstall

 
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

def execute_main(test_name, update=False, prompt=False):
    base_dir = os.path.join(expand_path('./test/resources'), test_name)
    dotinstall.main({
        'src': base_dir,
        'conf': os.path.join(base_dir, 'config.yaml'),
        'update': update,
        'prompt': prompt,
    })
