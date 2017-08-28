import io
import os
import unittest
import pytest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from tests.util import expand_path
from tests.util import execute_main
from tests.util import clean
from tests.util import in_resource_path

@pytest.fixture(autouse=True)
def config():
    with in_resource_path('./tests/resources/simple') as temp_dir:
        execute_main(False, False)
        yield


def test_linking():
    assert os.path.islink(expand_path("./other_dist/2.txt"))

def test_no_overwrite():
    assert os.path.isfile(expand_path("./dist/1.txt"))
    with io.open(expand_path("./dist/1.txt")) as fin:
        assert fin.read().strip() == "1"

def test_prelink():
    with io.open(expand_path("./dist/2.txt")) as fin:
        assert fin.read().strip() == "2"

def test_postlink():
    assert not os.path.exists(expand_path("./dist/3.txt"))

def test_clean():
    assert not os.path.exists(expand_path("~/test/broken1.txt"))
    assert not os.path.islink(expand_path("~/test/broken1.txt"))
    assert not os.path.exists(expand_path("~/test/broken2.txt"))
    assert not os.path.islink(expand_path("~/test/broken2.txt"))
