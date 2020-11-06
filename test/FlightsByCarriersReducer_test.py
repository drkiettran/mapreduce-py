import unittest
import sys
from test.IOUtil import StringIO
from app.FlightsByCarriersReducer import FlightsByCarriersReducer


INPUT = 'CO\t1\nCO\t1\nCO\t1\nPS\t1\nPS\t1\nAS\t1\nAS\t1\nAS\t1\nAS\t1'
BAD_INPUT = 'CO\t1\nCO\tabc\nCO\t1\nPS\t1\nPS\t1\nAS\t1\nAS\t1\nAS\t1\nAS\t1'

class TestFlightsByCarriersReducer(unittest.TestCase):
    def setUp(self):
        self.flights_by_carriers_reducer = FlightsByCarriersReducer()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_reduce_good_values(self):
        sys.stdin = StringIO(INPUT)
        self.flights_by_carriers_reducer.reduce()
        sys.stdout = sys.__stdout__
        self.assertTrue('CO\t3\nPS\t2\nAS\t4' in self.captured_output.getvalue())

    def test_reduce_bad_values(self):
        sys.stdin = StringIO(BAD_INPUT)
        self.flights_by_carriers_reducer.reduce()
        sys.stdout = sys.__stdout__
        self.assertTrue('CO\t2\nPS\t2\nAS\t4' in self.captured_output.getvalue())
