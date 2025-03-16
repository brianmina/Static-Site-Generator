from split_into_blocks import split_into_blocks
from htmlnode import HTMLNode
from block_type import BlockType, block_to_block_type
from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_image
from split_nodes_delimiter import split_nodes_delimiter
from markdown_parser import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def text_to_children(text):
    nodes = [TextNode(text, TextType.TEXT)]
    
    
    # Process bold text (** or __)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "__", TextType.BOLD)
    
    # Process italic text (* or _)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    # Process code text (`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    # Process links
    nodes = split_nodes_link(nodes)
    
    # Process images
    nodes = split_nodes_image(nodes)

    return nodes
    

    
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
            level = block.count("#", 0, 6)
            heading_text = block.lstrip("#").strip()
            node = HTMLNode(f"h{level}", children=text_to_children(heading_text))

        elif block_type == BlockType.CODE:
            # Wrap the code block in <pre><code>
            code_node = HTMLNode("code", children=[TextNode(block.strip("```"), TextType.TEXT)])
            node = HTMLNode("pre", children=[code_node])
        
        # Handle other cases like lists, quotes, etc., similarly
        elif block_type == BlockType.UNORDERED_LIST:
            print("Processing unordered list block:", repr(block))
            list_items = []
            for line in block.strip().split("\n"):
                print("  List line:", repr(line))
                item_text = line.lstrip("- ").strip()
                print("  Item text after stripping:", repr(item_text))
                children = text_to_children(item_text)
                print("  Children nodes:", children)
                list_items.append(HTMLNode("li", children=children))
            node = HTMLNode("ul", children=list_items)

        elif block_type == BlockType.ORDERED_LIST:
            print("Processing ordered list block:", repr(block))
            list_items = []
            for line in block.strip().split("\n"):
                print("  List line:", repr(line))
                item_text = line.lstrip("1234567890. ").strip()
                print("  Item text after stripping:", repr(item_text))
                children = text_to_children(item_text)
                print("  Children nodes:", children)
                list_items.append(HTMLNode("li", children=children))
            node = HTMLNode("ol", children=list_items)

        
        elif block_type == BlockType.QUOTE:
            # For a quote block, we strip the '>' characters
            quote_lines = []
            for line in block.strip().split("\n"):
                quote_lines.append(line.lstrip("> ").strip())
            quote_text = "\n".join(quote_lines)
            node = HTMLNode("blockquote", children=text_to_children(quote_text))
            print(f"Generated blockquote HTML: {node.to_html()}")  # Add this line
        # Append the created node to our list of child nodes
        child_nodes.append(node)
    
    # Create and return the parent node with all children
    return HTMLNode("div", children=child_nodes)

def test_simple_formatting():
    from markdown_to_html_node import markdown_to_html_node
    
    # Test bold text
    bold_md = "**bold text**"
    bold_html = markdown_to_html_node(bold_md).to_html()
    print(f"Bold test: {bold_md} -> {bold_html}")
    
    # Test italic text
    italic_md = "*italic text*"
    italic_html = markdown_to_html_node(italic_md).to_html()
    print(f"Italic test: {italic_md} -> {italic_html}")
    
    # Test code text
    code_md = "`code text`"
    code_html = markdown_to_html_node(code_md).to_html()
    print(f"Code test: {code_md} -> {code_html}")
    
    # Test a link
    link_md = "[Boot.dev](https://boot.dev)"
    link_html = markdown_to_html_node(link_md).to_html()
    print(f"Link test: {link_md} -> {link_html}")
    
    # Test an image
    img_md = "![alt text](image.jpg)"
    img_html = markdown_to_html_node(img_md).to_html()
    print(f"Image test: {img_md} -> {img_html}")

if __name__ == "__main__":
    test_simple_formatting()
