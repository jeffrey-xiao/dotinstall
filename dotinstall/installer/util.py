from dotinstall.installer.apt_installer import AptInstaller
from dotinstall.installer.brew_installer import BrewInstaller
from dotinstall.installer.eopkg_installer import EopkgInstaller

installers = [AptInstaller(), BrewInstaller(), EopkgInstaller()]


def get_system_installer():  # pragma: no cover
    for installer in installers:
        if installer.installer_exists():
            return installer
    return None
