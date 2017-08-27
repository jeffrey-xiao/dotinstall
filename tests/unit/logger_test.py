import io
import os
import mock
import unittest


from dotinstall.util.logger import Logger
from dotinstall.util.level import Level


class LoggerTest(unittest.TestCase):

    @mock.patch('sys.stdout.write')
    def test_log(self, mock_stdout):
        Logger.log(Level.HEADER, 'message')
        mock_stdout.assert_called_with('{}{}{}'.format(
            Level.HEADER,
            'message',
            Level.END,
        ))

    @mock.patch('dotinstall.util.logger.Logger')
    def test_normal(self, mock_logger):
        Logger.normal('message')
        mock_logger.log.assert_called_with(Level.NORMAL, 'message')

    @mock.patch('dotinstall.util.logger.Logger')
    def test_error(self, mock_logger):
        Logger.error('message')
        mock_logger.log.assert_called_with(Level.ERROR, 'message')

    @mock.patch('dotinstall.util.logger.Logger')
    def test_warning(self, mock_logger):
        Logger.warning('message')
        mock_logger.log.assert_called_with(Level.WARNING, 'message')

    @mock.patch('dotinstall.util.logger.Logger')
    def test_success(self, mock_logger):
        Logger.success('message')
        mock_logger.log.assert_called_with(Level.SUCCESS, 'message')

    @mock.patch('dotinstall.util.logger.Logger')
    def test_info(self, mock_logger):
        Logger.info('message')
        mock_logger.log.assert_called_with(Level.INFO, 'message')

    @mock.patch('dotinstall.util.logger.Logger')
    def test_header(self, mock_logger):
        Logger.header('message')
        mock_logger.log.assert_called_with(Level.HEADER, 'message')
