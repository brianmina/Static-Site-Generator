from text_node import TextNode, TextType
from markdown_parser import extract_markdown_links, extract_markdown_images

def split_nodes_link(old_nodes):
    new_nodes = []
    # For each node in old_nodes
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        link_delimiters = extract_markdown_links(text)

        if not link_delimiters:
            new_nodes.append(old_node)
            continue

        remaining_text = text

        for link_text, link_url in link_delimiters:
            link_markdown = f"[{link_text}]({link_url})"
            sections = remaining_text.split(link_markdown, 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    # For each node in old_nodes
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        # Use the image extraction function instead of link extraction
        image_delimiters = extract_markdown_images(text)

        if not image_delimiters:
            new_nodes.append(old_node)
            continue

        remaining_text = text

        for image_alt, image_url in image_delimiters:
            # Note the "!" before the opening bracket for images
            image_markdown = f"![{image_alt}]({image_url})"
            sections = remaining_text.split(image_markdown, 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            
            # Note TextType.IMAGE instead of TextType.LINK
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            if len(sections) > 1:
                remaining_text = sections[1]
            else:
                remaining_text = ""

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
