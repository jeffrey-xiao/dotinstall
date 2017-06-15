import subprocess
import os
import glob


import dotinstall.util.path as path
from dotinstall.util.logger import Logger


class Link(object):

    def execute(self, options, data, pkg_manager):
        symlinked_files = set()
        for link_location in data['linkLocations']:
            for pattern, dest_path in link_location.items():
                location = path.expand_path(dest_path)
                subprocess.call(
                    ["mkdir", "-pv", location], 
                    stderr=subprocess.DEVNULL,
                )
                for filename in glob.iglob(os.path.join(options['src'], data['package'], pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinked_files:
                        continue
                    symlinked_files.add(basename)

                    path = os.path.join(path.expand_path(location), basename)

                    if data['overwrite']:
                        subprocess.call(
                            ["rm", path], 
                            stderr=subprocess.DEVNULL,
                        )
                        subprocess.call(
                            ["ln", "-sfv", filename, path.expand_path(location)],
                        )
                    else:
                        subprocess.call(
                            ["ln", "-sv", filename, path.expand_path(location)],
                        )
