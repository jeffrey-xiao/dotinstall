import subprocess


from dotinstall.installer.ubuntu_installer import UbuntuInstaller


def getSystemInstaller():
    if subprocess.call(['which', 'apt-get'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
        return UbuntuInstaller()
    return None
