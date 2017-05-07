#!/bin/bash

cd $(dirname $(readlink -f $0))
chmod +x ./install

./install -s ./test/tests/simple
python ./test/checks/simple_check.py

