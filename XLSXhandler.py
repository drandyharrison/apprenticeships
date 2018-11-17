import sys
import requests
from URLhandler import URLhandler

class XLSXhandler:
    """Class for handling Excel files"""

    # creator methods
    def __init__(self):
        pass

    def __init__(self, fname):
        if (isinstance(fname, str)):
            # the name of the Excel file to be processed - can be a filename, full path, url etc.
            self.fname = fname
        else:
            raise ValueError("@XLSXhandler creator: {} is not a string".format(fname))

    # Read an Excel workbook from a url and returns whether the url is valid and points to a valid Excel workbook
    # contents of the workbook are loaded into the panda dataframe self.xlsx_data
    def get_xlsx_from_url(self):
        # TODO try ... except ...
        urlhndlr = URLhandler(self.fname)
        # is the url valid?
        if urlhndlr.check_url():
            del urlhndlr    # delete as soon as no longer needed
            # open url
            try:
                socket = urlopen(self.fname)
            except requests.exceptions.ConnectionError as e:
                print("@XLSXhandler.get_xlsx_from_url() Connection error for {}".format(self.fname))
                self.xlsx_data = None
                return False
            except:
                print("@XLSXhandler.get_xlsx_from_url() Unexpected error:", sys.exc_info()[0])
                self.xlsx_data = None
                return False
            # get Excel workbook
            try:
                self.xlsx_data = pd.ExcelFile(socket)
            except xlrd.biffh.XLRDError as e:
                print("@XLSXhandler.get_xlsx_from_url() Not an xlsx file: {}".format(self.fname))
                self.xlsx_data = None
                return False
            else:
                return True
        else:
            del urlhndlr
            print("@XLSXhandler.get_xlsx_from_url() URL doesn't exist: {}".format(self.fname))
            self.xlsx_data = None
            return False