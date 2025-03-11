
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from copy_static import copy_static 

def main():
     # Paths for your static and public directories
    static_path = "static"
    public_path = "public"
    
    # Copy static files to public directory
    copy_static(static_path, public_path)
    # Create a TextNode with some dummy values
    # Example: a link with anchor text
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the node
    print(node)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
