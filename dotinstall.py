import io
import os
import glob
import yaml


import dotinstall.util.parser as parser
from dotinstall.plugins.prelink import Prelink
from dotinstall.plugins.dependency import Dependency
from dotinstall.plugins.link import Link
from dotinstall.plugins.postlink import Postlink
from dotinstall.plugins.clean import Clean
from dotinstall.installer.util import getSystemInstaller
from dotinstall.util.logger import Logger


pkgManager = getSystemInstaller()
plugins = [
    Prelink(), 
    Dependency(),
    Link(),
    Postlink(),
    Clean(),
]

if __name__ == "__main__":
    print(parser)
    options = parser.parseOptions(parser.readOptions())

    with io.open(options['conf'], "r") as f:
        packages = yaml.load(f)

    for package in packages:
        if options['prompt']:
            Logger.header("\nInstall {} (Y/n)? ".format(package))
            if input().strip().lower() == "n":
                continue
        else:
            Logger.header("\nInstalling {}\n".format(package))

        data = parser.parseData(packages[package], package)
        for plugin in plugins:
            plugin.execute(options, data, pkgManager)
