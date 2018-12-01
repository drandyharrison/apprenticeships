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

    def test_get_worksheet_not_string(self):
        """Check get_worksheet throws a ValueError for a non-string worksheet name"""
        print("@test_get_worksheet_not_string")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        self.assertRaises(ValueError, xlsx.get_worksheet, 25, 1, 1, 1, 1,5)

    def test_get_worksheet_not_in_workbook(self):
        """Check get_worksheet throws a ValueError if worksheet not in workbook"""
        print("@test_get_worksheet_not_in_workbook")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "nil", 1, 2, 3, 3, 5)

    def test_get_worksheet_no_workbook(self):
        """Check get_worksheet throws a ValueError if workbook hasn't been loaded"""
        print("@test_get_worksheet_not_in_workbook")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 3, 3, 5)

    def test_get_worksheet_hdr_row_not_int(self):
        """Check get_worksheet throws a ValueError if hdr_row is not an integer"""
        print("@test_get_worksheet_hdr_row_not_int")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", "X", 2, 3, 3, 5)

    def test_get_worksheet_total_row_not_int(self):
        """Check get_worksheet throws a ValueError if total_row is not an integer"""
        print("@test_get_worksheet_total_row_not_int")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, "X", 3, 3, 5)

    def test_get_worksheet_start_row_not_int(self):
        """Check get_worksheet throws a ValueError if start_row is not an integer"""
        print("@test_get_worksheet_start_row_not_int")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, "X", 3, 5)

    def test_get_worksheet_end_row_not_int(self):
        """Check get_worksheet throws a ValueError if end_row is not an integer"""
        print("@test_get_worksheet_end_row_not_int")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 3, "X", 5)

    def test_get_worksheet_hdr_row_not_pos(self):
        """Check get_worksheet throws a ValueError if hdr_row is not positive"""
        print("@test_get_worksheet_hdr_row_not_pos")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 0, 2, 3, 3, 5)

    def test_get_worksheet_total_row_not_pos(self):
        """Check get_worksheet throws a ValueError if total_row is not positive"""
        print("@test_get_worksheet_total_row_not_pos")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 0, 3, 3, 5)

    def test_get_worksheet_start_row_not_pos(self):
        """Check get_worksheet throws a ValueError if start_row is not positive"""
        print("@test_get_worksheet_start_row_not_pos")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 0, 3, 5)

    def test_get_worksheet_end_row_not_pos(self):
        """Check get_worksheet throws a ValueError if end_row is not positive"""
        print("@test_get_worksheet_end_row_not_pos")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 3, 0, 5)

    def test_get_worksheet_start_after_end_row(self):
        """Check get_worksheet throws a ValueError if start_row is after end_row"""
        print("@test_get_worksheet_start_after_end_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 4, 3, 5)

    def test_get_worksheet_hdr_equals_total_row(self):
        """Check get_worksheet throws a ValueError if hdr_row equals total_row"""
        print("@test_get_worksheet_hdr_equals_total_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 1, 3, 3, 5)

    def test_get_worksheet_hdr_equals_start_row(self):
        """Check get_worksheet throws a ValueError if hdr_row equals start_row"""
        print("@test_get_worksheet_hdr_equals_start_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 1, 3, 5)

    def test_get_worksheet_hdr_equals_end_row(self):
        """Check get_worksheet throws a ValueError if hdr_row equals end_row"""
        print("@test_get_worksheet_hdr_equals_end_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 1, 3, 5)

    def test_get_worksheet_total_equals_start_row(self):
        """Check get_worksheet throws a ValueError if total_row equals start_row"""
        print("@test_get_worksheet_total_equals_start_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 2, 3, 5)

    def test_get_worksheet_total_equals_end_row(self):
        """Check get_worksheet throws a ValueError if total_row equals end_row"""
        print("@test_get_worksheet_total_equals_end_row")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 3, 2, 3, 5)


    def test_get_worksheet_num_cols_not_pos(self):
        """Check get_worksheet throws a ValueError if total_row equals end_row"""
        print("@test_get_worksheet_num_cols_not_pos")
        xlsx = XLSXhandler("https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/750709/apprenticeship_starts_tables.xlsx")
        xlsx.get_xlsx_from_url()
        self.assertRaises(ValueError, xlsx.get_worksheet, "1A", 1, 2, 3, 4, 0)

# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)