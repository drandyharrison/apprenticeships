# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import pandas
import numpy
import matplotlib.pyplot as plt
from XLSXhandler import XLSXhandler

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
        # Simple plot of totals
        plt.plot(xlsx.hdr_labels, xlsx.totals, 'ro')
        plt.xlabel('Years')
        plt.ylabel('Total')
        plt.title('Apprenticeships')
        # TODO How to make bigger to accomomdate y-axis label
        plt.show()
        # TODO plot a histogram of the data
        # TODO create a function to create a histogram for the analysed data - so will plot any data
        # TODO process the other worksheets to replicate the FEweek analysis
    else:
        print("\tFailed", flush=True)
    del xlsx
