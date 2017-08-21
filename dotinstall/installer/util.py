import subprocess


from dotinstall.installer.apt_installer import AptInstaller
from dotinstall.installer.brew_installer import BrewInstaller
from dotinstall.installer.eopkg_installer import EopkgInstaller


def get_system_installer():  # pragma: no cover
    has_apt_get = subprocess.call(
        ['which', 'apt-get'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ) == 0

    has_brew = subprocess.call(
        ['which', 'brew'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ) == 0

    has_eopkg = subprocess.call(
        ['which', 'eopkg'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ) == 0

    if has_apt_get:
        return AptInstaller()
    elif has_brew:
        return BrewInstaller()
    elif has_eopkg:
        return EopkgInstaller()
    return None
