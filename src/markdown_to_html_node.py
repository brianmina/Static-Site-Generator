from split_into_blocks import split_into_blocks
from htmlnode import HTMLNode
from block_type import BlockType, block_to_block_type
def markdown_to_html_node(markdown):
    # Step 1: Split the markdown into blocks
    blocks = split_into_blocks(markdown)
    
    # Step 2: Create a parent HTMLNode (e.g., a <div>)
    parent_node = HTMLNode("div")
    
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
            code_node = HTMLNode("code", children=[TextNode(block.strip("```"))])
            node = HTMLNode("pre", children=[code_node])
        # Handle other cases like lists, quotes, etc., similarly
        
        # Append the created node as a child of the parent node
        parent_node.add_child(node)
    
    return parent_node


markdown_text = """
This is a paragraph.

Here is another paragraph.
"""

result = markdown_to_html_node(markdown_text)
print(result)
