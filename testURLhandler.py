import unittest
from URLhandler import URLhandler

class testURLhandler(unittest.TestCase):
    def SetUp(self):
        """set-up code, which is called before each test, to avoid repetition"""
        pass

    def tearDown(self):
        """code to tidy up after each test"""
        pass

    def test_creator(self):
        """Test that creator throws a ValueError for a non-string url"""
        self.assertRaises(ValueError, URLhandler, 25)

    def test_invalid_url(self):
        """Checks that a badly url returns False when checked"""
        urlhndlr = URLhandler("google")
        self.assertFalse(urlhndlr.check_url())

    def test_non_exist_url(self):
        """Checks that a well formed url that doesn't exist returns False when checked"""
        urlhndlr = URLhandler("https://www.shddf.xx.xx")
        self.assertFalse(urlhndlr.check_url())

    def test_exist_url(self):
        """Checks that an valid url returns Trie when checked"""
        urlhndlr = URLhandler("https://www.google.co.uk")
        self.assertTrue(urlhndlr.check_url())

    def test_example(self):
        pass
        # assertEquals
        # assertTrue - assertFalse
        # assertRaises


# run tests
if __name__ == '__main__':
    unittest.main(verbosity=2)