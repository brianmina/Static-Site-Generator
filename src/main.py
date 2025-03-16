
from generate_page import generate_page
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from copy_static import copy_static 
import os

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the root directory (one level up from script_dir)
    root_dir = os.path.dirname(script_dir)

    # Update paths to be relative to the root directory
    static_path = os.path.join(root_dir, "static")
    public_path = os.path.join(root_dir, "public")
    from_path = os.path.join(root_dir, "content/index.md")
    template_path = os.path.join(root_dir, "template.html")

    # Delete and recreate the public directory
    if os.path.exists(public_path):
        # Use shutil to remove directory and all contents
        import shutil
        shutil.rmtree(public_path)
    
    # Create the public directory
    os.makedirs(public_path, exist_ok=True)
    
    # Copy static files to public directory
    copy_static(static_path, public_path)
    
    # Generate the main page
    dest_path = os.path.join(public_path, "index.html")
    
    generate_page(from_path, template_path, dest_path)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
