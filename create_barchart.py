import numpy
import matplotlib.pyplot as plt
import warnings


def create_barchart(x_data, y_data, width, colour, xlabel, title, fig_id, sub_id, show=True, type_of_bar='s'):
    """Create a bar chart
    x_data      - the x coordinates of the bars (the categories, don't have to be numeric)
    y_data      - the height of the bars
    width       - width of the bars
    colour      - the colour of the bars
    xlabel      - label for the x-axis
    title       - title for the bar chart
    fig_id      - figure id
    sub_id      - subplot id
    show        - boolean flag to indicate whether to show figure
    type_of_bar - type of bar chart: 'b' - basic, 'h' - horizontal"""
    # validate parameters
    # TODO replace ValueError with TypeError where appropriate
    if not isinstance(x_data, numpy.ndarray):
        raise TypeError("@create_barchart: x_data {} is not a numpy.ndarray".format(type(x_data)))
    if not isinstance(y_data, numpy.ndarray):
        raise TypeError("@create_barchart: y_data {} is not a numpy.ndarray".format(type(y_data)))
    if y_data.ndim > 2:
        raise ValueError("@create_barchart: y_data can be at most 2-dimensional")
    if (y_data.ndim == 1 and x_data.size != y_data.size) or (y_data.ndim == 2 and x_data.size != numpy.size(y_data, 0)):
        raise ValueError("@create_barchart: x_data [{}] and y_data [{}] are not the same length".format(x_data.size, y_data.size))
    if not isinstance(width, float):
        raise TypeError("@create_barchart: width={} is not a float".format(width))
    if not isinstance(colour, list):
        raise TypeError("@create_barchart: colour={} is not a list".format(colour))
    for idx, c in enumerate(colour):
        if not isinstance(c, str):
            raise TypeError("@create_barchart: {}-th colour={} is not a string".format(idx, c))
        if not (c and c.strip()):
            raise ValueError("@create_barchart: colour is blank or empty")
    if (y_data.ndim == 1 and numpy.size(colour) < 1) or (y_data.ndim == 2 and numpy.size(colour) < numpy.size(y_data, 0)):
        raise ValueError("@create_barchart: not enough colours")
    if not isinstance(xlabel, str):
        raise TypeError("@create_barchart: x_label={} is not a string".format(xlabel))
    if not (xlabel and xlabel.strip()):
        raise ValueError("@create_barchart xlabel is blank or empty")
    if not isinstance(title, str):
        raise TypeError("@create_barchart: title={} is not a string".format(title))
    if not isinstance(fig_id, int):
        raise TypeError("@create_barchart figure id {} is not an integer".format(fig_id))
    if fig_id <= 0:
        raise ValueError("@create_barchart figure id {} is not positive".format(fig_id))
    if not isinstance(sub_id, int):
        raise TypeError("@create_barchart subplot id {} is not an integer".format(sub_id))
    if not isinstance(show, bool):
        raise TypeError("@create_barchart show {} is not a boolean".format(show))
    if not isinstance(type_of_bar, str):
        raise TypeError("@create_barchart type_of_bar {} is not a string".format(type_of_bar))
    # check sub-plot id is valid (assumes 3 digit integer)
    a = int(sub_id/100)
    b = int(sub_id/10)%10
    c = sub_id%10
    num_subplots = a * b
    # only plot the sub-plot if sub_id is valid
    if 1 <= c <= num_subplots:
        # create bar chart
        plt.figure(fig_id)      # if figure id doesn't already exist, matplotlib.pyplot will create one
        plt.subplot(sub_id)     # if subplot not consistent with figure, new sub-plots added
        # TODO multiple bars - see https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars
        # python doesn't have a switch-case
        # TODO for each row of data, plot a bar chart
        if type_of_bar == 's':
            plt.bar(x_data, y_data, width, color=colour[0])
        elif type_of_bar == 'h':
            plt.barh(x_data, y_data, width, color=colour[0])
        else:
            raise ValueError("@create_barchart unknown type_of_bar {}".format(type_of_bar))
        plt.xlabel(xlabel)
        plt.ylabel("Number (000s)")
        # only give sub-plot a title if title is a non-empty string
        if title:
            plt.title(title)
        if show:
            plt.show()
    else:
        warnings.warn("@create_barchart(): invalid subplot reference {}".format(sub_id))
