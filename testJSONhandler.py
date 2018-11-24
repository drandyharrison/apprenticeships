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
        self.assertRaises(ValueError, JSONhandler, 25)

# run tests
if __name__ == '__main__':
    unittest.main()