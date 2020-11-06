import unittest
import sys
from test.IOUtil import StringIO
from app.FlightsByCarriersMapper import FlightsByCarriersMapper


HEADER = 'Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarrier,FlightNum,TailNum,' \
         'ActualElapsedTime,CRSElapsedTime,AirTime,ArrDelay,DepDelay,Origin,Dest,Distance,TaxiIn,TaxiOut,Cancelled,' \
         'CancellationCode,Diverted,CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,LateAircraftDelay '
GOOD_LINE = '1987,12,31,4,1821,1545,2037,1811,CO,541,NA,136,146,NA,146,156,CLE,TPA,927,NA,NA,0,NA,0,NA,NA,NA,NA,NA'


class TestFlightsByCarriersMapper(unittest.TestCase):
    def setUp(self):
        self.flights_by_carriers_mapper = FlightsByCarriersMapper()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_carrier_field(self):
        sys.stdin = StringIO(GOOD_LINE)
        self.flights_by_carriers_mapper.mapping()
        sys.stdout = sys.__stdout__
        self.assertTrue('CO\t1' in self.captured_output.getvalue())

    def test_carrier_header(self):
        sys.stdin = StringIO(HEADER)
        self.flights_by_carriers_mapper.mapping()
        sys.stdout = sys.__stdout__
        self.assertFalse(self.captured_output.getvalue())

