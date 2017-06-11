import unittest


from test.integration.simple_check import SimpleTest
from test.integration.no_clean_check import NoCleanTest
from test.integration.no_overwrite_check import NoOverwriteTest
from test.integration.no_scripts_check import NoScriptsTest


from test.unit.test_parser import TestParser


def get_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SimpleTest))
    test_suite.addTest(unittest.makeSuite(NoCleanTest))
    test_suite.addTest(unittest.makeSuite(NoOverwriteTest))
    test_suite.addTest(unittest.makeSuite(NoScriptsTest))

    test_suite.addTest(unittest.makeSuite(TestParser))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    ret = runner.run(get_suite()).wasSuccessful()
    exit(not ret)
