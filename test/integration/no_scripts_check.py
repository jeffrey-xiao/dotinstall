import io
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.util import expand
from test.util import execute_main
from test.util import clean


class NoScriptsTest(unittest.TestCase):
    def test_no_prelink(self):
        self.assertFalse(os.path.exists(expand("~/test/1.txt")))

    def test_no_postlink(self):
        self.assertFalse(os.path.exists(expand("~/test/2.txt")))

    @classmethod
    def setUpClass(cls):
        super(NoScriptsTest, cls).setUpClass()
        execute_main('no_scripts', update=True)

    @classmethod
    def tearDownClass(cls):
        super(NoScriptsTest, cls).tearDownClass()
        clean("~/test")
