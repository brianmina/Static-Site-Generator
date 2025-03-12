


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        # If we have a tag, create an HTML element
        if self.tag:
        # Start with the opening tag
            html = f"<{self.tag}"
        
         # Add any props/attributes
            if self.props:
                for prop, value in self.props.items():
                    html += f' {prop}="{value}"'
        
            html += ">"
        
        # Add children if any
            if self.children:
                for child in self.children:
                    html += child.to_html()
        
        # Close the tag
            html += f"</{self.tag}>"
            return html
    # If no tag, just concatenate the HTML of all children
        else:
            html = ""
            if self.children:
                for child in self.children:
                    html += child.to_html()
            return html


    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
