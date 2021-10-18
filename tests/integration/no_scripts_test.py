import os

import pytest

from testing.util import execute_install
from testing.util import expand_path
from testing.util import in_resource_path


@pytest.fixture(autouse=True)
def config():
    with in_resource_path("./testing/resources/no_scripts"):
        execute_install(True, False)
        yield


def test_no_prelink():
    assert not os.path.exists(expand_path("./dist/1.txt"))


def test_no_postlink():
    assert not os.path.exists(expand_path("./dist/2.txt"))
