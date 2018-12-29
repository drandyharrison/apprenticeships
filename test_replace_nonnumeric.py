import unittest
import numpy
from replace_nonnumeric import replace_nonnumeric

class testReplaceNonnumeric(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_replace_nonnumeric_template(self):
        """Check replace_nonnumeric throws a ValueError if something happens"""
        print("@test_replace_nonnumeric_template")
        # arrange
        test_data = []
        nonnumeric_val = numpy.nan
        cast_val = False
        # act
        # asset
        self.assertRaises(ValueError, replace_nonnumeric, test_data, nonnumeric=nonnumeric_val, cast=cast_val)


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
