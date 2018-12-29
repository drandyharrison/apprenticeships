import numpy


def replace_nonnumeric(data, nonumeric=numpy.nan, cast=False):
    """Given an iterable object, replace any non-numeric objects
    data      - the iterable object to be modified
    nonumeric - replace non-numeric values with this value
    cast      - attempt to cast non-numeric values; e.g. a string like '123'"""
    # validate inputs
    try:
        iterator = iter(data)
    except TypeError:
        raise TypeError("@replace_nonnumeric: data is not iterable")
    if not (isinstance(nonumeric, int) or isinstance(nonumeric, float)):
        raise TypeError("@replace_nonnumeric: nonumeric is not numeric")
    if not isinstance(cast, bool):
        raise TypeError("@replace_nonnumeric: cast is not boolean")
    # replace non-numeric values
    for idx, val in enumerate(data):
        if not (isinstance(val, int) or isinstance(val, float)):
            if cast:
                if isinstance(val, str):
                    try:
                        new_val = float(val)
                    except ValueError:
                        new_val = nonumeric
            else:
                new_val = nonumeric
            data[idx] = new_val
