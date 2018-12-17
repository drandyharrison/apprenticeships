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
        width = 1/1.5
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_y_data_not_ndarray(self):
        """Check create_barchart throws a ValueError if y_data is not a numpy.ndarray"""
        print("@test_create_barchart_y_data_not_ndarray")
        # arrange
        x_data = numpy.array([], dtype=numpy.float64)
        y_data = []
        width = 1/1.5
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_x_data_and_y_data_not_equal_len(self):
        """Check create_barchart throws a ValueError if x_data and y_data are different lengths"""
        print("@test_create_barchart_x_data_and_y_data_not_equal_len")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(5, dtype=numpy.float64)
        width = 1/1.5
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_colour_not_str(self):
        """Check create_barchart throws a ValueError if colour is not a string"""
        print("@test_create_barchart_colour_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = 3
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_colour_blank_str(self):
        """Check create_barchart throws a ValueError if colour is a blank string"""
        print("@test_create_barchart_colour_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ""
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_colour_empty_str(self):
        """Check create_barchart throws a ValueError if colour is an empty string"""
        print("@test_create_barchart_colour_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ""
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_width_is_str(self):
        """Check create_barchart throws a ValueError if test width is string"""
        print("@test_create_barchart_width_is_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = "3"
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_width_is_int(self):
        """Check create_barchart throws a ValueError if test width is an integer"""
        print("@test_create_barchart_width_is_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 3
        colour = "green"
        xlabel = "Years"
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_xlabel_not_str(self):
        """Check create_barchart throws a ValueError if xlabel is not a string"""
        print("@test_create_barchart_xlabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = "green"
        xlabel = 3
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_xlabel_blank_str(self):
        """Check create_barchart throws a ValueError if xlabel is a blank string"""
        print("@test_create_barchart_xlabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = "green"
        xlabel = "  "
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_xlabel_empty_str(self):
        """Check create_barchart throws a ValueError if xlabel is an empty string"""
        print("@test_create_barchart_xlabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = "green"
        xlabel = ""
        title = "Bar chart"
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_title_not_str(self):
        """Check create_barchart throws a ValueError if title is not a string"""
        print("@test_create_barchart_title_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = "green"
        xlabel = "Years"
        title = 3
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_title_blank_str(self):
        """Check create_barchart throws a ValueError if title is a blank string"""
        print("@test_create_barchart_title_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = "green"
        xlabel = "Years"
        title = "   "
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

    def test_create_barchart_title_empty_str(self):
        """Check create_barchart throws a ValueError if title is an empty string"""
        print("@test_create_barchart_title_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = "green"
        xlabel = "Years"
        title = ""
        # act
        # asset
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title)

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
