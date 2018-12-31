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
        """Check create_barchart throws a TypeError if x_data is not a numpy.ndarray"""
        print("@test_create_barchart_x_data_not_ndarray")
        # arrange
        x_data = []
        y_data = numpy.array([], dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_y_data_not_ndarray(self):
        """Check create_barchart throws a TypeError if y_data is not a numpy.ndarray"""
        print("@test_create_barchart_y_data_not_ndarray")
        # arrange
        x_data = numpy.array([], dtype=numpy.float64)
        y_data = []
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_x_data_and_y_data_not_equal_len(self):
        """Check create_barchart throws a ValueError if x_data and y_data are different lengths"""
        print("@test_create_barchart_x_data_and_y_data_not_equal_len")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(5, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_colour_not_list(self):
        """Check create_barchart throws a TypeError if colour is not a string"""
        print("@test_create_barchart_colour_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = 'red'
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_colour_blank_str(self):
        """Check create_barchart throws a ValueError if colour is a blank string"""
        print("@test_create_barchart_colour_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = [""]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_colour_empty_str(self):
        """Check create_barchart throws a ValueError if colour is an empty string"""
        print("@test_create_barchart_colour_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["   "]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_width_is_str(self):
        """Check create_barchart throws a TypeError if test width is string"""
        print("@test_create_barchart_width_is_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = "3"
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_width_is_int(self):
        """Check create_barchart throws a TypeError if test width is an integer"""
        print("@test_create_barchart_width_is_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 3
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_xlabel_not_str(self):
        """Check create_barchart throws a TypeError if xlabel is not a string"""
        print("@test_create_barchart_xlabel_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = 3
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_xlabel_blank_str(self):
        """Check create_barchart throws a ValueError if xlabel is a blank string"""
        print("@test_create_barchart_xlabel_blank_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "  "
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_xlabel_empty_str(self):
        """Check create_barchart throws a ValueError if xlabel is an empty string"""
        print("@test_create_barchart_xlabel_empty_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = ""
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_title_not_str(self):
        """Check create_barchart throws a TypeError if title is not a string"""
        print("@test_create_barchart_title_not_str")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1/1.5
        colour = ["green"]
        xlabel = "Years"
        title = 3
        fig_id = 1
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_fig_id_not_int(self):
        """Check create_barchart throws a TypeError if fig_id is not integer"""
        print("@test_create_barchart_fig_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = "x"
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_fig_id_not_pos(self):
        """Check create_barchart throws a ValueError if fig_id is not positive"""
        print("@test_create_barchart_fig_id_not_pos")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 0
        sub_id = 111
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_sub_id_not_int(self):
        """Check create_barchart throws a TypeError if sub_id is not integer"""
        print("@test_create_barchart_sub_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = "111"
        show = True
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_show_not_bool(self):
        """Check create_barchart throws a TypeError if show is not boolean"""
        print("@test_create_barchart_show_not_bool")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 111
        show = 3
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(TypeError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_invalid_subplot_id(self):
        """Check create_barchart throws a warning if sub_id is not a valid subplot reference"""
        print("@test_create_barchart_fig_id_not_int")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 227
        show = False
        type_of_bar = 's'
        # act
        # assert
        self.assertWarns(UserWarning, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show, type_of_bar)

    def test_create_barchart_default_type_of_bar(self):
        """Check create_barchart runs ok using default value for type_of_bar"""
        print("@test_create_barchart_default_type_of_bar")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        show = False
        #type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show)

    def test_create_barchart_default_show(self):
        """Check create_barchart runs ok using default value for show"""
        print("@test_create_barchart_default_show")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(3, dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        #show = False
        type_of_bar = 's'
        # act
        # assert
        # confirm no exceptions (or warnings?) are raised
        create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, type_of_bar=type_of_bar)

    def test_create_barchart_not_enough_colours(self):
        """Check create_barchart fails if there aren't enough colours for the data"""
        print("@test_create_barchart_not_enough_colours")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        show = False
        type_of_bar = 's'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                         show=show, type_of_bar=type_of_bar)

    def test_create_barchart_3d_y_data(self):
        """Check create_barchart fails if ty_data has more than 2 dimensions"""
        print("@test_create_barchart_3d_y_data")
        # arrange
        x_data = numpy.ones(3, dtype=numpy.float64)
        y_data = numpy.ones(shape=(2, 3, 3), dtype=numpy.float64)
        width = 1 / 1.5
        colour = ["green"]
        xlabel = "Years"
        title = "Bar chart"
        fig_id = 1
        sub_id = 223
        show = False
        type_of_bar = 'h'
        # act
        # assert
        self.assertRaises(ValueError, create_barchart, x_data, y_data, width, colour, xlabel, title, fig_id, sub_id,
                         show=show, type_of_bar=type_of_bar)


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)
