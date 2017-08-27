import mock
import pytest
import sys
import dotinstall


@pytest.fixture
def mock_stdout():
    with mock.patch.object(sys.stdout, 'write') as _mock:
        yield _mock

@pytest.fixture
def mock_logger():
    with mock.patch.object(dotinstall.util.logger, 'Logger') as _mock:
        yield _mock
