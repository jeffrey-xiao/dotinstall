import builtins
import io
import os
import unittest
from unittest.mock import patch


import dotinstall.dotinstall as dotinstall
from test.util import expand_path
from test.util import execute_main
from test.util import clean


class PromptTest(unittest.TestCase):

    def test_prompt_y(self):
        with patch.object(builtins, 'input', return_value='y'):
            execute_main('prompt', prompt=True)
        self.assertTrue(os.path.exists(expand_path("~/test1/test1")))
        self.assertTrue(os.path.exists(expand_path("~/test2/test2")))
        clean("~/test1")
        clean("~/test2")

    def test_prompt_n(self):
        with patch.object(builtins, 'input', return_value='n'):
            execute_main('prompt', prompt=True)
        self.assertFalse(os.path.exists(expand_path("~/test1/test1")))
        self.assertFalse(os.path.exists(expand_path("~/test2/test2")))
        clean("~/test1")
        clean("~/test2")
