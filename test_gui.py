
import unittest
import time

def get_sky_color():
    return 'blue'

def is_water_wet():
    return True

class TestGUIFunction(unittest.TestCase):
    def test_print_1_many_times(self):
        '''Just print 1's'''
        for i in range(0, 5):
            time.sleep(0.5)
            print(i, ".. GUI verification")

    def test_print_2_many_times(self):
        '''More GUI verification'''
        for i in range(0,10):
            time.sleep(0.1)
            print(i, ".. More GUI verification")

    def test_failure_1(self):
        '''Test a failure scenario'''
        print('Testing for a failure scenario.')
        for i in range(0,10):
            time.sleep(0.1)
            print(i, ".. GUI verification")
        print('Asserting now..')
        assert(0)

    def test_long_running_1(self):
        '''Sort of long running test case'''
        for idx in range(0, 5):
            print('Testing a sort of long running test case.. ', idx)
            time.sleep(.2)

    def test_sky_is_blue(self):
        '''Another filler test'''
        print('Testing sky is blue')
        time.sleep(0.2)
        assert 'blue' == get_sky_color(), 'Ooops.. sky is not blue'

    def test_water_is_wet(self):
        '''Another filler test'''
        print('Testing if water is wet')
        time.sleep(0.2)
        assert True == is_water_wet(), 'Ooops.. water doesn\'t seem to be wet'

    def test_failure_scenario2(self):
        '''Additional failure test to make UI look pretty'''
        print('Testing failure scenario 2')
        time.sleep(0.2)
        assert 0, 'Okay this was expected failure.'


