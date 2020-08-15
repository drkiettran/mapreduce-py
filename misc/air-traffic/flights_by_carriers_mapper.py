#!/usr/bin/env python3

import sys
import socket
import re


class FlightsByCarriersMapper:
    def __init__(self):
        # initial code
        self.count = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)

    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)

    def map(self):
        for line in sys.stdin:
            # self._log(line)
            s = re.sub('[.,:;?!|]', ' ', line).split()
            # self._log(s[0])
            if s[0] == 'Year':
                self._log(line)
            else:
                print('{}\t{}'.format(s[8], 1))


# Main

def main(argv):
    flightsByCarriersMapper = FlightsByCarriersMapper()
    flightsByCarriersMapper.map()


if __name__ == "__main__":
    main(sys.argv[:1])
