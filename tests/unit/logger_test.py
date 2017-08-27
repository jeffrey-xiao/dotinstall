import io
import sys
import os
import mock
import pytest
import unittest


from dotinstall.util.logger import Logger
from dotinstall.util.level import Level


def test_log(mock_stdout):
    Logger.log(Level.HEADER, 'message')
    mock_stdout.assert_called_with('{}{}{}'.format(
        Level.HEADER,
        'message',
        Level.END,
    ))

def test_normal(mock_logger):
    Logger.normal('message')
    mock_logger.log.assert_called_with(Level.NORMAL, 'message')

def test_error(mock_logger):
    Logger.error('message')
    mock_logger.log.assert_called_with(Level.ERROR, 'message')

def test_warning(mock_logger):
    Logger.warning('message')
    mock_logger.log.assert_called_with(Level.WARNING, 'message')

def test_success(mock_logger):
    Logger.success('message')
    mock_logger.log.assert_called_with(Level.SUCCESS, 'message')

def test_info(mock_logger):
    Logger.info('message')
    mock_logger.log.assert_called_with(Level.INFO, 'message')

def test_header(mock_logger):
    Logger.header('message')
    mock_logger.log.assert_called_with(Level.HEADER, 'message')
