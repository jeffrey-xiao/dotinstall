import os
import unittest


import dotinstall.dotinstall as dotinstall
import dotinstall.util.path as path
from test.checks.helper import expand
from test.checks.helper import clean

class SimpleTest(unittest.TestCase):
    def test_linking(self):
        self.assertTrue(os.path.islink(expand("~/other/2.txt")))

    def test_no_overwrite(self):
        self.assertTrue(os.path.isfile(expand("~/test/1.txt")))

    def test_prelink(self):
        contents = ""
        with open(expand("~/test/1.txt")) as fin:
            contents += fin.read().strip()
        self.assertTrue(contents == "100")

    def test_postlink(self):
        self.assertTrue(not os.path.exists("~/other/3.txt"))

    def test_clean(self):
        self.assertTrue(not os.path.exists("~/test/broken1.txt"))
        self.assertTrue(not os.path.islink("~/test/broken1.txt"))
        self.assertTrue(not os.path.exists("~/other/broken2.txt"))
        self.assertTrue(not os.path.islink("~/other/broken2.txt"))

    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        dotinstall.main({
            'src': path.expand_path('./test/tests/simple'),
            'conf': path.expand_path('./test/tests/simple/config.yaml'),
            'update': False,
            'prompt': False,
        })

    @classmethod
    def tearDownClass(cls):
        super(SimpleTest, cls).tearDownClass()
        clean("~/test")
        clean("~/other")

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SimpleTest))
    return test_suite
