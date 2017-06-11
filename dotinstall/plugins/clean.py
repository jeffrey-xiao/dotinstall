import os
import subprocess
import glob


import dotinstall.util.path as path
from dotinstall.util.logger import Logger


class Clean(object):
    def execute(self, options, data, pkgManager):
        if data['clean']:
            folders = set()
            for linkLocation in data['linkLocations']:
                for pattern, destPath in linkLocation.items():
                    location = path.expandPath(destPath)
                    folders.add(location)

            for folder in folders:
                for pattern in ['.*', '*']:
                    for filename in glob.iglob(os.path.join(folder, pattern)):
                        if path.isBrokenSymlink(filename):
                            path.clean(filename)
