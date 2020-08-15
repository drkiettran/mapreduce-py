#!/usr/bin/env python3

import sys
import socket
import re


class FlightsByCarriersReducer:
    def __init__(self):
        # initial code
        self.count = 0
        self.current_word = None
        self.word = None
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        
    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)
                
    def reduce(self):
        for line in sys.stdin:
            # self._log(line)
         
            line = line.strip()
            self.word, count = line.split('\t', 1)
            try:
                count = int(count)
            except ValueError:
                continue
            
            if self.current_word == self.word:
                self.current_count += count
            else:
                if self.current_word:
                    print ('{}\t{}'.format(self.current_word, self.current_count))
                self.current_count = count
                self.current_word = self.word
                
        if self.current_word == self.word:
            print('{}\t{}'.format(self.current_word, self.current_count))

# Main

def main(argv):
    flightsByCarriersReducer = FlightsByCarriersReducer()
    flightsByCarriersReducer.reduce()

if __name__ == "__main__":
    main(sys.argv[:1])