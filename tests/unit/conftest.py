import subprocess
import sys

import mock
import pytest


@pytest.fixture
def mock_stdout():
    with mock.patch.object(sys.stdout, 'write') as _mock:
        yield _mock


@pytest.fixture
def call_mock():
    with mock.patch.object(subprocess, 'call') as _mock:
        yield _mock


@pytest.fixture
def popen_mock():
    with mock.patch.object(subprocess, 'Popen') as _mock:
        yield _mock
