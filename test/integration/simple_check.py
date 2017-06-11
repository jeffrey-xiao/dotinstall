import io
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.util import expand
from test.util import execute_main
from test.util import clean

class SimpleTest(unittest.TestCase):
    def test_linking(self):
        self.assertTrue(os.path.islink(expand("~/other/2.txt")))

    def test_no_overwrite(self):
        self.assertTrue(os.path.isfile(expand("~/test/1.txt")))
        with io.open(expand("~/test/1.txt")) as fin:
            self.assertTrue(fin.read().strip() == "1")

    def test_prelink(self):
        with io.open(expand("~/test/2.txt")) as fin:
            self.assertTrue(fin.read().strip() == "2")

    def test_postlink(self):
        self.assertTrue(not os.path.exists(expand("~/other/3.txt")))

    def test_clean(self):
        self.assertTrue(not os.path.exists(expand("~/test/broken1.txt")))
        self.assertTrue(not os.path.islink(expand("~/test/broken1.txt")))
        self.assertTrue(not os.path.exists(expand("~/test/broken2.txt")))
        self.assertTrue(not os.path.islink(expand("~/test/broken2.txt")))

    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        execute_main('simple')

    @classmethod
    def tearDownClass(cls):
        super(SimpleTest, cls).tearDownClass()
        clean("~/test")
        clean("~/other")
