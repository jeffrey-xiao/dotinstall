import os
import glob
import yaml

from logger import *
from util import *
from plugins import *

pkgManager = getSystemInstaller()
plugins = [Prelink(), Dependency(), Link(), Postlink()]

if __name__ == "__main__":
    options = parseOptions(readOptions())

    stream = open(options['conf'], "r")
    packages = yaml.load(stream)

    for package in packages:
        if options['prompt']:
            Logger.header("\nInstall {} (Y/n)? ".format(package))
            if raw_input().strip().lower() == "n":
                continue
        else:
            Logger.header("\nInstalling {}\n".format(package))

        data = parseData(packages[package], package)
        for plugin in plugins:
            plugin.execute(options, data, pkgManager)

