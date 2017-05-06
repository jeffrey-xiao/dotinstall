import argparse
from path import *

def readOptions() :
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

def parseOptions(args) :
    src = expandPath(args.src) or os.path.dirname(os.path.realpath(os.path.join(__file__, "..", "..", "..")))
    conf = expandPath(args.conf) or os.path.join(src, "config.yaml")
    update = args.update
    prompt = args.prompt

    return (src, conf, update, prompt)
