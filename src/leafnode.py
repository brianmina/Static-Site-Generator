

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value

        self_closing_tags = ["img", "br", "hr", "input", "meta", "link"]
    
        if self.tag in self_closing_tags:
            return f"<{self.tag}{self.props_to_html()}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
