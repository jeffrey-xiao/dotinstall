# DOTINSTALL
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web) [![Coverage Status](https://coveralls.io/repos/github/jeffrey-xiao/dotinstall/badge.svg?branch=master)](https://coveralls.io/github/jeffrey-xiao/dotinstall?branch=master)

Dotinstall makes it easier to completely setup a fresh install. By grouping your configs into 'packages',
you can use dotinstall to quickly symlink your files, install dependencies, and setup your system. You might have a particularly
hard time setting up your windows manager. For example, I use i3-gaps and i3blocks-gaps on Ubuntu so I have to install those from
source. By having a package defined as i3, I can associate dependencies and scripts to run to setup my windows manager.

Features:
 - Easy integration into existing dotfiles by installing as submodule.
 - Association of dependencies with packages.
 - Globbing for specifying targets to symlink in each package.
 - Prelink, and postlink scripts to run before symlinking and dependency installation.
 - Easy configuration setup using yaml.

## Installation
```
mkdir dotfiles
cd dotfiles
git submodule add https://github.com/jeffrey-xiao/dotinstall.git
git submodule update --init --recursive
pip3 install -r ./dotinstall/requirements.txt
python3 ./dotinstall/install.py
```

## Usage
Run ```python3 ./dotinstall/install.py -h``` for more details.

## Config File
The config file (default ```config.yaml```) has the following possible entries.

**link**: If specified as an item, it will link all the items in the package to the specified location.
If specified as a list, it will link the specific items to their specified location. Note that each item will at most be
linked once. For example, if you have three files ```1.txt```, ```2.txt```, ```3.txt``` and you first link ```1.txt```,
it will only link ```2.txt``` and ```3.txt``` when you later try to link ```*.txt```.

**prelink**: A list of scripts that will run before dependency installation and linking.

**postlink**: A list of scripts that will run after dependency installation and linking.

**dependencies**: A list of dependencies of each package that will be installed by the detected package manager. Dependency installation will occur before linking.

**overwrite**: If true (default), the symlinking will forcibly remove existing files, symlinks, and directories.

**clean**: If true (default), dotinstall will remove all broken symlinks in all target directories.

The order of the commands will be: prelink -> dependencies -> link -> postlink -> clean.

## Example
Please see my personal dotfile [config](https://github.com/jeffrey-xiao/dotfiles/blob/master/config.yaml).

## Contributing
Please fork the repository and submit a PR. New plugins are very easy to create, by adding a new class with a `execute` command.

Additionally, only the `apt-get` package manager is integrated into `dotinstall`. Feel free to add other package managers (`brew`, `pacman`).
