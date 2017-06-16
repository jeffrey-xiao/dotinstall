import subprocess


from dotinstall.installer.installer import Installer


class BrewInstaller(Installer):

    def _is_installed(self, dependency):  # pragma: no cover
        return subprocess.call(
            ["brew", "ls", "--versions", "python"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0

    def _install(self, dependency):  # pragma: no cover
        return subprocess.call(
            ["brew", "install", dependency],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ) == 0
