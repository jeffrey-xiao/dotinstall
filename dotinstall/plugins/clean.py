import subprocess
import glob
from logger import Logger
from util import *


class Clean(object):
    def execute(self, options, data, pkgManager):
        if data['clean']:
            folders = set()
            for linkLocation in data['linkLocations']:
                for pattern, path in linkLocation.items():
                    location = expandPath(path)
                    folders.add(location)

            for folder in folders:
                for pattern in ['.*', '*']:
                    for filename in glob.iglob(os.path.join(folder, pattern)):
                        if isBrokenSymlink(filename):
                            clean(filename)
