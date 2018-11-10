# based on FE week article on apprenticeships: https://bit.ly/2SlNP13
# the articles uses the DfE statistics at https://www.gov.uk/government/statistics/apprenticeships-in-england-by-industry-characteristics
# ---------------------------------------------------------------------
from sys import exit
import xlrd
import pandas as pd
from urllib.request import urlopen
import matplotlib
import validators
from http.client import OK, FOUND, MOVED_PERMANENTLY
import requests
import json
from pathlib import Path

def check_url(url):
    """
    Check if a URL exists without downloading the whole file. It only checks the URL header.
    :param url: the url to be checked
    :return:    True if url is a valid url string and web site exists/responds
    """
    # check it's a valid url string
    if validators.url(url):
        good_codes = [OK, FOUND, MOVED_PERMANENTLY]
        # check url exists
        try:
            request = requests.get(url)
            if request.status_code in good_codes:
                return True
            else:
                print("@check_url() Website returned response code: {code}".format(code=request.status_code))
                return False
        except requests.exceptions.ConnectionError as e:
            print('@check_url() Connection error for {}'.format(url))
            return False
        except:
            print("@check_url() Unexpected error (when converting string to integer):", sys.exc_info()[0])
            return False
    else:
        print("@check_url() Invalid url: {}".format(url))
        return False

def get_xlsx_from_url(url):
    """
    Read an Excel workbook from a url
    :param url: url pointing to an Excel workbook
    :return:    flag to indicate whether the url is valid and points to a valid Excel workbook,
                if True also returns the contents of the Excel workbook as a pandas dataframe; otherwise None
    """
    # is the url valid?
    if check_url(url):
        # open url
        try:
            socket = urlopen(url)
        except requests.exceptions.ConnectionError as e:
            print("@get_xlsx_from_url() Connection error for {}".format(url))
            return False, None
        except:
            print("Unexpected error (when converting string to integer):", sys.exc_info()[0])
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
        print("@get_xlsx_from_url() URL doesn't exist: {}".format(url))
        return False, None

def get_urls(json_fname_of_urls):
    """
    Read a list of urls from a JSON file
    :param json_fname_of_urls:  name of JSON file to read
    :return:                    list of urls
    """
    url_list = []
    # read urls to process from a JSON file
    json_of_urls = Path(json_fname_of_urls)  # create Path object
    # does file exist
    if json_of_urls.exists():
        # check it's a file
        if json_of_urls.is_file():
            with json_of_urls.open() as f:
                try:
                    json_data = json.load(f)
                except json.decoder.JSONDecodeError as e:
                    print("json.decoder.JSONDecodeError: reading {} | error: {}".format(json_fname_of_urls, e.msg))
                    return None
                except:
                    print("@check_url() Unexpected error (when converting string to integer):", sys.exc_info()[0])
                    return None
                else:
                    for data_url in json_data:
                        url_list.append(data_url)
                    return url_list
        else:
            print("Isn't a file: {}".format(json_fname_of_urls))
            return None
    else:
        print("Doesn't exist: {}".format(json_fname_of_urls))
        return None

# get urls to process
url_list = get_urls("data_url.json")
# process the urls
for url in url_list:
    print("Processing: {}".format(url), flush=True)
    flag, xlsx_data = get_xlsx_from_url(url)
    if flag:
        # get the sheet names
        sht_names = xlsx_data.sheet_names
        print("\tSheet names: {}".format(sht_names), flush=True)
    else:
        print("\tFailed", flush=True)

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