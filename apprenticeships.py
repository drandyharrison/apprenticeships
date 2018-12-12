# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at
# https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import pandas
import matplotlib.pyplot as plt
from XLSXhandler import XLSXhandler

def create_barchart(x_data, y_data, width, colour, x_label, title):
    """Create a bar chart"""
    # TODO validate parameters
    # x_data and y_data are lists of the same length
    # y_data are numeric
    # colour is a string
    # x_label is a string
    # title is a string
    # create bar chart
    plt.bar(x_data, y_data, width, color=colour)
    plt.xlabel(x_label)
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
        create_barchart(xlsx.hdr_labels, xlsx.totals, 1/1.5,'green', 'Years', 'Apprenticeships (totals)')
        # TODO process the other worksheets to replicate the FEweek analysis
    else:
        print("\tFailed", flush=True)
    del xlsx
