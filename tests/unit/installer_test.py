import mock

from dotinstall.installer.installer import Installer
from dotinstall.util.logger import Logger


def test_install_already_installed():
    with mock.patch.object(Logger, "info") as mock_logger:
        installer = Installer()
        installer._is_installed = mock.Mock(return_value=True)
        installer.install("ack")
        mock_logger.assert_called_once_with("'ack' is already installed.\n")


def test_install_successfully_installed():
    with mock.patch.object(Logger, "success") as mock_logger:
        installer = Installer()
        installer._is_installed = mock.Mock(return_value=False)
        installer._install = mock.Mock(return_value=True)
        installer.install("ack")
        mock_logger.assert_called_once_with("'ack' has been successfully installed.\n")


def test_install_error_installed():
    with mock.patch.object(Logger, "error") as mock_logger:
        installer = Installer()
        installer._is_installed = mock.Mock(return_value=False)
        installer._install = mock.Mock(return_value=False)
        installer.install("ack")
        mock_logger.assert_called_once_with("'ack' could not be installed.\n")
