# This file prints discovers all test cases and prints out their IDs.
import compat
from config import get_setting
import unittest
import argparse

class Discover:
    def __init__(self):
        self.tests = []

    def flatten_results(self, iterable):
        input = list(iterable)
        while input:
            item = input.pop(0)
            try:
                data = iter(item)
                input = list(data) + input
            except:
                yield item

    def collect_tests(self, dirname):
        loader = unittest.TestLoader()
        suite = loader.discover(dirname)
        flatresults = list(self.flatten_results(suite))
        self.tests = [r.id() for r in flatresults]

    def print_tests(self):
        print('\n'.join(self.tests).strip())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--testdir', dest='testdir', default=get_setting('StartDir'), help='Directory to choose tests from')
    options = parser.parse_args()

    disc = Discover()
    disc.collect_tests(options.testdir)
    disc.print_tests()
