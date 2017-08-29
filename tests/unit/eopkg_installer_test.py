import subprocess

import mock
import pytest

from dotinstall.installer.eopkg_installer import EopkgInstaller


@pytest.fixture
def call_mock():
    with mock.patch.object(subprocess, 'call') as _mock:
        yield _mock


@pytest.fixture
def popen_mock():
    with mock.patch.object(subprocess, 'Popen') as _mock:
        yield _mock


def test_installer_exists(call_mock):
    EopkgInstaller().installer_exists()
    call_mock.assert_called_once_with(
        ['which', 'eopkg'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def test_installer_is_installed(popen_mock):
    pipe_1 = mock.Mock()
    pipe_2 = mock.Mock()
    popen_mock.side_effect = (pipe_1, pipe_2)

    EopkgInstaller()._is_installed('ack')

    expected_popen_calls = [
        mock.call(
            ['eopkg', 'li', '-i'],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ),
        mock.call(
            ['grep', '\back\b'],
            stdin=pipe_1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ),
    ]

    popen_mock.assert_has_calls(expected_popen_calls)
    pipe_2.communicate.assert_called_once()


def test_installer_install(call_mock):
    EopkgInstaller()._install('ack')
    call_mock.assert_called_once_with(
        ['sudo', 'eopkg', 'it', '-y', 'ack'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
