import builtins
import contextlib
import os

import mock

from testing.util import execute_install
from testing.util import expand_path
from testing.util import in_resource_path


@contextlib.contextmanager
def config():
    with in_resource_path("./testing/resources/prompt"):
        execute_install(False, True, ["test1"])
        yield


def test_positional():
    with mock.patch.object(builtins, "input", return_value="y"):
        with config():
            assert os.path.exists(expand_path("./dist1/test1"))
            assert not os.path.exists(expand_path("./dist2/test2"))
