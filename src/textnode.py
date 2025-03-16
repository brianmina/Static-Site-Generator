from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        # Return True if all properties are equal
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        # Return string representation
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html(self):
        # For text nodes, we need to handle the different text types
        if self.text_type == TextType.TEXT:
            return self.text
        elif self.text_type == TextType.BOLD:
            return f"<b>{self.text}</b>"
        elif self.text_type == TextType.ITALIC:
            return f"<i>{self.text}</i>"
        elif self.text_type == TextType.CODE:
            return f"<code>{self.text}</code>"
        elif self.text_type == TextType.LINK:
            # Assuming the URL is stored in the text itself
            # You might need to adjust this based on your implementation
            return f"<a href=\"{self.url}\">{self.text}</a>"
        elif self.text_type == TextType.IMAGE:
            return f"<img src=\"{self.url}\" alt=\"{self.text}\" />"
        else:
            # Default case
            return self.text
