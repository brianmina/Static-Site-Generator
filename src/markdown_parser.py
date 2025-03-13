import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def parse_bold(text):
    # Replace **text** with <b>text</b>
    import re
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

def parse_italic(text):
    # Replace _text_ or *text* with <i>text</i>
    import re
    text = re.sub(r'_([^_]+)_', r'<i>\1</i>', text)
    return re.sub(r'\*([^\*]+)\*', r'<i>\1</i>', text)

def parse_paragraph(text):
    # Handle existing paragraph logic and apply bold/italic parsing
    text = parse_bold(text)
    text = parse_italic(text)
    # Your existing paragraph logic here
    return f"<p>{text}</p>"


def parse_list(lines):
    list_type = "ul"
    if re.match(r'^\d+\.', lines[0].strip()):
        list_type = "ol"
    
    result = f"<{list_type}>"
    for line in lines:
        # Extract content after list marker
        if list_type == "ul":
            # For unordered lists: "- Item" or "* Item" -> "Item"
            item_content = re.sub(r'^[-*]\s*', '', line.strip())
        else:
            # For ordered lists: "1. Item" -> "Item"
            item_content = re.sub(r'^\d+\.\s*', '', line.strip())
        
        # Apply other formatting to the list item content
        item_content = parse_bold(item_content)
        item_content = parse_italic(item_content)
        
        # Add the list item to the result
        result += f"<li>{item_content}</li>"
    
    result += f"</{list_type}>"
    return result
