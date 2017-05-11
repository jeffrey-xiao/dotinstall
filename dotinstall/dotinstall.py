import os
import glob
import yaml

from logger import Logger
from util import *
from installer import *
from plugins import *

pkgManager = getSystemInstaller()
plugins = [Prelink(), Dependency(), Link(), Postlink(), Clean()]

if __name__ == "__main__":
    options = parseOptions(readOptions())

    stream = open(options['conf'], "r")
    packages = yaml.load(stream)

    for package in packages:
        if options['prompt']:
            Logger.header("\nInstall {} (Y/n)? ".format(package))
            if input().strip().lower() == "n":
                continue
        else:
            Logger.header("\nInstalling {}\n".format(package))

        data = parseData(packages[package], package)
        for plugin in plugins:
            plugin.execute(options, data, pkgManager)
