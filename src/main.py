
from generate_page import generate_page
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from copy_static import copy_static 
import os

def main():
    # Paths for your static and public directories
    static_path = "static"
    public_path = "public"
    
    # Copy static files to public directory
    copy_static(static_path, public_path)
    
    # Generate the main page
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = os.path.join(public_path, "index.html")
    
    generate_page(from_path, template_path, dest_path)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
