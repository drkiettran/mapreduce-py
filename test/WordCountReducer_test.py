import unittest
import sys
import io
from app.WordCountReducer import WordCountReducer
from test.IOUtil import StringIO


class TestWordCountReducer(unittest.TestCase):
    def setUp(self):
        self.reducer = WordCountReducer()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_reduce(self):
        sys.stdin = StringIO("abc\t1\nabc\t1\nxyz\t1\nabd\t1\nad\t1\nad\t1\nefr\t1")
        self.reducer.reduce()
        sys.stdout = sys.__stdout__
        self.assertTrue('abc\t2\nxyz\t1\nabd\t1\nad\t2\nefr\t1' in self.captured_output.getvalue())
