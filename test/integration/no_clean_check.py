import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.util import expand
from test.util import execute_main
from test.util import clean


class NoCleanTest(unittest.TestCase):
    def test_no_clean(self):
        self.assertFalse(os.path.exists(expand("~/test/broken1.txt")))
        self.assertTrue(os.path.islink(expand("~/test/broken1.txt")))
        self.assertFalse(os.path.exists(expand("~/test/broken2.txt")))
        self.assertTrue(os.path.islink(expand("~/test/broken2.txt")))

    @classmethod
    def setUpClass(cls):
        super(NoCleanTest, cls).setUpClass()
        execute_main('no_clean')

    @classmethod
    def tearDownClass(cls):
        super(NoCleanTest, cls).tearDownClass()
        # clean("~/test")
