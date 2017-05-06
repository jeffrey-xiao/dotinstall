import os
import glob
import sys
import yaml
import argparse
import subprocess
import shlex

from logger import Logger

out = Logger()

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
    src = expandPath(args.src) or os.path.dirname(os.path.realpath(os.path.join(__file__, "..", "..")))
    conf = expandPath(args.conf) or os.path.join(src, "config.yaml")
    update = args.update
    prompt = args.prompt

    return (src, conf, update, prompt)

def streamToString (stream):
    ret = ""
    if stream != None:
        for line in stream:
            ret += line
    return ret

def processPipe (pipe):
    stdoutOutput = ""
    stderrOutput = ""

    stdoutOutput = streamToString(pipe.stdout)
    stderrOutput = streamToString(pipe.stderr)

    out.info(stdoutOutput)
    out.error(stderrOutput)

def installDependency (dependency):
    pipe = subprocess.Popen(["dpkg-query", "-W", "-f=${Status}", dependency], stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb'))
    if streamToString(pipe.stdout).strip() == "install ok installed":
        out.info("{} already installed.\n".format(dependency))
    elif subprocess.call(["sudo", "apt-get", "install", "-y", dependency], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb')) == 0:
        out.success("{} successfully installed.\n".format(dependency))
    else:
        out.error("{} could not be installed.\n".format(dependency))

def expandPath (path) :
    if path == None:
        return None
    return os.path.abspath(expand(path))

def expand (token):
    if token == None:
        return None
    return os.path.expanduser(os.path.expandvars(token))

if __name__ == "__main__":
    args = readOptions()
    src, conf, update, prompt = parseOptions()

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
                processPipe(subprocess.Popen([expand(token) for token in shlex.split(script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
            for dependency in dependencies:
                installDependency(dependency)

        for linkLocation in linkLocations:
            for pattern, path in linkLocation.iteritems():
                location = expandPath(path)
                processPipe(subprocess.Popen(["mkdir", "-pv", location], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                for filename in glob.iglob(os.path.join(src, package, pattern)):
                    basename = os.path.basename(filename)
                    if basename in symlinkedFiles:
                        continue
                    symlinkedFiles.add(basename)

                    if overwrite:
                        processPipe(subprocess.Popen(["rm", os.path.join(expandPath(location), basename)], stdout=subprocess.PIPE, stderr=open(os.devnull, 'wb')))
                        processPipe(subprocess.Popen(["ln", "-sfv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
                    else:
                        processPipe(subprocess.Popen(["ln", "-sv", filename, expandPath(location)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))

        if not update:
            for script in postlink:
                processPipe(subprocess.Popen([expand(token) for token in shlex.split(script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE))
