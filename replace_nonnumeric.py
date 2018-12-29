import numpy


# TODO define associated unit tests
def replace_nonnumeric(data, nonumeric=numpy.nan, cast=False):
    """Given an iterable object, replace any non-numeric objects
    data      - the iterable object to be modified
    nonumeric - replace non-numeric values with this value
    cast      - attempt to cast non-numeric values; e.g. a string like '123'"""
    # validate inputs
    # TODO check data is iterable
    # TODO check nonnumeric is numeric
    # TODO check cast is boolean
    # TODO implement the cast flag
    for idx, val in enumerate(data):
        if not (isinstance(val, int) or isinstance(val, float)):
            data[idx] = nonumeric
