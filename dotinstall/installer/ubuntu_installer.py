import subprocess
from installer import Installer
from util import *

class UbuntuInstaller(Installer):
    def _isInstalled(self, dependency):
        pipe = subprocess.Popen(["dpkg-query", "-W", "-f=${Status}", dependency], stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb'))
        return streamToString(pipe.stdout).strip() == "install ok installed"

    def _install(self, dependency):
        return subprocess.call(["sudo", "apt-get", "install", "-y", dependency], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb')) == 0
