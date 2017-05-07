import argparse
from .path import *


def readOptions():
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


def parseOptions(args):
    src = expandPath(args.src) or os.path.dirname(os.path.realpath(os.path.join(__file__, "..", "..", "..")))
    conf = expandPath(args.conf) or os.path.join(src, "config.yaml")
    update = args.update
    prompt = args.prompt

    return {
        'src': src,
        'conf': conf,
        'update': update,
        'prompt': prompt
    }


def parseData(package, packageName):
    ret = {
        'linkLocations': [],
        'overwrite': True,
        'prelink': [],
        'postlink': [],
        'dependencies': [],
        'symlinkedFiles': set(),
        'package': packageName
    }

    if 'link' not in package:
        out.error("No link attribute set.\n")
        exit(1)
    elif isinstance(package['link'], list):
        ret['linkLocations'] = package['link']
    else:
        ret['linkLocations'] = [
            {"*": package['link']},
            {".*": package['link']}
        ]

    if 'overwrite' in package:
        ret['overwrite'] = package['overwrite']

    if 'prelink' in package:
        ret['prelink'] = package['prelink']

    if 'postlink' in package:
        ret['postlink'] = package['postlink']

    if 'dependencies' in package:
        ret['dependencies'] = package['dependencies']

    return ret
