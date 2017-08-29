import subprocess

from dotinstall.installer.installer import Installer


class AptInstaller(Installer):

    def installer_exists(self):
        return subprocess.call(
            ['which', 'apt-get'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _is_installed(self, dependency):
        pipe = subprocess.Popen(
            ['dpkg-query', '-W', '-f=${Status}', dependency],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        return pipe.communicate()[0].decode().strip() == 'install ok installed'

    def _install(self, dependency):
        return subprocess.call(
            ['sudo', 'apt-get', 'install', '-y', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        ) == 0
