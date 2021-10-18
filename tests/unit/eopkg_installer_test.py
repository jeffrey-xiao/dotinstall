import subprocess

import mock
import pytest

from dotinstall.installer.eopkg_installer import EopkgInstaller


@pytest.fixture
def call_mock():
    with mock.patch.object(subprocess, "call") as _mock:
        yield _mock


@pytest.fixture
def popen_mock():
    with mock.patch.object(subprocess, "Popen") as _mock:
        yield _mock


def test_installer_exists(call_mock):
    EopkgInstaller().installer_exists()
    call_mock.assert_called_once_with(
        ["which", "eopkg"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_is_installed(popen_mock):
    popen_mock.return_value.communicate.return_value = (b"", b"")
    EopkgInstaller()._is_installed("ack")
    popen_mock.assert_called_once_with(
        ["sudo", "eopkg", "it", "-n", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )


def test_installer_install(call_mock):
    EopkgInstaller()._install("ack")
    call_mock.assert_called_once_with(
        ["sudo", "eopkg", "it", "-y", "ack"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
