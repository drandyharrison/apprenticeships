# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
import sys
import xlrd
import pandas as pd
from urllib.request import urlopen
import matplotlib
import validators

# url for data, which links to an Excel
data_url = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx"

# Read an Excel workbook from a given url
#   url     url pointing to Excel
#
# returns contents of Excel as a pandas dataframe
#
def get_xlsx_from_url(url):
    """
    Read an Excel workbook from a url
    :param url:
    :return:
    """
    if validators.url(url):
        # open url
        try:
            socket = urlopen(url)
        except (TimeoutError, urllib.error.URLError) as e:
            print('Timeout error for {}'.format(url))
            print("url probably doesn't exist")
            #print(e)
        except:
            print("Unexpected error (when converting string to integer):", sys.exc_info()[0])
            raise
        # get Excel workbook
        try:
            xlsx_data = pd.ExcelFile(socket)
        except xlrd.biffh.XLRDError as e:
            print("Not an xlsx file: {}".format(url))
            return None
        print("Succesfully read: {}".format(url))
        print(xlsx_data.sheet_names)
        return xlsx_data
    else:
        print("Invalid url: {}".format(url))
    #print('Valid url and exists: {}'.format(url))

# test url checking
# TODO - create unit test based on these
#get_xlsx_from_url('google')
get_xlsx_from_url('http://google.co.uk')
#get_xlsx_from_url('https://www.shddf.xx.xx')
get_xlsx_from_url(data_url)
## temporary exit to check code
quit(0)

# TODO add exeption handling
# TODO commit to analytical-adventures repo
# create socket for url
socket = urlopen(data_url)
# get Excel workbook
xlsx_data = pd.ExcelFile(socket)
# get the sheet names
sht_names = xlsx_data.sheet_names
print(sht_names)
# Load worksheet 1A into a data frame
df = xlsx_data.parse("1A")
# size and shape of the dataframe
print("No.  dimensions: {}".format(df.ndim))
print("Shape:           {}".format(df.shape))
print("Columns:         {}".format(df.columns))
# rename the columns to contiguous integers, makes access easier
# TODO achieve this with a lambda function
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