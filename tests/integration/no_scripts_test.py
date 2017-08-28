import io
import pytest
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from tests.util import expand_path
from tests.util import execute_main
from tests.util import clean
from tests.util import in_resource_path

@pytest.fixture(autouse=True)
def config():
    with in_resource_path('./tests/resources/no_scripts') as temp_dir:
        execute_main(True, False)
        yield

def test_no_prelink():
    assert not os.path.exists(expand_path("./dist/1.txt"))

def test_no_postlink():
    assert not os.path.exists(expand_path("./dist/2.txt"))
