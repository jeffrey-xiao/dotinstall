# dotinstall

[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web) [![codecov](https://codecov.io/gh/jeffrey-xiao/dotinstall/branch/master/graph/badge.svg)](https://codecov.io/gh/jeffrey-xiao/dotinstall)
[![PyPI version](https://badge.fury.io/py/dotinstall.svg)](https://badge.fury.io/py/dotinstall)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

`dotinstall` makes it easier to completely setup a fresh install. By grouping your configs into
'packages', you can use `dotinstall` to quickly symlink your files, install dependencies, and setup
your system. You might have a particularly hard time setting up your windows manager. For example, I
use i3-gaps and i3blocks-gaps on Ubuntu so I have to install those from source. By having a package
defined as i3, I can associate dependencies and scripts to run to setup my windows manager.

Features:

- Easy integration into existing dotfiles by installing as submodules.
- Association of dependencies with packages.
- Globbing for specifying targets to symlink in each package.
- Prelink, and postlink scripts to run before symlinking and dependency installation.
- Easy configuration setup using yaml.

## Installation

```
mkdir dotfiles
cd dotfiles
pip3 install dotinstall
dotinstall
```

## Usage

Run `dotinstall -h` for more details.

## Config File

The config file (default `config.yaml`) has the following possible entries.

**link**: If specified as an item, it will link all the items in the package to the specified
location. If specified as a list, it will link the specific items to their specified location. Note
that each item will at most be linked once. For example, if you have three files `1.txt`,
`2.txt`, `3.txt` and you first link `1.txt`, it will only link `2.txt` and
`3.txt` when you later try to link `*.txt`.

**prelink**: A list of scripts that will run before dependency installation and linking.

**postlink**: A list of scripts that will run after dependency installation and linking.

**dependencies**: A list of dependencies of each package that will be installed by the detected
package manager. Dependency installation will occur before linking.

**overwrite**: If true (default), the symlinking will forcibly remove existing files, symlinks, and
directories.

**clean**: If true (default), dotinstall will remove all broken symlinks in all target directories.

The order of the commands will be: prelink -> dependencies -> link -> postlink -> clean.

Each submodule will be installed in the order that it is listed in the config file.

## Example

Please see my personal dotfile
[config](https://github.com/jeffrey-xiao/dotfiles/blob/master/config.yaml).

## Contributing

Please fork the repository and submit a PR. New plugins are very easy to create, by adding a new
class with a `execute` command.

Currently implemented package managers are:

- `apt-get`
- `brew`
- `pacman`
- `eopkg`

Feel free to add other package managers.

## License

`dotinstall` is dual-licensed under the terms of either the MIT License or the Apache License
(Version 2.0).

See [LICENSE-APACHE](LICENSE-APACHE) and [LICENSE-MIT](LICENSE-MIT) for more details.
