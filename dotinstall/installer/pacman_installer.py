import subprocess

from dotinstall.installer.installer import Installer


class PacmanInstaller(Installer):

    def installer_exists(self):
        return subprocess.call(
            ['which', 'pacman'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _is_installed(self, dependency):
        return subprocess.call(
            ['pacman', '-Q', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _install(self, dependency):
        return subprocess.call(
            ['sudo', 'pacman', '-S', '--noconfirm', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0
