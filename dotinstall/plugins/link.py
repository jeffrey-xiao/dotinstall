import subprocess
import os
import glob


import dotinstall.util.path as path
from dotinstall.util.logger import Logger


class Link(object):
    def execute(self, options, data, pkgManager):
        symlinkedFiles = set()
        for linkLocation in data['linkLocations']:
            for pattern, destPath in linkLocation.items():
                location = path.expandPath(destPath)
                subprocess.call(["mkdir", "-pv", location], stderr=subprocess.DEVNULL)
                for filename in glob.iglob(os.path.join(options['src'], data['package'], pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if data['overwrite']:
                        subprocess.call(["rm", os.path.join(path.expandPath(location), basename)], stderr=subprocess.DEVNULL)
                        subprocess.call(["ln", "-sfv", filename, path.expandPath(location)])
                    else:
                        subprocess.call(["ln", "-sv", filename, path.expandPath(location)])
