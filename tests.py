import unittest

from tests.integration.simple_test import SimpleTest
from tests.integration.no_clean_test import NoCleanTest
from tests.integration.no_overwrite_test import NoOverwriteTest
from tests.integration.no_scripts_test import NoScriptsTest
from tests.integration.prompt_test import PromptTest

from tests.unit.parser_test import ParserTest
from tests.unit.logger_test import LoggerTest


def get_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SimpleTest))
    test_suite.addTest(unittest.makeSuite(NoCleanTest))
    test_suite.addTest(unittest.makeSuite(NoOverwriteTest))
    test_suite.addTest(unittest.makeSuite(NoScriptsTest))
    test_suite.addTest(unittest.makeSuite(PromptTest))

    test_suite.addTest(unittest.makeSuite(ParserTest))
    test_suite.addTest(unittest.makeSuite(LoggerTest))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=0, buffer=True)
    ret = runner.run(get_suite()).wasSuccessful()
    exit(not ret)
