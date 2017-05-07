import unittest
from helper import *

class SimpleTest(unittest.TestCase):
    def test_linking(self):
        self.assertTrue(os.path.islink(expand("~/other/2.txt")))

    @classmethod
    def tearDownClass(cls):
        super(SimpleTest, cls).tearDownClass()
        clean("~/test")
        clean("~/other")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
