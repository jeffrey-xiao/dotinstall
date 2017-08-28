import builtins
import io
import os
import mock
import contextlib


import dotinstall.dotinstall as dotinstall
from tests.util import expand_path
from tests.util import execute_main
from tests.util import clean
from tests.util import in_resource_path

@contextlib.contextmanager
def config():
    with in_resource_path('./tests/resources/prompt') as temp_dir:
        execute_main(False, True)
        yield

def test_prompt_y():
    with mock.patch.object(builtins, 'input', return_value='y'):
        with config():
            assert os.path.exists(expand_path("./dist1/test1"))
            assert os.path.exists(expand_path("./dist2/test2"))

def test_prompt_n():
    with mock.patch.object(builtins, 'input', return_value='n'):
        with config():
            assert not os.path.exists(expand_path("~/test1/test1"))
            assert not os.path.exists(expand_path("~/test2/test2"))
