import io
import os

import pytest

from testing.util import execute_install
from testing.util import expand_path
from testing.util import in_resource_path


@pytest.fixture(autouse=True)
def config():
    with in_resource_path("./testing/resources/simple"):
        execute_install(False, False)
        yield


def test_linking():
    assert os.path.islink(expand_path("./other_dist/2.txt"))


def test_overwrite():
    assert os.path.isfile(expand_path("./dist/1.txt"))
    with io.open(expand_path("./dist/1.txt")) as fin:
        assert fin.read().strip() == "1"


def test_prelink():
    assert os.path.isfile(expand_path("./dist/1.txt"))
    with io.open(expand_path("./dist/2.txt")) as fin:
        assert fin.read().strip() == "200"


def test_postlink():
    assert not os.path.exists(expand_path("./dist/3.txt"))


def test_clean():
    assert not os.path.exists(expand_path("./dist/broken1.txt"))
    assert not os.path.islink(expand_path("./dist/broken1.txt"))
    assert not os.path.exists(expand_path("./dist/broken2.txt"))
    assert not os.path.islink(expand_path("./dist/broken2.txt"))
