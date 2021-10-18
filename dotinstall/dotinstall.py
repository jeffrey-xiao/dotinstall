import io

import yaml

import dotinstall.util.parser as parser
from dotinstall.installer.util import get_system_installer
from dotinstall.plugins.clean import Clean
from dotinstall.plugins.dependency import Dependency
from dotinstall.plugins.link import Link
from dotinstall.plugins.postlink import Postlink
from dotinstall.plugins.prelink import Prelink
from dotinstall.util.logger import Logger

pkg_manager = get_system_installer()
plugins = [
    Prelink(),
    Dependency(),
    Link(),
    Postlink(),
    Clean(),
]


def main():  # pragma: no cover
    options = parser.parse_options(parser.read_options())
    install(options)


def install(options):
    with io.open(options["conf"], "r") as f:
        packages = yaml.full_load(f)

    for package in options["packages"] or packages.keys():
        if package not in packages.keys():
            Logger.warning("\nPackage {} does not exist.\n".format(package))
            continue
        if options["prompt"]:
            Logger.header("\nInstall {} (Y/n)? ".format(package))
            resp = input().strip().lower()
            while resp != "n" and resp != "y" and resp != "":
                Logger.header(
                    "\nInvalid response '{}'. Install {} (Y/n)? ".format(resp, package),
                )
                resp = input().strip().lower()
            if resp == "n":
                continue
        else:
            Logger.header("\nInstalling {}.\n".format(package))

        data = parser.parse_data(packages[package], package)
        for plugin in plugins:
            plugin.execute(options, data, pkg_manager)
