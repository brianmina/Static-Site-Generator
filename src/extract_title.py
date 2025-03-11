def extract_title(markdown):
    """
    Extract the h1 header from a markdown string.
    
    Args:
        markdown: The markdown content as a string
        
    Returns:
        The title without the leading # and whitespace
        
    Raises:
        Exception: If no h1 header is found
    """
    lines = markdown.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    raise Exception("No h1 header found in the markdown content")
