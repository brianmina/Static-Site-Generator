import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        
    def test_title_with_spaces(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")
        
    def test_title_with_extra_whitespace(self):
        self.assertEqual(extract_title("#    Lots of Space    "), "Lots of Space")
        
    def test_title_in_multiline_markdown(self):
        markdown = """Some text before
# The Actual Title
Some text after"""
        self.assertEqual(extract_title(markdown), "The Actual Title")
        
    def test_no_title_raises_exception(self):
        with self.assertRaises(Exception):
            extract_title("No title here")

if __name__ == "__main__":
    unittest.main()
