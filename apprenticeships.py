# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at
# https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import pandas
import numpy
import matplotlib.pyplot as plt
from XLSXhandler import XLSXhandler

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

jsondf = pandas.read_json("data_url.json")

for url in jsondf.values:
    # check url is right size - should be ndarray with one element
    if url.size != 1:
        raise ValueError("url wrong size: {}".format(url))
    url_str = url.item(0)
    print("Processing: {}".format(url_str), flush=True)
    xlsx = XLSXhandler(url_str)
    if xlsx.get_xlsx_from_url():
        sht_names = xlsx.get_sheet_names()  # get the sheet names
        print("\tSheet names: {}".format(sht_names), flush=True)
        xlsx.extract_worksheet_data("1A", 3, 4, 7, 28, 5)
        create_barchart(xlsx.hdr_labels.values, xlsx.totals, 1/1.5,'green', 'Years', 'Apprenticeships (totals)')
        # TODO process the other worksheets to replicate the FEweek analysis
    else:
        print("\tFailed", flush=True)
    del xlsx
