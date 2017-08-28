import os
import pytest

import dotinstall.dotinstall as dotinstall
from tests.util import expand_path
from tests.util import execute_main
from tests.util import clean
from tests.util import in_resource_path

@pytest.fixture(autouse=True)
def config():
    with in_resource_path('./tests/resources/no_clean') as temp_dir:
        execute_main(False, False)
        yield

def test_no_clean():
    assert not os.path.exists(expand_path("./dist/broken1.txt"))
    assert os.path.islink(expand_path("./dist/broken1.txt"))
    assert not os.path.exists(expand_path("./dist/broken2.txt"))
    assert os.path.islink(expand_path("./dist/broken2.txt"))
