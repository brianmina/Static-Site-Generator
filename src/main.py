import sys
from generate_page import generate_page, generate_pages_recursive
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from copy_static import copy_static 
import os

def main():

    # Get the base path from command-line arguments or default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the root directory (one level up from script_dir)
    root_dir = os.path.dirname(script_dir)

    # Update paths to be relative to the root directory
    static_path = os.path.join(root_dir, "static")
    docs_path = os.path.join(root_dir, "docs")
    content_path = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")

    # Delete and recreate the public directory
    if os.path.exists(docs_path):
        # Use shutil to remove directory and all contents
        import shutil
        shutil.rmtree(docs_path)
    
    # Create the public directory
    os.makedirs(docs_path, exist_ok=True)
    
    # Copy static files to public directory
    copy_static(static_path, docs_path)
    
    # Generate the main page
    generate_pages_recursive(content_path, template_path, docs_path, basepath)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
