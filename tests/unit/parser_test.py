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
        self.assertIsNone(args.src)
        self.assertIsNone(args.conf)

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
        self.assertEqual(args.src, './test')
        self.assertEqual(args.conf, '~/test')

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
        self.assertEqual(args.src, './test')
        self.assertEqual(args.conf, '~/test')

    def test_parse_options_defaults(self):
        args = mock.Mock()
        args.update = True
        args.prompt = True
        args.conf = None
        args.src = None
        data = parser.parse_options(args)

        expected_dir = os.getcwd()
        expected_path = os.path.join(expected_dir, 'config.yaml')

        self.assertTrue(data['update'])
        self.assertTrue(data['prompt'])
        self.assertEqual(data['src'], expected_dir)
        self.assertEqual(data['conf'], expected_path)

    def test_parse_options(self):
        args = mock.Mock()
        args.update = True
        args.prompt = True
        args.conf = './test'
        args.src = '~/test'
        data = parser.parse_options(args)

        self.assertTrue(data['update'])
        self.assertTrue(data['prompt'])
        self.assertEqual(data['src'], os.path.join(os.environ['HOME'], 'test'))
        self.assertEqual(data['conf'], os.path.join(os.getcwd(), 'test'))

    @mock.patch('dotinstall.util.parser.Logger')
    def test_parse_data_no_link(self, mock_logger):
        with self.assertRaises(SystemExit) as e:
            parser.parse_data({}, 'test_package')
        self.assertEqual(e.exception.code, 1)
        mock_logger.error.assert_called_with('No link attribute set.\n')

    def test_parse_data_one_link(self):
        ret = parser.parse_data({'link': 'test'}, 'test_package')
        self.assertIn('linkLocations', ret)
        self.assertEqual(len(ret['linkLocations']), 2)
        self.assertEqual(ret['linkLocations'][0], {'*': 'test'})
        self.assertEqual(ret['linkLocations'][1], {'.*': 'test'})

    def test_parse_data_multiple_links(self):
        ret = parser.parse_data({
            'link': [
                {'a': 'link_a'},
                {'b': 'link_b'},
            ]
        }, 'test_package')
        self.assertIn('linkLocations', ret)
        self.assertEqual(len(ret['linkLocations']), 2)
        self.assertEqual(ret['linkLocations'][0], {'a': 'link_a'})
        self.assertEqual(ret['linkLocations'][1], {'b': 'link_b'})

    def test_parse_data_attributes(self):
        ret = parser.parse_data({
            'link': 'test',
            'overwrite': 'overwrite',
            'prelink': 'prelink',
            'postlink': 'postlink',
            'dependencies': 'dependencies',
            'clean': 'clean',
        }, 'test_package')

        self.assertIn('overwrite', ret)
        self.assertEqual(ret['overwrite'], 'overwrite')
        self.assertIn('prelink', ret)
        self.assertEqual(ret['prelink'], 'prelink')
        self.assertIn('postlink', ret)
        self.assertEqual(ret['postlink'], 'postlink')
        self.assertIn('dependencies', ret)
        self.assertEqual(ret['dependencies'], 'dependencies')
        self.assertIn('clean', ret)
        self.assertEqual(ret['clean'], 'clean')

    def test_parse_data_no_attributes(self):
        ret = parser.parse_data({
            'link': 'test',
        }, 'test_package')

        self.assertIn('overwrite', ret)
        self.assertEqual(ret['overwrite'], True)
        self.assertIn('prelink', ret)
        self.assertEqual(ret['prelink'], [])
        self.assertIn('postlink', ret)
        self.assertEqual(ret['postlink'], [])
        self.assertIn('dependencies', ret)
        self.assertEqual(ret['dependencies'], [])
        self.assertIn('clean', ret)
        self.assertEqual(ret['clean'], True)

    def test_parse_data_package_name(self):
        ret = parser.parse_data({
            'link': 'test',
        }, 'test_package')

        self.assertIn('package', ret)
        self.assertEqual(ret['package'], 'test_package')
