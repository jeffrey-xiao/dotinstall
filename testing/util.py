import contextlib
import os
import shutil
import tempfile

import dotinstall.dotinstall as dotinstall


def expand_path(path):
    path = os.path.expandvars(path)
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    return path


def clean(path):
    path = expand_path(path)
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def execute_install(update=False, prompt=False):
    dotinstall.install({
        'src': os.getcwd(),
        'conf': os.path.join(os.getcwd(), 'config.yaml'),
        'update': update,
        'prompt': prompt,
    })


@contextlib.contextmanager
def in_resource_path(resource_path):
    working_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp()

    try:
        new_working_dir = os.path.join(temp_dir, 'src')
        shutil.copytree(os.path.abspath(resource_path), new_working_dir)
        os.chdir(new_working_dir)
        yield new_working_dir
    finally:
        os.chdir(working_dir)
        clean(temp_dir)
