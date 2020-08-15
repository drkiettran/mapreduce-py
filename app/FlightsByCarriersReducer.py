#!/usr/bin/env python3

import sys
import socket
import re


class FlightsByCarriersReducer:
    def __init__(self):
        self.count = 0
        self.current_word = None
        self.current_count = 0
        self.word = None

    def reduce(self):
        for line in sys.stdin:
            line = line.strip()
            self.word, self.count = line.split('\t', 1)
            try:
                self.count = int(self.count)
            except ValueError:
                continue

            if self.current_word == self.word:
                self.current_count += self.count
            else:
                if self.current_word:
                    print('{}\t{}'.format(self.current_word, self.current_count))
                self.current_count = self.count
                self.current_word = self.word

        if self.current_word == self.word:
            print('{}\t{}'.format(self.current_word, self.current_count))


# Main

def main(argv):
    flights_by_carriers_reducer = FlightsByCarriersReducer()
    flights_by_carriers_reducer.reduce()


if __name__ == "__main__":
    main(sys.argv[:1])
