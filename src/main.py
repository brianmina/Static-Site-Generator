
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

def main():
    # Create a TextNode with some dummy values
    # Example: a link with anchor text
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    
    # Print the node
    print(node)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
