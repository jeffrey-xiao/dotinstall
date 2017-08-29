import subprocess

from dotinstall.installer.installer import Installer


class BrewInstaller(Installer):

    def installer_exists(self):
        return subprocess.call(
            ['which', 'brew'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _is_installed(self, dependency):
        return subprocess.call(
            ['brew', 'ls', '--versions', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _install(self, dependency):
        return subprocess.call(
            ['brew', 'install', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        ) == 0
