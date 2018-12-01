import sys
import xlrd
import pandas as pd
from urllib.request import urlopen
import requests
from URLhandler import URLhandler

class XLSXhandler:
    """Class for handling Excel files"""

    # creator methods
    def __init__(self):
        pass

    def __init__(self, fname):
        if (isinstance(fname, str)):
            # check whether string is empty or blanh
            if not(fname and fname.strip()):
                raise ValueError("@XLSXhandler creator: {} is blank".format(fname))
            else:
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

    def get_sheet_names(self):
        """Return the sheet names"""
        return self.xlsx_data.sheet_names

    def get_worksheet(self, worksheet, hdr_row, total_row, start_row, end_row, num_cols):
        """Return the data contents of the worksheet as a ndarray

        worksheet -- name of the worksheet to process
        hdr_row - row comtainer the data header/field names
        total_row -- row with totals, -1 if no totals row
        start_row -- first row containing data
        end_row -- last row containing data"""
        if isinstance(worksheet, str):
            # check xlsx_data exists
            try:
                # check the worksheet exists
                if worksheet in self.xlsx_data.sheet_names:
                    self.data = self.xlsx_data.parse(worksheet)
                    # rename the columns to contiguous integers, makes access easier
                    for idx, col in enumerate(self.data.columns):
                        self.data.rename(columns={col: idx}, inplace=True)
                    # check row id parameters: hdr_row, total_row, start_row, end_row
                    if not isinstance(hdr_row, int):        # check hdr_row is an integer
                        raise ValueError("@get_worksheet(): hdr_row {} is not integer".format(hdr_row))
                    if not isinstance(total_row, int):  # check total_row is an integer
                        raise ValueError("@get_worksheet(): total_row {} is not integer".format(total_row))
                    if not isinstance(start_row, int):  # check start_row is an integer
                        raise ValueError("@get_worksheet(): start_row {} is not integer".format(start_row))
                    if not isinstance(end_row, int):    # check end_row is an integer
                        raise ValueError("@get_worksheet(): end_row {} is not integer".format(end_row))
                    if hdr_row <= 0:                    # check hdr_row is positive
                        raise ValueError("@get_worksheet(): hdr_row {} is not positive".format(end_row))
                    if total_row <= 0:                  # check total_row is positive
                        raise ValueError("@get_worksheet(): total_row {} is not positive".format(total_row))
                    if start_row <= 0:                  # check start_row is positive
                        raise ValueError("@get_worksheet(): start_row {} is not positive".format(start_row))
                    if end_row <= 0:                    # check end_row is positive
                        raise ValueError("@get_worksheet(): end_row {} is not positive".format(end_row))
                    if start_row > end_row:             # check start_row is before end_row
                        raise ValueError("@get_worksheet(): end_row {} is before start_row {}".format(end_row, start_row))
                    if hdr_row == total_row:            # check hdr_row and total_row are not the same
                        raise ValueError("@get_worksheet(): hdr_row {} matches total_row {}".format(hdr_row, total_row))
                    if hdr_row == start_row:            # check hdr_row and start_row are not the same
                        raise ValueError("@get_worksheet(): hdr_row {} matches start_row {}".format(hdr_row, start_row))
                    if hdr_row == end_row:              # check hdr_row and end_row are not the same
                        raise ValueError("@get_worksheet(): hdr_row {} matches end_row {}".format(hdr_row, end_row))
                    if total_row == start_row:          # check total_row and start_row are not the same
                        raise ValueError("@get_worksheet(): total_row {} matches start_row {}".format(total_row, start_row))
                    if total_row == end_row:            # check total_row and end_row are not the same
                        raise ValueError("@get_worksheet(): total_row {} matches end_row {}".format(total_row, end_row))
                    if num_cols <= 0:                   # check num_cols is positive
                        raise ValueError("@get_worksheet(): num_cols is not positive")
                    pass
                else:
                    print("@XLSXhandler.get_worksheet: worksheet {} is not in workbook".format(worksheet))
                    raise ValueError("@XLSXhandler.get_worksheet: worksheet {} is not in workbook".format(worksheet))
            except AttributeError:
                print("@XLSXhandler.get_worksheet(): attribute xlsx_data not defined")
                raise ValueError("@XLSXhandler.get_worksheet(): attribute xlsx_data not defined")
        else:
            print("@XLSXhandler.get_worksheet: {} is not a string".format(worksheet))
            raise ValueError("@XLSXhandler.get_worksheet: {} is not a string".format(worksheet))