import subprocess

from dotinstall.installer.apt_installer import AptInstaller


def test_installer_exists(call_mock):
    AptInstaller().installer_exists()
    call_mock.assert_called_once_with(
        ["which", "apt-get"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_is_installed(popen_mock):
    popen_mock.return_value.communicate.return_value = [b" install ok installed "]

    assert AptInstaller()._is_installed("ack")
    popen_mock.assert_called_once_with(
        ["dpkg-query", "-W", "-f=${Status}", "ack"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )


def test_installer_install(call_mock):
    AptInstaller()._install("ack")
    call_mock.assert_called_once_with(
        ["sudo", "apt-get", "install", "-y", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
