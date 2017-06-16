import io
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.util import expand
from test.util import execute_main
from test.util import clean


class NoOverwriteTest(unittest.TestCase):

    def test_no_overwrite(self):
        with io.open(expand("~/test/1.txt")) as fin:
            self.assertTrue(fin.read().strip() == "original 1")
        with io.open(expand("~/test/2.txt")) as fin:
            self.assertTrue(fin.read().strip() == "original 2")

    @classmethod
    def setUpClass(cls):
        super(NoOverwriteTest, cls).setUpClass()
        execute_main('no_overwrite')

    @classmethod
    def tearDownClass(cls):
        super(NoOverwriteTest, cls).tearDownClass()
        clean("~/test")
