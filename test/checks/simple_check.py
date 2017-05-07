import unittest
from helper import *

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

    @classmethod
    def tearDownClass(cls):
        super(SimpleTest, cls).tearDownClass()
        clean("~/test")
        clean("~/other")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
