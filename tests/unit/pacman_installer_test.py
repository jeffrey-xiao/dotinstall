import subprocess

from dotinstall.installer.pacman_installer import PacmanInstaller


def test_installer_exists(call_mock):
    PacmanInstaller().installer_exists()
    call_mock.assert_called_once_with(
        ["which", "pacman"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_is_installed(call_mock):
    PacmanInstaller()._is_installed("ack")
    call_mock.assert_called_once_with(
        ["pacman", "-Q", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_install(call_mock):
    PacmanInstaller()._install("ack")
    call_mock.assert_called_once_with(
        ["sudo", "pacman", "-S", "--noconfirm", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
