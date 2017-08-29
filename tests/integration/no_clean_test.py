import os

import pytest

from testing.util import execute_install
from testing.util import expand_path
from testing.util import in_resource_path


@pytest.fixture(autouse=True)
def config():
    with in_resource_path('./testing/resources/no_clean'):
        execute_install(False, False)
        yield


def test_no_clean():
    assert not os.path.exists(expand_path('./dist/broken1.txt'))
    assert os.path.islink(expand_path('./dist/broken1.txt'))
    assert not os.path.exists(expand_path('./dist/broken2.txt'))
    assert os.path.islink(expand_path('./dist/broken2.txt'))
