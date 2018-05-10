
import unittest
import time

class TestGUIFunction(unittest.TestCase):
    def test_print_1_many_times(self):
        for i in range(0,10):
            time.sleep(1)
            print(i, ".. GUI verification")

    def test_print_2_many_times(self):
        for i in range(0,10):
            print(i, ".. More GUI verification")

    def test_failure_1(self):
        print('Testing for a failure scenario.')
        for i in range(0,10):
            print(i, ".. GUI verification")
        print('Asserting now..')
        assert(0)

    def test_long_running_1(self):
        for idx in range(0, 20):
            print('Testing long running test case.. ', idx)
            time.sleep(.5)

