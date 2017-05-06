import subprocess
from installer import *

def getSystemInstaller(logger):
    if subprocess.call(['which', 'apt-get']) == 0:
        return UbuntuInstaller(logger)
    return None
