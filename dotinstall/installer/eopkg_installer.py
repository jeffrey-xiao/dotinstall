import subprocess

from dotinstall.installer.installer import Installer


class EopkgInstaller(Installer):

    def installer_exists(self):
        return subprocess.call(
            ['which', 'eopkg'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _is_installed(self, dependency):
        eopkg_pipe = subprocess.Popen(
            ['sudo', 'eopkg', 'it', '-n', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

        _, error = eopkg_pipe.communicate()

        return 'already installed' in error.decode('utf-8')

    def _install(self, dependency):
        return subprocess.call(
            ['sudo', 'eopkg', 'it', '-y', dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        ) == 0
