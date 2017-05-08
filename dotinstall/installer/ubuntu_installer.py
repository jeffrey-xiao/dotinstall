import subprocess
from installer import Installer
from util import *


class UbuntuInstaller(Installer):
    def _isInstalled(self, dependency):
        pipe = subprocess.Popen(["dpkg-query", "-W", "-f=${Status}", dependency], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return pipe.communicate()[0].decode().strip() == "install ok installed"

    def _install(self, dependency):
        return subprocess.call(["sudo", "apt-get", "install", "-y", dependency], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
