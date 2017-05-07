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
                Logger.logPipe(subprocess.Popen(["mkdir", "-pv", location], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                for filename in glob.iglob(os.path.join(options['src'], data['package'], pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if data['overwrite']:
                        Logger.logPipe(subprocess.Popen(["rm", os.path.join(expandPath(location), basename)], stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb')))
                        Logger.logPipe(subprocess.Popen(["ln", "-sfv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                    else:
                        Logger.logPipe(subprocess.Popen(["ln", "-sv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
