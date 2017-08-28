import io
import pytest
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from tests.util import expand_path
from tests.util import execute_install
from tests.util import clean
from tests.util import in_resource_path

@pytest.fixture(autouse=True)
def config():
    with in_resource_path('./tests/resources/no_overwrite') as temp_dir:
        execute_install(False, False)
        yield

def test_no_overwrite():
    with io.open(expand_path("./dist/1.txt")) as fin:
        assert fin.read().strip() == "original 1"
    with io.open(expand_path("./dist/2.txt")) as fin:
        assert fin.read().strip() == "original 2"
