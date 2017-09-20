import glob
import os

import dotinstall.util.path as path
from dotinstall.util.logger import Logger


class Clean(object):

    def execute(self, options, data, pkg_manager):
        if data['clean']:
            folders = set()
            for link_location in data['linkLocations']:
                for pattern, dest_path in link_location.items():
                    location = path.expand_path(dest_path)
                    folders.add(location)

            for folder in folders:
                for pattern in ['.*', '*']:
                    for filename in glob.iglob(os.path.join(folder, pattern)):
                        if path.is_broken_symlink(filename):
                            path.clean(filename)
                            Logger.info(
                                "Removed broken symlink: '{}'\n".format(filename),
                            )
