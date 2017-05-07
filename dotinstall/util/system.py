import subprocess
from installer import *


def getSystemInstaller():
    if subprocess.call(['which', 'apt-get'], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb')) == 0:
        return UbuntuInstaller()
    return None
