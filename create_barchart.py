import numpy
import matplotlib.pyplot as plt

def create_barchart(x_data, y_data, width, colour, xlabel, title):
    """Create a bar chart

    x_data - the x coordinates of the bars (the categories, don't have to be numeric)
    y_data - the height of the bars
    width  - width of the bars
    colour - the colour of the bars
    xlabel - label for the x-axis
    title  - title for the bar chart"""
    # validate parameters
    # TODO do we want to support more generic data types for x_data and y_data?
    # x_data and y_data are the same length
    if not isinstance(x_data, numpy.ndarray):
        raise ValueError("@create_barchart: x_data {} is not a numpy.ndarray".format(type(x_data)))
    if not isinstance(y_data, numpy.ndarray):
        raise ValueError("@create_barchart: y_data {} is not a numpy.ndarray".format(type(y_data)))
    if x_data.size != y_data.size:
        raise ValueError("@create_barchart: x_data [{}] and y_data [{}] are not the same length".format(x_data.size, y_data.size))
    for y, idx in enumerate(y_data):
        if not (isinstance(y, int) or isinstance(y, float)):
            raise ValueError("@create_barchart: y_data[{}]={} is not numeric".format(idx, y))
    if not isinstance(colour, str):
        raise ValueError("@create_barchart: colour={} is not a string".format(colour))
    if not isinstance(xlabel, str):
        raise ValueError("@create_barchart: x_label={} is not a string".format(xlabel))
    if not isinstance(title, str):
        raise ValueError("@create_barchart: title={} is not a string".format(title))
    # create bar chart
    plt.bar(x_data, y_data, width, color=colour)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()
