# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import sys
from sys import exit
import xlrd
import pandas as pd
from urllib.request import urlopen
import matplotlib
from JSONhandler import JSONhandler
from XLSXhandler import XLSXhandler

def get_xlsx_from_url(url):
    """
    Read an Excel workbook from a url
    :param url: url pointing to an Excel workbook
    :return:    flag to indicate whether the url is valid and points to a valid Excel workbook,
                if True also returns the contents of the Excel workbook as a pandas dataframe; otherwise None
    """
    urlhndlr = URLhandler(url)
    # is the url valid?
    if urlhndlr.check_url():
        del urlhndlr
        # open url
        try:
            socket = urlopen(url)
        except requests.exceptions.ConnectionError as e:
            print("@get_xlsx_from_url() Connection error for {}".format(url))
            return False, None
        except:
            print("@get_xlsx_from_url() Unexpected error:", sys.exc_info()[0])
            return False, None
        # get Excel workbook
        try:
            xlsx_data = pd.ExcelFile(socket)
        except xlrd.biffh.XLRDError as e:
            print("@get_xlsx_from_url() Not an xlsx file: {}".format(url))
            return False, None
        else:
            return True, xlsx_data
    else:
        del urlhndlr
        print("@get_xlsx_from_url() URL doesn't exist: {}".format(url))
        return False, None

# create json handler, ready to replace get_str_lst_from_json
jsonhndlr = JSONhandler("data_url.json")
# get urls to process
url_list = jsonhndlr.get_str_lst()
del jsonhndlr
# process the urls
for url in url_list:
    print("Processing: {}".format(url), flush=True)
    xlsx = XLSXhandler(url)
    flag = xlsx.get_xlsx_from_url()
    if flag:
        # get the sheet names
        sht_names = xlsx.xlsx_data.sheet_names
        print("\tSheet names: {}".format(sht_names), flush=True)
    else:
        print("\tFailed", flush=True)
    del xlsx

## temporary exit to check code
exit(0)

# Load worksheet 1A into a data frame
df = xlsx_data.parse("1A")
# size and shape of the dataframe
print("No.  dimensions: {}".format(df.ndim))
print("Shape:           {}".format(df.shape))
print("Columns:         {}".format(df.columns))
# rename the columns to contiguous integers, makes access easier
for idx, col in enumerate(df.columns):
    df.rename(columns={col:idx}, inplace=True)
print("Renamed columns: {}".format(df.columns))
# Extract data etc.
row_years = 3       # row 3 is the years
row_totals = 4      # row 4 is totals
data_start = 7      # rows 7 - 28 are the data
data_finish = 28
# TODO change so that the columns and rows start from 0 (renaming, as above)
years = df.loc[row_years,1:5]
totals = df.loc[row_totals,1:5]
sectors = df.loc[data_start:data_finish,0]
data = df.loc[data_start:data_finish,1:5]
print("Years:\n{}".format(years))
print("Totals:\n{}".format(totals))
print("Sectors:\n{}".format(sectors))
print("Data:\n{}".format(data))

# TODO plot a histogram of the data

# TODO process the other worksheets to replicate the FEweek analysis
# TODO craate a function for extracting and munging a worksheet
# TODO create a function to create a histogram for the analysed data













# ------------------
# code to read a CSV
# ------------------
#import csv
#import urllib2

#url = 'http://winterolympicsmedals.com/medals.csv'
#response = urllib2.urlopen(url)
#cr = csv.reader(response)

#for row in cr:
#    print row