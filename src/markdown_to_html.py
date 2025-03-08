from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from text_node import text_node_to_html_node
from block_type import block_to_block_type, BlockType
from markdown_blocks import markdown_to_blocks

def text_to_children(text):
    """
    Convert a text string with inline markdown to a list of HTML nodes
    
    Args:
        text: A string containing inline markdown
        
    Returns:
        list: A list of HTMLNode objects representing the inline markdown
    """
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

def block_to_html_node(block, block_type):
    """
    Convert a markdown block to an HTML node
    
    Args:
        block: A string containing a markdown block
        block_type: The type of the markdown block
        
    Returns:
        HTMLNode: An HTML node representing the markdown block
    """
    if block_type == BlockType.PARAGRAPH:
        return HTMLNode("p", None, None, text_to_children(block))
    elif block_type == BlockType.HEADING:
        # Count the number of # characters
        level = 0
        for char in block:
            if char == '#':
                level += 1
            else:
                break
        return HTMLNode(f"h{level}", None, None, text_to_children(block[level+1:]))
    elif block_type == BlockType.CODE:
        # Remove the ``` from start and end
        code_content = "\n".join(block.split("\n")[1:-1])
        # Create a text node (no inline parsing for code blocks)
        from text_node import TextNode
        text_node = TextNode(code_content, "text")
        code_node = HTMLNode("code", None, None, [text_node_to_html_node(text_node)])
        return HTMLNode("pre", None, None, [code_node])
    
    elif block_type == BlockType.QUOTE:
        # Remove the > prefix from each line
        lines = block.split("\n")
        quote_content = "\n".join([line[2:] if line.startswith("> ") else line[1:] for line in lines])
        return HTMLNode("blockquote", None, None, text_to_children(quote_content))
    
    elif block_type == BlockType.UNORDERED_LIST:
        list_items = []
        for line in block.split("\n"):
            # Remove the "- " prefix and convert the content to HTML nodes
            item_content = line[2:] if line.startswith

