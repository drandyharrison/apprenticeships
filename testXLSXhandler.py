import unittest
from XLSXhandler import XLSXhandler

class testXLSXhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator_non_string(self):
        """Test that creator throws a ValueError for a non-string url"""
        print("@test_creator_non_string")
        self.assertRaises(ValueError, XLSXhandler, 25)

    def test_creator_blank(self):
        """check the creator throws expected error when passed a blank string"""
        print("@test_creator_blank")
        self.assertRaises(ValueError, XLSXhandler, "   ")

    def test_creator_empty(self):
        """check the creator throws expected error when passed an empty string"""
        print("@test_creator_empty")
        self.assertRaises(ValueError, XLSXhandler, "")

    def test_get_xlsx_from_url_invalid_url(self):
        """Checks that a badly url returns False when checked"""
        print("@test_get_xlsx_from_url_invalid_url")
        xlsx = XLSXhandler("google")
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_non_exist_url(self):
        """Checks that a well formed url that doesn't exist returns False when checked"""
        print("@test_get_xlsx_from_url_non_exist_url")
        xlsx = XLSXhandler("https://www.shddf.xx.xx")
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_exist_not_xlsx(self):
        """Checks that a valid url that's not an Excel returns False when checked"""
        print("@test_get_xlsx_from_url_exist_not_xlsx")
        xlsx = XLSXhandler("https://www.google.co.uk")
        self.assertFalse(xlsx.get_xlsx_from_url())

    def test_get_xlsx_from_url_exist_is_xlsx(self):
        """Checks that a valid url that's an Excel returns True when checked"""
        print("@test_get_xlsx_from_url_exist_is_xlsx")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        self.assertTrue(xlsx.get_xlsx_from_url())

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)