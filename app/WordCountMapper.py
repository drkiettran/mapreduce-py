#!/usr/bin/env python3

import re
import sys


class WordCountMapper:
    def __init__(self):
        pass

    def proc_line(self, line):
        line = line.strip().rstrip().lower()
        line = re.sub("[^A-Za-z0-9 ]", " ", line)
        return line.split()

    def map(self):
        for line in sys.stdin:
            for word in self.proc_line(line):
                print('{}\t{}'.format(word, 1))


def main():
    word_count_mapper = WordCountMapper()
    word_count_mapper.map()


if __name__ == '__main__':
    main()
