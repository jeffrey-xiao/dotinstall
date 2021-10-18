import io

import pytest

from testing.util import execute_install
from testing.util import expand_path
from testing.util import in_resource_path


@pytest.fixture(autouse=True)
def config():
    with in_resource_path("./testing/resources/no_overwrite"):
        execute_install(False, False)
        yield


def test_no_overwrite():
    with io.open(expand_path("./dist/1.txt")) as fin:
        assert fin.read().strip() == "original 1"
    with io.open(expand_path("./dist/2.txt")) as fin:
        assert fin.read().strip() == "original 2"
