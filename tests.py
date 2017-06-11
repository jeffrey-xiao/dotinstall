import unittest

import test.checks.simple_check as simple_check

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(simple_check.suite())
