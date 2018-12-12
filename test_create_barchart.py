import unittest
import numpy
from create_barchart import create_barchart

class testCreateBarchart(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_create_barchart_x_data_not_ndarray(self):
        """Check create_barchart throws a ValueError if x_data is not a numpy.ndarray"""
        print("@test_create_barchart_x_data_not_ndarray")
        # arrange
        x_data = []
        y_data = numpy.array([], dtype=numpy.float64)
        width = 0.0
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    # TODO test y_data is not a numpy.ndarray
    # TODO test x_data and y_data are different lengths
    # TODO test y_data is all numeric
    # TODO test colour is not a string
    # TODO test colour is not an empty string
    # TODO test width is float (string and int)
    # TODO test xlabel is not a string
    # TODO test xlabel is not an empty string
    # TODO test title is not a string
    # TODO test title is not an empty string
    # TODO check coverage


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
