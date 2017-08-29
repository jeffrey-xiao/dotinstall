import os

import mock
import pytest

import dotinstall.util.parser as parser
from dotinstall.util.logger import Logger


def test_read_options_defaults():
    args = parser.read_options(())

    assert not args.prompt
    assert not args.update
    assert args.src is None
    assert args.conf is None


def test_read_options_short():
    args = parser.read_options((
        '-s',
        './test',
        '-c',
        './test/config.yaml',
        '-p',
        '-u',
    ))

    assert args.prompt
    assert args.update
    assert args.src == './test'
    assert args.conf == './test/config.yaml'


def test_read_options_long():
    args = parser.read_options((
        '--src',
        './test',
        '--conf',
        './test/config.yaml',
        '--prompt',
        '--update',
    ))

    assert args.prompt
    assert args.update
    assert args.src == './test'
    assert args.conf == './test/config.yaml'


def test_parse_options_defaults():
    args = mock.Mock()
    args.update = True
    args.prompt = True
    args.conf = None
    args.src = None
    data = parser.parse_options(args)

    expected_dir = os.getcwd()
    expected_path = os.path.join(expected_dir, 'config.yaml')

    assert data['update']
    assert data['prompt']
    assert data['src'] == expected_dir
    assert data['conf'] == expected_path


def test_parse_options():
    args = mock.Mock()
    args.update = True
    args.prompt = True
    args.src = './test'
    args.conf = './test/config.yaml'
    data = parser.parse_options(args)

    assert data['update']
    assert data['prompt']
    assert data['src'] == os.path.join(os.getcwd(), 'test')
    assert data['conf'] == os.path.join(os.getcwd(), 'test', 'config.yaml')


def test_parse_data_no_link():
    with mock.patch.object(Logger, 'error') as mock_logger:
        with pytest.raises(SystemExit) as excinfo:
            parser.parse_data({}, 'test_package')
        mock_logger.assert_called_once_with('No link attribute set.\n')
    assert excinfo.value.code == 1


def test_parse_data_one_link():
    ret = parser.parse_data({'link': 'test'}, 'test_package')
    assert 'linkLocations' in ret
    assert len(ret['linkLocations']) == 2
    assert ret['linkLocations'][0] == {'*': 'test'}
    assert ret['linkLocations'][1] == {'.*': 'test'}


def test_parse_data_multiple_links():
    ret = parser.parse_data(
        {
            'link': [
                {'a': 'link_a'},
                {'b': 'link_b'},
            ],
        }, 'test_package',
    )
    assert 'linkLocations' in ret
    assert len(ret['linkLocations']) == 2
    assert ret['linkLocations'][0] == {'a': 'link_a'}
    assert ret['linkLocations'][1] == {'b': 'link_b'}


def test_parse_data_attributes():
    ret = parser.parse_data(
        {
            'link': 'test',
            'overwrite': 'overwrite',
            'prelink': 'prelink',
            'postlink': 'postlink',
            'dependencies': 'dependencies',
            'clean': 'clean',
        }, 'test_package',
    )

    assert 'overwrite' in ret
    assert ret['overwrite'] == 'overwrite'
    assert 'prelink' in ret
    assert ret['prelink'] == 'prelink'
    assert 'postlink' in ret
    assert ret['postlink'] == 'postlink'
    assert 'dependencies' in ret
    assert ret['dependencies'] == 'dependencies'
    assert 'clean' in ret
    assert ret['clean'] == 'clean'


def test_parse_data_no_attributes():
    ret = parser.parse_data(
        {
            'link': 'test',
        }, 'test_package',
    )

    assert 'overwrite' in ret
    assert ret['overwrite']
    assert 'prelink' in ret
    assert ret['prelink'] == []
    assert 'postlink' in ret
    assert ret['postlink'] == []
    assert 'dependencies' in ret
    assert ret['dependencies'] == []
    assert 'clean' in ret
    assert ret['clean']


def test_parse_data_package_name():
    ret = parser.parse_data(
        {
            'link': 'test',
        }, 'test_package',
    )

    assert 'package' in ret
    assert ret['package'] in 'test_package'
