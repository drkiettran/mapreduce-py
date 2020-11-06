#!/usr/bin/env python3

import sys


class WordCountReducer:
    def __init__(self):
        self.current_word = None
        self.current_count = 0
        self.word = None

    def reduce(self):
        for line in sys.stdin:
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
                    print('{}\t{}'.format(self.current_word, self.current_count))
                self.current_count = count
                self.current_word = self.word

        if self.current_word == self.word:
            print('{}\t{}'.format(self.current_word, self.current_count))


def main():
    word_count_mapper = WordCountReducer()
    word_count_mapper.reduce()


if __name__ == '__main__':
    main()