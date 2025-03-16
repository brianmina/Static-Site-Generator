from extract_title import extract_title
import os
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.
    
    Args:
        from_path: Path to the markdown file
        template_path: Path to the HTML template
        dest_path: Path to write the generated HTML file
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    # Read the template file
    with open(template_path, "r") as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the final HTML tothe destination file
    with open(dest_path, "w") as f:
        f.write(final_html)



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages from markdown files
    """
    # Make sure the destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)
    
    # List all entries in the content directory
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        
        # If it's a directory, recursively process it
        if os.path.isdir(entry_path):
            # Create corresponding directory in destination
            rel_path = os.path.relpath(entry_path, dir_path_content)
            new_dest_dir = os.path.join(dest_dir_path, rel_path)
            os.makedirs(new_dest_dir, exist_ok=True)
            
            # Recursive call with updated paths
            generate_pages_recursive(entry_path, template_path, new_dest_dir)
        
        # If it's a markdown file, process it
        elif entry.endswith(".md"):
            # Create the destination file path with .html extension
            # Special case for index.md to keep it as index.html
            if entry == "index.md":
                dest_file = "index.html"
            else:
                dest_file = entry.replace(".md", ".html")
            
            dest_path = os.path.join(dest_dir_path, dest_file)
            
            # Generate the HTML page
            generate_page(entry_path, template_path, dest_path)
