# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at
# https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import pandas
import matplotlib.pyplot as plt
from XLSXhandler import XLSXhandler
from create_barchart import create_barchart

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
        # Get apprenticeship starts by sector
        xlsx.extract_worksheet_data("1A", 3, 4, 7, 28, 5)
        title = 'Change in apprenticeships starts by sector'
        width = 1/1.5
        fig_id = 1
        plt.figure(fig_id, figsize=(16, 5))     # size the figure
        plt.suptitle(title)
        fig = plt.gcf()
        fig.canvas.set_window_title('Apprenticeships')     # name the figure
        # if called with the wrong type of parameters, it will raise a TypeError
        # TODO Replicate the FEweek analysis
        # TODO (1) Health and Social work dominate
        # TODO get data for 2012/13 by sector
        x_data = xlsx.row_labels.values
        y_data_1213 = xlsx.data[:,0]
        y_data_1617 = xlsx.data[:,4]
        # TODO get data for 2016/17 by sector
        # create_barchart(x_data, y_data_1213, width, 'red', 'Sectors', "", fig_id, 131, True, 's')
        create_barchart(x_data, y_data_1213, width, ['red'], 'Sectors', "", fig_id, 131, True, 'h')
        # TODO (2) Fewest people are beginning apprenticeships in the north east
        # TODO (3) Women choose social work, men choose construction
        # TODO (4) Large employers make up the majority of starts
        # TODO (5) Differences by age
    else:
        print("\tFailed", flush=True)
    del xlsx
