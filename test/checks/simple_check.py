import unittest
from helper import *

class SimpleTest(unittest.TestCase):
    def test_linking(self):
        print expand("~/other/2.txt")
        self.assertTrue(os.path.islink(expand("~/other/2.txt")))

def main():
    unittest.main()

if __name__ == '__main__':
    main
    clean("~/test")
    clean("~/other")
