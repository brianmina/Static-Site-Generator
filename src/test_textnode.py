import unittest

from textnode import TextNode, TextType
from markdown_parser import extract_markdown_images, extract_markdown_links

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node = TextNode("Text one", TextType.BOLD)
        node2 = TextNode("Text two", TextType.BOLD)
        self.assertNotEqual(node, node2)

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "Here are two images: ![first](https://example.com/1.jpg) and ![second](https://example.com/2.jpg)"
        )
        self.assertListEqual([
            ("first", "https://example.com/1.jpg"),
            ("second", "https://example.com/2.jpg")
        ], matches)
    
    def test_extract_no_images(self):
        matches = extract_markdown_images("This text has no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
        "Here are two links: [first](https://example.com/1) and [second](https://example.com/2)"
        )   
        self.assertListEqual([
        ("first", "https://example.com/1"),
        ("second", "https://example.com/2")
        ], matches)

    def test_extract_no_links(self):
        matches = extract_markdown_links("This text has no links")
        self.assertListEqual([], matches)

    def test_extract_links_not_images(self):
        matches = extract_markdown_links(
        "This has a ![image](https://example.com/img.jpg) and a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
if __name__ == "__main__":
    unittest.main()
