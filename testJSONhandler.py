import unittest
from JSONhandler import JSONhandler

class testJSONhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator_notstr(self):
        """check that creator throws expected error when passed a non-string"""
        print("@test_creator_notstr")
        self.assertRaises(ValueError, JSONhandler, 25)

    def test_creator_blank(self):
        """check the creator throws expected error when passed a blank string"""
        print("@test_creator_blank")
        self.assertRaises(ValueError, JSONhandler, "   ")

    def test_creator_empty(self):
        """check the creator throws expected error when passed an empty string"""
        print("@test_creator_empty")
        self.assertRaises(ValueError, JSONhandler, "")

    def test_get_str_lst_not_exists(self):
        """When a string is passed but path doesn't exist"""
        print("@test_get_str_lst_not_exists")
        jsonhndlr = JSONhandler("does_not_exist.json")
        self.assertIsNone(jsonhndlr.get_str_lst())

    def test_get_str_lst_not_file(self):
        """When a valid string is passed and exists but isn't a file; e.g. a directory"""
        print("@test_get_str_lst_not_file")
        jsonhndlr = JSONhandler("C:\Windows")
        self.assertIsNone(jsonhndlr.get_str_lst())

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)