# coding=utf-8
import unittest


class Test(unittest.TestCase):
    def test_001(self):
        #! [001]
        self.assertEqual('o w', 'hello world'[4:7])
        #! [001]

    def test_002(self):
        #! [002]
        self.assertEqual('abc\ndef', """abc
def""")
        #! [002]

    def test_003(self):
        #! [003]
        self.assertEqual(u'文', u'中文'[1])
        self.assertEqual(2, len(u'中文'))
        self.assertEqual(6, len('中文'))
        #! [003]

    def test_004(self):
        #! [004]
        self.assertEqual('中文', u'中文'.encode('utf8'))
        #! [004]

    def test_005(self):
        #! [005]
        self.assertListEqual(['hello', 'world'], 'hello world'.split(' '))
        #! [005]

    def test_006(self):
        #! [006]
        # small
        self.assertEqual('hello world', 'hello' + ' world')
        # large
        parts = []
        parts.append('h')
        parts.append('e')
        parts.append('ll')
        parts.append('o')
        self.assertEqual('hello', ''.join(parts))
        #! [006]

    def test_007(self):
        #! [007]
        # positional
        self.assertEqual('hello world', '{} {}'.format('hello', 'world'))
        # named
        self.assertEqual('hello world', '{v1} {v2}'.format(v1='hello', v2='world'))
        # format
        self.assertEqual('3.14', '{:.2f}'.format(3.1415))
        #! [007]

    def test_008(self):
        #! [008]
        self.assertEqual('hello world', 'Hello World'.lower())
        self.assertEqual('HELLO WORLD', 'Hello World'.upper())
        #! [008]

    def test_009(self):
        #! [009]
        self.assertTrue('Hello World'.startswith('He'))
        #! [009]

    def test_010(self):
        #! [010]
        self.assertTrue('Hello World'.endswith('ld'))
        #! [010]