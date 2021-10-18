import mock
import pytest

from dotinstall.util.level import Level
from dotinstall.util.logger import Logger


@pytest.fixture
def mock_log():
    with mock.patch.object(Logger, "log") as _mock:
        yield _mock


def test_log(mock_stdout):
    Logger.log(Level.HEADER, "message")
    mock_stdout.assert_called_once_with(
        "{}{}{}".format(
            Level.HEADER,
            "message",
            Level.END,
        ),
    )


def test_normal(mock_log):
    Logger.normal("message")
    mock_log.assert_called_once_with(Level.NORMAL, "message")


def test_error(mock_log):
    Logger.error("message")
    mock_log.assert_called_once_with(Level.ERROR, "message")


def test_warning(mock_log):
    Logger.warning("message")
    mock_log.assert_called_once_with(Level.WARNING, "message")


def test_success(mock_log):
    Logger.success("message")
    mock_log.assert_called_once_with(Level.SUCCESS, "message")


def test_info(mock_log):
    Logger.info("message")
    mock_log.assert_called_once_with(Level.INFO, "message")


def test_header(mock_log):
    Logger.header("message")
    mock_log.assert_called_once_with(Level.HEADER, "message")
