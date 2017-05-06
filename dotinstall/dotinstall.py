import os
import glob
import sys
import yaml
import argparse
import subprocess
import shlex

from logger import Logger
from util import *

out = Logger()
pkgManager = getSystemInstaller(out)

if __name__ == "__main__":
    src, conf, update, prompt = parseOptions(readOptions())

    stream = open(conf, "r")
    packages = yaml.load(stream)

    for package in packages:
        if prompt:
            out.header("\nInstall {} (Y/n)? ".format(package))
            if raw_input().strip().lower() == "n":
                continue
        else:
            out.header("\nInstalling {}\n".format(package))

        linkLocations = []
        overwrite = True
        prelink = []
        postlink = []
        dependencies = []
        symlinkedFiles = set()

        if not 'link' in packages[package]:
            out.error("No link attribute set.\n")
            exit(1)
        elif isinstance(packages[package]['link'], list):
            linkLocations = packages[package]['link']
        else:
            linkLocations = [
                {"*": packages[package]['link']},
                {".*": packages[package]['link']}
            ]

        if 'overwrite' in packages[package]:
            overwrite = packages[package]['overwrite']

        if 'prelink' in packages[package]:
            prelink = packages[package]['prelink']

        if 'postlink' in packages[package]:
            postlink = packages[package]['postlink']

        if 'dependencies' in packages[package]:
            dependencies = packages[package]['dependencies']

        if not update:
            for script in prelink:
                subprocess.call([expand(token) for token in shlex.split(script)])
            for dependency in dependencies:
                pkgManager.install(dependency)

        for linkLocation in linkLocations:
            for pattern, path in linkLocation.iteritems():
                location = expandPath(path)
                out.logPipe(subprocess.Popen(["mkdir", "-pv", location], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                for filename in glob.iglob(os.path.join(src, package, pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if overwrite:
                        out.logPipe(subprocess.Popen(["rm", os.path.join(expandPath(location), basename)], stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb')))
                        out.logPipe(subprocess.Popen(["ln", "-sfv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                    else:
                        out.logPipe(subprocess.Popen(["ln", "-sv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))

        if not update:
            for script in postlink:
                subprocess.call([expand(token) for token in shlex.split(script)])
