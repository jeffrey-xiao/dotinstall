import subprocess


from dotinstall.installer.apt_installer import AptInstaller
from dotinstall.installer.brew_installer import BrewInstaller
from dotinstall.installer.eopkg_installer import EopkgInstaller


def get_system_installer():  # pragma: no cover
    if AptInstaller.installer_exists():
        return AptInstaller()
    elif BrewInstaller.installer_exists():
        return BrewInstaller()
    elif EopkgInstaller.installer_exists():
        return EopkgInstaller()
    return None
