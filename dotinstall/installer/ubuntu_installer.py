import subprocess


from dotinstall.installer.installer import Installer


class UbuntuInstaller(Installer):
    def _is_installed(self, dependency):  # pragma: no cover
        pipe = subprocess.Popen(["dpkg-query", "-W", "-f=${Status}", dependency], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return pipe.communicate()[0].decode().strip() == "install ok installed"

    def _install(self, dependency):  # pragma: no cover
        return subprocess.call(["sudo", "apt-get", "install", "-y", dependency], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
