import os
import glob
import sys
import yaml
import argparse
import subprocess
import shlex

from logger import Logger

def readOptions () :
    parser = argparse.ArgumentParser(description="Installation script for dotfiles.")
    parser.add_argument("-s", "--src", dest="src", metavar="dir",
        help="root directory of dotfiles")
    parser.add_argument("-c", "--conf", dest="conf", metavar="file",
        help="config file for symlinking and installing")
    parser.add_argument("-p", "--prompt", dest="prompt", action="store_true",
        help="prompt user before installing package")
    parser.add_argument("-u", "--update", dest="update", action="store_true",
        help="only symlinks files")

    return parser.parse_args()

def parseOptions () :
    src = expandPath(args.src) or os.path.dirname(os.path.realpath(os.join(__file__, "..", "..")))
    conf = expandPath(args.conf) or os.path.join(src, "config.yaml")
    update = args.update
    prompt = args.prompt

    return (src, conf, update, prompt)


def expandPath (path) :
    if path == None:
        return None
    return os.path.abspath(expand(path))

def expand (token):
    if token == None:
        return None
    return os.path.expanduser(os.path.expandvars(token))

if __name__ == "__main__":
    out = Logger()
    args = readOptions()
    src, conf, update, prompt = parseOptions()

    stream = open(conf, "r")
    packages = yaml.load(stream)

    for package in packages:
        if prompt:
            out.header("Install {} (Y/n)? ".format(package))
            if raw_input().strip().lower() == "n":
                continue
        else:
            out.header("Install {} (Y/n)? ".format(package))

        linkLocations = []
        overwrite = True
        prelink = []
        postlink = []
        dependencies = []
        symlinkedFiles = set()

        if not 'link' in packages[package]:
            raise ValueError('No link attribute set.')
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
                subprocess.call(["sudo", "apt-get", "install", dependency])

        for linkLocation in linkLocations:
            for pattern, path in linkLocation.iteritems():
                location = expandPath(path)
                subprocess.call(["mkdir", "-pv", location])
                for filename in glob.iglob(os.path.join(src, package, pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if overwrite:
                        subprocess.call(["rm", os.path.join(expandPath(location), basename)], stderr=open(os.devnull, 'wb'))
                        subprocess.call(["ln", "-sfv", filename, expandPath(location)])
                    else:
                        subprocess.call(["ln", "-sv", filename, expandPath(location)])

        if not update:
            for script in postlink:
                subprocess.call([expand(token) for token in shlex.split(script)])
