import subprocess

from dotinstall.installer.brew_installer import BrewInstaller


def test_installer_exists(call_mock):
    BrewInstaller().installer_exists()
    call_mock.assert_called_once_with(
        ["which", "brew"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_is_installed(call_mock):
    BrewInstaller()._is_installed("ack")
    call_mock.assert_called_once_with(
        ["brew", "ls", "--versions", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_install(call_mock):
    BrewInstaller()._install("ack")
    call_mock.assert_called_once_with(
        ["brew", "install", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
