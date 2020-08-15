#!/usr/bin/env python3

import sys
import csv


class FlightsByCarriersMapper:
    def __init__(self):
        pass

    def mapping(self):
        for row in csv.reader(iter(sys.stdin.readline, '')):
            if row[0] != 'Year':
                print('{}\t{}'.format(row[8], 1))


def main(argv):
    flights_by_carriers_mapper = FlightsByCarriersMapper()
    flights_by_carriers_mapper.mapping()


if __name__ == "__main__":
    main(sys.argv[:1])
