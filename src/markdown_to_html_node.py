from split_into_blocks import split_into_blocks
from htmlnode import HTMLNode
from block_type import BlockType, block_to_block_type
from textnode import TextNode, TextType


def text_to_children(text):
    # For now, just create a simple text node with no special formatting
    return [TextNode(text, TextType.TEXT)]

def markdown_to_html_node(markdown):
    # Step 1: Split the markdown into blocks
    blocks = split_into_blocks(markdown)
    
    # Step 2: Create a list to collect child nodes
    child_nodes = []
    
    # Step 3: Loop over each block
    for block in blocks:
        # Determine the block type
        block_type = block_to_block_type(block)
        
        # Create the appropriate HTMLNode based on the block type
        if block_type == BlockType.PARAGRAPH:
            # Create a <p> node for paragraphs
            node = HTMLNode("p", children=text_to_children(block))
        elif block_type == BlockType.HEADING:
            # Determine the heading level (e.g., <h1>, <h2>)
            level = block.count("#", 0, 6)  # Count leading '#' characters
            node = HTMLNode(f"h{level}", children=text_to_children(block.lstrip("# ").strip()))
        elif block_type == BlockType.CODE:
            # Wrap the code block in <pre><code>
            code_node = HTMLNode("code", children=[TextNode(block.strip("```"), TextType.TEXT)])
            node = HTMLNode("pre", children=[code_node])
        # Handle other cases like lists, quotes, etc., similarly
        
        # Append the created node to our list of child nodes
        child_nodes.append(node)
    
    # Create and return the parent node with all children
    return HTMLNode("div", children=child_nodes)
