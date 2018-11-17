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
