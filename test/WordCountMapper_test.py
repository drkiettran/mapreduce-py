import unittest
from app.WordCountMapper import WordCountMapper
from test.IOUtil import StringIO
import sys


class TestWordCountMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = WordCountMapper()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_process_line(self):
        words = self.mapper.proc_line("abcdef.; -abc xyz-abd ad? efr;")
        self.assertEqual(words, ['abcdef', 'abc', 'xyz', 'abd', 'ad', 'efr'])

    def test_map(self):
        sys.stdin = StringIO("abcdef.; -abc xyz-abd ad? efr;")
        self.mapper.map()
        sys.stdout = sys.__stdout__
        self.assertTrue('abcdef\t1\nabc\t1\nxyz\t1\nabd\t1\nad\t1\nefr\t1' in self.captured_output.getvalue())
