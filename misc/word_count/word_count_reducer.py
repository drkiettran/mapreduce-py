#!/usr/bin/env python3  
    
import sys
import socket

class Reducer:
    def __init__(self):
        self.current_word = None
        self.current_count = 0
        self.word = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)
        self._log('connecting to server ...')
        
    def _log(self, message):
        self.sock.sendto(message.encode(), self.server_address)
        
    def reduce(self):
        # self._log("entering ...")
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
    reducer = Reducer()
    reducer._log('main ...')
    reducer.reduce()

if __name__ == "__main__":    
    main(sys.argv[:1])
    