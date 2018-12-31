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

    def test_replace_nonnumeric_data_not_iterable(self):
        """Check replace_nonnumeric throws a TypeError if data is not iterable"""
        print("@test_replace_nonnumeric_template")
        # arrange
        test_data = 2
        nonnumeric_val = numpy.nan
        cast_val = False
        # act
        # asset
        self.assertRaises(TypeError, replace_nonnumeric, test_data, nonnumeric=nonnumeric_val, cast=cast_val)

    def test_replace_nonnumeric_nonnumeric_not_numeric(self):
        """Check replace_nonnumeric throws a TypeError if nonnumeric is not numeric"""
        print("@test_replace_nonnumeric_nonnumeric_not_numeric")
        # arrange
        test_data = [2]
        nonnumeric_val = "nan"
        cast_val = False
        # act
        # asset
        self.assertRaises(TypeError, replace_nonnumeric, test_data, nonnumeric=nonnumeric_val, cast=cast_val)

    def test_replace_nonnumeric_cast_not_boolean(self):
        """Check replace_nonnumeric throws a TypeError if cast is not boolean"""
        print("@test_replace_nonnumeric_cast_not_boolean")
        # arrange
        test_data = [2]
        nonnumeric_val = numpy.nan
        cast_val = "x"
        # act
        # asset
        self.assertRaises(TypeError, replace_nonnumeric, test_data, nonnumeric=nonnumeric_val, cast=cast_val)

    def test_replace_nonnumeric_cast_false_not_converted(self):
        """Check replace_nonnumeric doesn't convert the string '123' when cast is False"""
        print("@test_replace_nonnumeric_cast_not_boolean")
        # arrange
        num_str = "123"
        test_data = [num_str]
        nonnumeric_val = numpy.nan
        cast_val = False
        # act
        replace_nonnumeric(test_data, nonnumeric=nonnumeric_val, cast=cast_val)
        # asset
        self.assertTrue(numpy.isnan(test_data[0]))

# TODO confirm "123" is converted if cast = True
# TODO confirm "*" goes to NaN if cast = False
# TODO confirm "*" goes to NaN if cast = True


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)