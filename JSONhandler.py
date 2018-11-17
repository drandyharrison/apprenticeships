import json
from pathlib import Path

class JSONhandler:
    """A class to handle JSON files"""

    # creator methods
    def __init__(self):
        pass
    def __init__(self, json_fname):
        if(isinstance(json_fname, str)):
            # the name of the JSON file to be processed
            self.json_fname = json_fname
        else:
            raise ValueError("@JSONhandler creator: {} is not a string".format(fname))
        
    # method to read a list of strings from a JSON file
    def get_str_lst(self):
        # list of strings to be returned
        self.str_list = []
        # read strings to process from a JSON file
        json_of_str = Path(self.json_fname)  # create Path object
        # does file exist
        if json_of_str.exists():
            # check it's a file
            if json_of_str.is_file():
                with json_of_str.open() as f:
                    try:
                        json_data = json.load(f)
                    except json.decoder.JSONDecodeError as e:
                        print("json.decoder.JSONDecodeError: reading {} | error: {}".format(self.json_fname, e.msg))
                        return None
                    except:
                        print("@JSONhandler.get_str_lst() Unexpected error:", sys.exc_info()[0])
                        return None
                    else:
                        # parse json_data
                        for data in json_data:
                            self.str_list.append(data)
                        return self.str_list
            else:
                print("@JSONhandler.get_str_lst() Isn't a file: {}".format(self.json_fname))
                return None
        else:
            print("@JSONhandler.get_str_lst() Doesn't exist: {}".format(self.json_fname))
            return None
