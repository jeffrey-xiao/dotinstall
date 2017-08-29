import argparse
import os

import dotinstall.util.path as path
from dotinstall.util.logger import Logger


def read_options(argv=None):
    parser = argparse.ArgumentParser(
        description='Installation script for dotfiles.',
    )
    parser.add_argument(
        '-s', '--src', dest='src', metavar='dir',
        help='root directory of dotfiles',
    )
    parser.add_argument(
        '-c', '--conf', dest='conf', metavar='file',
        help='config file for symlinking and installing',
    )
    parser.add_argument(
        '-p', '--prompt', dest='prompt', action='store_true',
        help='prompt user before installing package',
    )
    parser.add_argument(
        '-u', '--update', dest='update', action='store_true',
        help='only symlinks files',
    )

    return parser.parse_args(argv)


def parse_options(args):
    default_dir = os.getcwd()
    src = path.expand_path(args.src) or default_dir

    default_config = os.path.join(src, 'config.yaml')
    conf = path.expand_path(args.conf) or default_config

    update = args.update
    prompt = args.prompt

    return {
        'src': src,
        'conf': conf,
        'update': update,
        'prompt': prompt,
    }


def parse_data(package, package_name):
    ret = {
        'linkLocations': [],
        'overwrite': True,
        'clean': True,
        'prelink': [],
        'postlink': [],
        'dependencies': [],
        'symlinkedFiles': set(),
        'package': package_name,
    }

    if 'link' not in package:
        Logger.error('No link attribute set.\n')
        exit(1)
    elif isinstance(package['link'], list):
        ret['linkLocations'] = package['link']
    else:
        ret['linkLocations'] = [
            {'*': package['link']},
            {'.*': package['link']},
        ]

    if 'overwrite' in package:
        ret['overwrite'] = package['overwrite']

    if 'prelink' in package:
        ret['prelink'] = package['prelink']

    if 'postlink' in package:
        ret['postlink'] = package['postlink']

    if 'dependencies' in package:
        ret['dependencies'] = package['dependencies']

    if 'clean' in package:
        ret['clean'] = package['clean']

    return ret
