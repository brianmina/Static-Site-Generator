from enum import Enum, auto



class BlockType(Enum):
    PARAGRAPH = auto()
    HEADING = auto()
    CODE = auto()
    QUOTE = auto()
    UNORDERED_LIST = auto()
    ORDERED_LIST = auto()

def block_to_block_type(block):

    """
    Determine the type of a markdown block.
    
    Args:
        block: A string containing a markdown block
        
    Returns:
        BlockType: The type of the markdown block
    """
    # Check for heading (starts with 1-6 # characters, followed by a space)
    if block.startswith('#'):
        # Make sure there's a space after the # symbols
        pound_count = 0
        for char in block:
            if char == '#':
                pound_count += 1
            else:
                break
                
        # Valid heading has 1-6 # symbols followed by a space
        if 1 <= pound_count <= 6 and block[pound_count] == ' ':
            return BlockType.HEADING
    
    # Check for code block (starts and ends with ```)
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    # Check for quote block (every line starts with >)
    lines = block.split('\n')
    # Check for quote block (first line starts with >)
    if lines and lines[0].strip().startswith('>'):
        return BlockType.QUOTE
    # Check for unordered list (every line starts with -)
    
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list (lines start with 1., 2., etc.)
    # Check for ordered list (lines start with 1., 2., etc.)
    if lines and lines[0].startswith('1. '):
        expected_number = 1
        is_ordered_list = True
        for line in lines:
            expected_number_str = f"{expected_number}. "
            if not line.startswith(expected_number_str):
                is_ordered_list = False
                break
            expected_number += 1
        if is_ordered_list:
            return BlockType.ORDERED_LIST
    # If none of the above, it's a paragraph
    return BlockType.PARAGRAPH
