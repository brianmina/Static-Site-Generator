import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    
    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading(self):
        # Test valid heading
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Test heading with multiple #
        block = "### This is a level 3 heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        # Test invalid heading (no space after #)
        block = "#This is not a valid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Test invalid heading (too many #)
        block = "####### This has too many #"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code(self):
        # Test simple code block
        block = "```\ncode goes here\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        # Test code block with language specified
        block = "```python\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_quote(self):
        # Test single line quote
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        # Test multi-line quote
        block = "> This is a quote\n> And this is another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_unordered_list(self):
        # Test single item list
        block = "- Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Test multi-item list
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        # Test invalid list (no space after -)
        block = "-Item 1\n-Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        # Test single item list
        block = "1. Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Test multi-item list
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        # Test invalid list (wrong starting number)
        block = "2. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        # Test invalid list (non-consecutive numbers)
        block = "1. Item 1\n3. Item 2"
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)
        

