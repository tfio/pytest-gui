
import unittest
import time

def get_sky_color():
    return 'blue'

def is_water_wet():
    return True

class TestPyTestGui2(unittest.TestCase):
    def test_new_things_here(self):
        '''Just print 1's'''
        for i in range(0, 5):
            time.sleep(0.5)
            print(i, ".. New things verification")

    def test_more_new_things(self):
        '''More GUI verification'''
        for i in range(0,10):
            time.sleep(0.1)
            print(i, ".. More new things GUI verification")

    def test_new_failures(self):
        '''Test a failure scenario'''
        print('Testing for a new failure scenario')
        for i in range(0,10):
            time.sleep(0.1)
            print(i, ".. GUI verification")
        print('Asserting now..')
        assert(0)

    def test_new_long_run(self):
        '''Sort of long running test case'''
        for idx in range(0, 5):
            print('Testing a sort of long running test case.. ', idx)
            time.sleep(.2)

