#!/usr/bin/env python3

import sys
import socket

class UdpTest:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        
    def _log(self, message):
        self.sock.sendto(message, self.server_address)
                
    def send(self, message):
        self._log(message.encode())

# Main


def main(argv):
    udpTest = UdpTest()
    udpTest.send('testing message\n')


if __name__ == "__main__":
    main(sys.argv[:1])
