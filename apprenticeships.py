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
        xlsx.extract_worksheet_data("1A", 3, 4, 7, 28, 5)
        title = 'Apprenticeships (totals)'
        width = 1/1.5
        fig_id = 1
        plt.figure(fig_id, figsize=(16, 5))     # size the figure
        plt.suptitle(title)
        fig = plt.gcf()
        fig.canvas.set_window_title('Apprenticeships')     # name the figure
        # if called with the wrong type of parameters, it will raise a TypeError
        create_barchart(xlsx.hdr_labels.values, xlsx.totals/1000, width, 'red', 'Years', "", fig_id, 131, False)
        create_barchart(xlsx.hdr_labels.values, xlsx.totals/1000, width, 'green', 'Years', "", fig_id, 447, False)
        create_barchart(xlsx.hdr_labels.values, xlsx.totals/1000, width, 'orange', 'Years', "  ", fig_id, 133, True)
        # TODO process the other worksheets to replicate the FEweek analysis
    else:
        print("\tFailed", flush=True)
    del xlsx
