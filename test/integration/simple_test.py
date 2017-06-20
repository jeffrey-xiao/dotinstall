import io
import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.util import expand_path
from test.util import execute_main
from test.util import clean


class SimpleTest(unittest.TestCase):

    def test_linking(self):
        self.assertTrue(os.path.islink(expand_path("~/other/2.txt")))

    def test_no_overwrite(self):
        self.assertTrue(os.path.isfile(expand_path("~/test/1.txt")))
        with io.open(expand_path("~/test/1.txt")) as fin:
            self.assertEqual(fin.read().strip(), "1")

    def test_prelink(self):
        with io.open(expand_path("~/test/2.txt")) as fin:
            self.assertEqual(fin.read().strip(), "2")

    def test_postlink(self):
        self.assertFalse(os.path.exists(expand_path("~/other/3.txt")))

    def test_clean(self):
        self.assertFalse(os.path.exists(expand_path("~/test/broken1.txt")))
        self.assertFalse(os.path.islink(expand_path("~/test/broken1.txt")))
        self.assertFalse(os.path.exists(expand_path("~/test/broken2.txt")))
        self.assertFalse(os.path.islink(expand_path("~/test/broken2.txt")))

    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        execute_main('simple')

    @classmethod
    def tearDownClass(cls):
        super(SimpleTest, cls).tearDownClass()
        clean("~/test")
        clean("~/other")
