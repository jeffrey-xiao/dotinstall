import io
import os
import mock
import unittest


import dotinstall.util.parser as parser


class ParserTest(unittest.TestCase):

    def test_read_options_defaults(self):
        args = parser.read_options(())

        self.assertFalse(args.prompt)
        self.assertFalse(args.update)
        self.assertTrue(args.src == None)
        self.assertTrue(args.conf == None)

    def test_read_options_short(self):
        args = parser.read_options((
            '-s',
            './test',
            '-c',
            '~/test',
            '-p',
            '-u',
        ))

        self.assertTrue(args.prompt)
        self.assertTrue(args.update)
        self.assertTrue(args.src == './test')
        self.assertTrue(args.conf == '~/test')

    def test_read_options_long(self):
        args = parser.read_options((
            '--src',
            './test',
            '--conf',
            '~/test',
            '--prompt',
            '--update',
        ))

        self.assertTrue(args.prompt)
        self.assertTrue(args.update)
        self.assertTrue(args.src == './test')
        self.assertTrue(args.conf == '~/test')


    def test_parse_options_defaults(self):
        args = mock.Mock()
        args.update = True
        args.prompt = True
        args.conf = None
        args.src = None
        data = parser.parse_options(args)

        expected_dir = os.path.normpath(os.path.join(os.getcwd(), '..'))

        self.assertTrue(data['update'])
        self.assertTrue(data['prompt'])
        self.assertTrue(data['src'] == expected_dir)
        self.assertTrue(data['conf'] == os.path.join(expected_dir, 'config.yaml'))

    def test_parse_options(self):
        args = mock.Mock()
        args.update = True
        args.prompt = True
        args.conf = './test'
        args.src = '~/test'
        data = parser.parse_options(args)

        self.assertTrue(data['update'])
        self.assertTrue(data['prompt'])
        self.assertTrue(data['src'] == os.path.join(os.environ['HOME'], 'test'))
        self.assertTrue(data['conf'] == os.path.join(os.getcwd(), 'test'))

    @mock.patch('dotinstall.util.parser.Logger')
    def test_parse_data_no_link(self, mock_logger):
        with self.assertRaises(SystemExit) as e:
            parser.parse_data({}, 'test_package')
        self.assertEqual(e.exception.code, 1)
        mock_logger.error.assert_called_with('No link attribute set.\n')

    def test_parse_data_one_link(self):
        ret = parser.parse_data({'link': 'test'}, 'test_package')
        self.assertTrue('linkLocations' in ret)
        self.assertTrue(len(ret['linkLocations']) == 2)
        self.assertTrue(ret['linkLocations'][0] == {'*': 'test'})
        self.assertTrue(ret['linkLocations'][1] == {'.*': 'test'})

    def test_parse_data_multiple_links(self):
        ret = parser.parse_data({
            'link': [
                {'a': 'link_a'},
                {'b': 'link_b'},
            ]
        }, 'test_package')
        self.assertTrue('linkLocations' in ret)
        self.assertTrue(len(ret['linkLocations']) == 2)
        self.assertTrue(ret['linkLocations'][0] == {'a': 'link_a'})
        self.assertTrue(ret['linkLocations'][1] == {'b': 'link_b'})

    def test_parse_data_attributes(self):
        ret = parser.parse_data({
            'link': 'test',
            'overwrite': 'overwrite',
            'prelink': 'prelink',
            'postlink': 'postlink',
            'dependencies': 'dependencies',
            'clean': 'clean',
        }, 'test_package')

        self.assertTrue('overwrite' in ret)
        self.assertTrue(ret['overwrite'] == 'overwrite')
        self.assertTrue('prelink' in ret)
        self.assertTrue(ret['prelink'] == 'prelink')
        self.assertTrue('postlink' in ret)
        self.assertTrue(ret['postlink'] == 'postlink')
        self.assertTrue('dependencies' in ret)
        self.assertTrue(ret['dependencies'] == 'dependencies')
        self.assertTrue('clean' in ret)
        self.assertTrue(ret['clean'] == 'clean')

    def test_parse_data_no_attributes(self):
        ret = parser.parse_data({
            'link': 'test',
        }, 'test_package')

        self.assertTrue('overwrite' in ret)
        self.assertTrue(ret['overwrite'] == True)
        self.assertTrue('prelink' in ret)
        self.assertTrue(ret['prelink'] == [])
        self.assertTrue('postlink' in ret)
        self.assertTrue(ret['postlink'] == [])
        self.assertTrue('dependencies' in ret)
        self.assertTrue(ret['dependencies'] == [])
        self.assertTrue('clean' in ret)
        self.assertTrue(ret['clean'] == True)

    def test_parse_data_package_name(self):
        ret = parser.parse_data({
            'link': 'test',
        }, 'test_package')

        self.assertTrue('package' in ret)
        self.assertTrue(ret['package'] == 'test_package')
