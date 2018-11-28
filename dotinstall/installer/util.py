from dotinstall.installer.apt_installer import AptInstaller
from dotinstall.installer.brew_installer import BrewInstaller
from dotinstall.installer.eopkg_installer import EopkgInstaller
from dotinstall.installer.pacman_installer import PacmanInstaller

installers = [AptInstaller(), BrewInstaller(), EopkgInstaller(), PacmanInstaller()]


def get_system_installer():  # pragma: no cover
    for installer in installers:
        if installer.installer_exists():
            return installer
    return None
