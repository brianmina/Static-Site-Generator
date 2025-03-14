from split_into_blocks import split_into_blocks
from htmlnode import HTMLNode
from block_type import BlockType, block_to_block_type
from textnode import TextNode, TextType


def text_to_children(text):
    """Convert markdown text to a list of TextNode objects."""
    # This is a simplified implementation. For a full implementation, you would
    # need to handle nested formatting and precedence rules more carefully.
    
    # Process the text nodes in order: links, images, bold, italic, code
    nodes = [TextNode(text, TextType.TEXT)]
    result = []
    
    # Process each node
    for node in nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        # Check for images ![alt](url)
        if "![" in node.text and "](" in node.text and ")" in node.text:
            start_img = node.text.find("![")
            end_alt = node.text.find("](", start_img)
            end_url = node.text.find(")", end_alt)
            
            if start_img >= 0 and end_alt >= 0 and end_url >= 0:
                # Text before the image
                if start_img > 0:
                    result.append(TextNode(node.text[:start_img], TextType.TEXT))
                
                # The image alt text and URL
                alt_text = node.text[start_img+2:end_alt]
                img_url = node.text[end_alt+2:end_url]
                
                result.append(TextNode(alt_text, TextType.IMAGE, img_url))
                
                # Text after the image
                if end_url + 1 < len(node.text):
                    result.append(TextNode(node.text[end_url+1:], TextType.TEXT))
            else:
                result.append(node)
        
        # Handle italic text (*text*)
        elif "*" in node.text and node.text.count("*") >= 2:  # Make sure there are at least 2 asterisks
            parts = node.text.split("*")
            is_italic = False
            temp_result = []
    
            for part in parts:
                if part == "":  # Skip empty parts (consecutive asterisks)
                    continue
            
                if is_italic:
                    temp_result.append(TextNode(part, TextType.ITALIC))
                else:
                    temp_result.append(TextNode(part, TextType.TEXT))
            
                is_italic = not is_italic
        
            result.extend(temp_result)

        # Check for bold text (**text**)
        if "**" in node.text:
            parts = node.text.split("**")
            for i in range(len(parts)):
                if i % 2 == 0:  # Regular text
                    if parts[i]:
                        result.append(TextNode(parts[i], TextType.TEXT))
                else:  # Bold text
                    if parts[i]:
                        result.append(TextNode(parts[i], TextType.BOLD))
        
        # Check for links
        elif "[" in node.text and "](" in node.text and ")" in node.text:
            # Find the positions
            start_link = node.text.find("[")
            end_text = node.text.find("](", start_link)
            end_link = node.text.find(")", end_text)
            
            if start_link >= 0 and end_text >= 0 and end_link >= 0:
                # Text before the link
                if start_link > 0:
                    result.append(TextNode(node.text[:start_link], TextType.TEXT))
                
                # The link text and URL
                link_text = node.text[start_link+1:end_text]
                link_url = node.text[end_text+2:end_link]
                
                result.append(TextNode(link_text, TextType.LINK, link_url))

                if end_link + 1 < len(node.text):
                    result.append(TextNode(node.text[end_link+1:], TextType.TEXT))
    return result

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
            heading_text = block.lstrip("#").strip()
            node = HTMLNode(f"h{level}", children=[TextNode(heading_text, TextType.TEXT)])
        
        elif block_type == BlockType.CODE:
            # Wrap the code block in <pre><code>
            code_node = HTMLNode("code", children=[TextNode(block.strip("```"), TextType.TEXT)])
            node = HTMLNode("pre", children=[code_node])
        
        # Handle other cases like lists, quotes, etc., similarly
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in block.strip().split("\n"):
                item_text = line.lstrip("- ").strip()
                list_items.append(HTMLNode("li", children=text_to_children(item_text)))
            node = HTMLNode("ul", children=list_items)

        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            for line in block.strip().split("\n"):
                item_text = line.lstrip("1234567890. ").strip()
                list_items.append(HTMLNode("li", children=text_to_children(item_text)))
            node = HTMLNode("ol", children=list_items)
        
        elif block_type == BlockType.QUOTE:
            # For a quote block, we strip the '>' characters
            quote_lines = []
            for line in block.strip().split("\n"):
                quote_lines.append(line.lstrip("> ").strip())
            quote_text = "\n".join(quote_lines)
            node = HTMLNode("blockquote", children=text_to_children(quote_text))
        # Append the created node to our list of child nodes
        child_nodes.append(node)
    
    # Create and return the parent node with all children
    return HTMLNode("div", children=child_nodes)
