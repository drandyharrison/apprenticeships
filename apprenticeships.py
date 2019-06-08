# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at
# https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import numpy
import pandas
import matplotlib.pyplot as plt
import XLSXhandler
import create_barchart
import replace_nonnumeric

jsondf = pandas.read_json("data_url.json")

for url in jsondf.values:
    # check url is right size - should be ndarray with one element
    if url.size != 1:
        raise ValueError("url wrong size: {}".format(url))
    url_str = url.item(0)
    print("Processing: {}".format(url_str), flush=True)
    xlsx = XLSXhandler.XLSXhandler(url_str)
    if xlsx.get_xlsx_from_url():
        sht_names = xlsx.get_sheet_names()  # get the sheet names
        print("\tSheet names: {}".format(sht_names), flush=True)
        # Get apprenticeship starts by sector
        xlsx.extract_worksheet_data("1A", 5, 6, 9, 30, 5)
        title = 'Change in apprenticeships starts by sector'
        width = 0.9
        fig_id = 1
        # TODO is there scope to shrink the area of the plot and still have sector labels?
        plt.figure(fig_id, figsize=(24, 10))     # size the figure
        plt.suptitle(title)
        fig = plt.gcf()
        fig.canvas.set_window_title('Apprenticeships')     # name the figure
        # if called with the wrong type of parameters, it will raise a TypeError
        # TODO (1) Health and Social work dominate
        x_data = xlsx.get_row_labels()
        for idx, x_val in enumerate(x_data):
            x_data[idx] = x_val.strip()             # remove any leading or trailing spaces from labels
        # create y_data array, with multiple rows
        y_data = numpy.zeros(shape=(2, xlsx.get_num_rows()), dtype=numpy.float64)
        # replace an non-numeric values
        y_data_1213 = numpy.array(numpy.asmatrix(xlsx.get_col_val(0))).flatten()
        y_data_1617 = numpy.array(numpy.asmatrix(xlsx.get_col_val(4))).flatten()
        # remove non-numeric values before populating the numpy array of floats
        # TODO now I know Python is there existing functionality to do this
        replace_nonnumeric.replace_nonnumeric(y_data_1213)
        replace_nonnumeric.replace_nonnumeric(y_data_1617)
        y_data[0, :] = y_data_1213
        y_data[1, :] = y_data_1617
        # TODO print the dataframe as a whole should make it a multiple bar chart with legends
        create_barchart.create_barchart(x_data, y_data/1000, width, ['red', 'blue'], 'Sectors', "", fig_id, 221, "Number (000s)",
                        ['2012/12', '2016/17'], True, 's')
        # create_barchart.create_barchart(x_data, y_data/1000, width, ['red', 'blue'], 'Sectors', "", fig_id, 221, True, 'h')
        # TODO (2) Fewest people are beginning apprenticeships in the north east
        # TODO (3) Women choose social work, men choose construction
        # TODO (4) Large employers make up the majority of starts
        # TODO (5) Differences by age
    else:
        print("\tFailed", flush=True)
    del xlsx
