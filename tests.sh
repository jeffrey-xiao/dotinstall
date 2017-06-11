#!/bin/bash

cd $(dirname $(readlink -f $0))

python3 ./dotinstall.py -s ./test/tests/simple
python3 ./test/checks/simple_check.py
