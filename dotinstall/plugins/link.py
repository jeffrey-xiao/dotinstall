import subprocess
import os
import glob
from util import *
from logger import Logger


class Link(object):
    def execute(self, options, data, pkgManager):
        symlinkedFiles = set()
        for linkLocation in data['linkLocations']:
            for pattern, path in linkLocation.items():
                location = expandPath(path)
                subprocess.call(["mkdir", "-pv", location], stderr=subprocess.DEVNULL)
                for filename in glob.iglob(os.path.join(options['src'], data['package'], pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if data['overwrite']:
                        subprocess.call(["rm", os.path.join(expandPath(location), basename)], stderr=subprcoess.DEVNULL)
                        subprocess.call(["ln", "-sfv", filename, expandPath(location)])
                    else:
                        subprocess.call(["ln", "-sv", filename, expandPath(location)])
